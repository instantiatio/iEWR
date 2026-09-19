"""Explicit read-only Human View projection -> immutable offline HTML.

No discovery, semantic classification, response handling or execution. Standard
library only. Cooperative file checks do not establish truth or host isolation.
"""
import argparse
from hashlib import sha256
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from decision_view.snapshot import (LIMIT, fields, text, sequence, timestamp,
                                    local_path, read_local, unique_object)

STYLE = Path(__file__).resolve().parents[1] / 'decision_view' / 'style.css'
KINDS = {'situation': ('Ситуация', 'state'), 'change': ('Изменение', 'delta'),
         'plan': ('План', 'course'), 'review': ('Проверка', 'review'),
         'result': ('Результат', 'outcome')}
LEVELS = {'core': 0, 'standard': 1, 'deep': 2}
MODES = {'GLANCE': 0, 'STANDARD': 1, 'DEEP': 2}
TONES = {'neutral': 'Сведения', 'attention': 'Внимание',
         'blocking': 'Блокирующее условие', 'success': 'Подтверждённый результат'}
esc = lambda value: escape(str(value), quote=True)


def strings(values, where):
    sequence(values, where)
    for value in values:
        text(value, where)
    return '<ul>' + ''.join('<li>' + esc(v) + '</li>' for v in values) + '</ul>' if values else ''


def table(columns, rows, title):
    return ('<div class="table-wrap" role="region" aria-label="' + esc(title)
            + '" tabindex="0"><table><caption>' + esc(title) + '</caption><thead><tr>'
            + ''.join('<th scope="col">' + esc(c) + '</th>' for c in columns)
            + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + esc(c)
              + '</td>' for c in row) + '</tr>' for row in rows) + '</tbody></table></div>')


def section_content(section):
    fmt, value = section['format'], section['content']
    if fmt == 'text':
        text(value, 'section.content')
        return '<p>' + esc(value) + '</p>'
    if fmt == 'list':
        result = strings(value, 'section.content')
        if not value:
            raise ValueError('Пустая секция не нужна')
        return result
    if fmt == 'table':
        fields(value, 'columns rows', 'table')
        strings(value['columns'], 'table.columns')
        if not 1 <= len(value['columns']) <= 12:
            raise ValueError('Таблица: 1–12 столбцов')
        sequence(value['rows'], 'table.rows')
        if not value['rows']:
            raise ValueError('Таблица без строк')
        for row in value['rows']:
            strings(row, 'table.row')
            if len(row) != len(value['columns']):
                raise ValueError('Число ячеек не совпадает со столбцами')
        return table(value['columns'], value['rows'], section['title'])
    if fmt == 'change':
        sequence(value, 'change')
        if not value:
            raise ValueError('Нет переданных изменений')
        result = []
        for change in value:
            fields(change, 'subject before after consequence', 'change.row')
            for key in change:
                text(change[key], 'change.' + key)
            result.append('<section class="change"><h3>' + esc(change['subject'])
                          + '</h3><dl>' + ''.join('<dt>' + label + '</dt><dd>'
                          + esc(change[key]) + '</dd>' for key, label in
                          [('before', 'Было'), ('after', 'Стало'), ('consequence', 'Последствия')])
                          + '</dl></section>')
        return ''.join(result)
    raise ValueError('Неизвестная форма секции')


class PlainText(HTMLParser):
    """Complete text fallback from the same escaped, script-free body."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'h1', 'h2', 'h3', 'p', 'li', 'dt', 'dd', 'tr', 'summary', 'section'}:
            self.parts.append('\n')
        if tag in {'td', 'th'}:
            self.parts.append(' | ')
        if tag == 'a':
            self.parts.append(' [' + dict(attrs).get('href', '') + '] ')

    def handle_data(self, data):
        self.parts.append(data)


def render(data, input_path, output_path, root):
    fields(data, 'schema id revision kind title subject recipient summary status asOf scope '
           'coverage limits attention sections materials refreshWhen next synthetic', 'view')
    if type(data['schema']) is not int or data['schema'] != 1:
        raise ValueError('Поддерживается только schema:1')
    for key in ('id', 'revision', 'title', 'subject', 'recipient', 'summary', 'scope', 'refreshWhen', 'next'):
        text(data[key], key)
    if not isinstance(data['kind'], str) or data['kind'] not in KINDS:
        raise ValueError('Read-only kind: situation/change/plan/review/result; решения — Decision View')
    if type(data['synthetic']) is not bool:
        raise ValueError('synthetic должен быть boolean')
    timestamp(data['asOf'], 'asOf', False)
    fields(data['status'], 'label tone', 'status')
    text(data['status']['label'], 'status.label')
    if not isinstance(data['status']['tone'], str) or data['status']['tone'] not in TONES:
        raise ValueError('Неизвестный status.tone')
    fields(data['attention'], 'mode reason', 'attention')
    text(data['attention']['reason'], 'attention.reason')
    mode = data['attention']['mode']
    if not isinstance(mode, str) or mode not in MODES:
        raise ValueError('Неизвестный attention.mode')
    fields(data['coverage'], 'sources omissions', 'coverage')
    omissions = strings(data['coverage']['omissions'], 'coverage.omissions')
    limits = strings(data['limits'], 'limits')
    bindings, gaps = {}, []

    def references(refs, where):
        sequence(refs, where)
        result = []
        for ref in refs:
            fields(ref, 'label revision purpose path sha256', where)
            for key in ('label', 'revision', 'purpose'):
                text(ref[key], where + '.' + key)
            name, expected = ref['path'], ref['sha256']
            text(name, where + '.path', True)
            if expected is not None and (not isinstance(expected, str) or not re.fullmatch('[a-f0-9]{64}', expected)):
                raise ValueError('Некорректный SHA-256')
            label = ref['label'] + ' · ' + ref['revision']
            if name is None:
                gaps.append(label + ': локальный источник не предоставлен; ' + ref['purpose'])
                link = esc(label)
            else:
                parsed = urlsplit(name)
                if (parsed.scheme or parsed.netloc or parsed.query or parsed.fragment
                        or '\\' in name or ':' in name or '%' in name or name.startswith('/')
                        or any(ord(c) < 32 for c in name)):
                    raise ValueError('Нужна относительная локальная ссылка без URL/fragment')
                path = local_path(input_path.parent / name, root)
                if not path.is_file():
                    gaps.append(label + ': файл отсутствует: ' + name)
                    link = esc(label + ' — ' + name)
                else:
                    raw = read_local(path, 32 * LIMIT)
                    digest = sha256(raw).hexdigest()
                    if expected is None:
                        raise ValueError('Для доступного файла нужен ожидаемый SHA-256: ' + name)
                    if digest != expected or path in bindings and bindings[path] != digest:
                        raise ValueError('Редакция источника изменилась: ' + name)
                    bindings[path] = digest
                    href = quote(os.path.relpath(path, output_path.parent).replace(os.sep, '/'), safe='/')
                    link = '<a href="' + esc(href) + '">' + esc(label) + '</a>'
                    if path.suffix.lower() == '.zip':
                        link = ('<details><summary>' + esc(label) + ' · ZIP</summary><p>'
                                + esc(path.name) + ' · ' + str(len(raw)) + ' байт</p><a href="'
                                + esc(href) + '" download="' + esc(path.name) + '">Скачать ZIP</a></details>')
            result.append('<li>' + link + ' — ' + esc(ref['purpose'])
                          + '<small>Файл: ' + esc(name or 'не предоставлен')
                          + '. Если недоступен, запросите эту редакцию у автора представления.</small></li>')
        return '<ul>' + ''.join(result) + '</ul>' if result else ''

    sources = references(data['coverage']['sources'], 'coverage.sources')
    materials = references(data['materials'], 'materials')
    if not data['coverage']['sources']:
        gaps.append('Источники охвата не предоставлены; содержание требует отдельной проверки.')
    sequence(data['sections'], 'sections', 30)
    seen, sections, disclosures = set(), [], []
    primary = KINDS[data['kind']][1]
    for section in data['sections']:
        fields(section, 'id title level format content', 'section')
        ident = section['id']
        if not isinstance(ident, str) or not re.fullmatch('[a-z][a-z0-9-]{0,63}', ident) or ident in seen:
            raise ValueError('Повторный или неверный section.id')
        seen.add(ident)
        text(section['title'], 'section.title')
        level = section['level']
        if not isinstance(level, str) or level not in LEVELS:
            raise ValueError('Неизвестный уровень секции')
        if ident == primary and (level != 'core' or data['kind'] == 'change' and section['format'] != 'change'):
            raise ValueError('Основная секция всегда core; delta имеет format:change')
        content = section_content(section)
        if level == 'core':
            sections.append('<section id="' + ident + '"><h2>' + esc(section['title']) + '</h2>' + content + '</section>')
        else:
            opened = ' open' if LEVELS[level] <= MODES[mode] else ''
            sections.append('<details id="' + ident + '"' + opened + '><summary>'
                            + esc(section['title']) + '</summary>' + content + '</details>')
            disclosures.append(section['title'])
    if primary not in seen:
        raise ValueError('Нужна основная секция ' + primary)
    tone = data['status']['tone']
    body = ('<header><p class="meta">' + KINDS[data['kind']][0] + ' · ' + esc(data['id'])
            + ' · редакция ' + esc(data['revision']) + '</p><h1>' + esc(data['title'])
            + '</h1><p>' + esc(data['subject']) + '</p><p class="meta">Для: ' + esc(data['recipient'])
            + ' · Снимок на ' + esc(data['asOf']) + '</p></header>')
    if data['synthetic']:
        body += '<p class="notice">Учебный пример. Факты условные; это не действующий запрос или решение проекта.</p>'
    body += ('<p class="status ' + tone + '">' + TONES[tone] + ': ' + esc(data['status']['label'])
             + '</p><section class="summary"><h2>Главное</h2><p>' + esc(data['summary']) + '</p></section>')
    if limits:
        body += '<section class="limits"><h2>Существенные ограничения</h2>' + limits + '</section>'
    if gaps:
        body += '<section class="notice"><h2>Пробелы оснований</h2>' + strings(gaps, 'gaps') + '</section>'
    body += ('<p class="attention"><strong>Глубина: ' + mode + '</strong> · ' + esc(data['attention']['reason'])
             + ('<br>Детали доступны в любом режиме: ' + esc('; '.join(disclosures)) + '.' if disclosures else '<br>Дополнительных слоёв нет.')
             + ' Режим задаёт начальное раскрытие, не время чтения.</p>' + ''.join(sections)
             + '<section class="next"><h2>Что дальше</h2><p>' + esc(data['next']) + '</p></section>'
             + '<section class="coverage"><h2>Охват и актуальность</h2><p>' + esc(data['scope']) + '</p>'
             + ('<h3>Не включено / не проверено</h3>' + omissions if omissions else '<p>Составитель не указал исключений; полнота автоматически не проверена.</p>')
             + '<p><strong>Когда сверить и обновить: </strong>' + esc(data['refreshWhen']) + '</p></section>')
    if sources or materials:
        body += '<section class="materials"><h2>Основания и материалы</h2>' + sources + materials + '</section>'
    canonical = json.loads(json.dumps(data))
    canonical['attention'].pop('mode')
    content_digest = sha256(json.dumps(canonical, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()
    body += ('<footer><p class="hint">Представление для чтения. Открытие, раскрытие и сохранение не являются ответом, приёмкой или разрешением действия. Обсудите замечания в текущей задаче, указав предмет и редакцию.</p>'
             + '<p class="meta">SHA-256 содержания (без режима раскрытия): ' + content_digest + '</p></footer>')
    css = read_local(STYLE).decode('utf-8')
    result = ('<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
              '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'">'
              '<title>' + esc(data['title']) + '</title><style>' + css + '</style></head><body><main>' + body + '</main></body></html>')
    fallback = PlainText()
    fallback.feed(body)
    return result.encode('utf-8'), gaps, bindings, ''.join(fallback.parts).strip() + '\n', content_digest


def build(input_path, output_path, root, text_only=False):
    root = Path(os.path.abspath(root))
    if not root.is_dir() or root.resolve() != root:
        raise ValueError('Нужен существующий root без ссылок')
    input_path = local_path(input_path, root)
    output_path = local_path(output_path, root)
    relative = output_path.relative_to(root).as_posix()
    if not relative.startswith(('project/handoff/', 'project/artifacts/')) or output_path.suffix.lower() != '.html':
        raise ValueError('Выход: новый .html в project/handoff или project/artifacts')
    if not output_path.parent.is_dir():
        raise ValueError('Каталог результата должен существовать')
    raw = read_local(input_path)
    data = json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object)
    html, gaps, bindings, fallback, content_digest = render(data, input_path, output_path, root)
    bindings[input_path] = sha256(raw).hexdigest()
    for path, digest in bindings.items():
        local_path(path, root)
        if sha256(read_local(path, 32 * LIMIT)).hexdigest() != digest:
            raise ValueError('Основание изменилось во время подготовки')
    if text_only:
        return fallback
    with output_path.open('xb') as target:
        target.write(html)
    if output_path.read_bytes() != html:
        raise ValueError('Результат изменился после записи; сохранить для разбора')
    return {'path': str(output_path), 'bytes': len(html), 'sha256': sha256(html).hexdigest(),
            'input_sha256': sha256(raw).hexdigest(), 'content_sha256': content_digest,
            'diagnostics': gaps, 'limit': 'Read-only snapshot; no response, authority or automatic refresh.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--text', action='store_true', help='Полное содержание в stdout; файл не создаётся')
    args = parser.parse_args()
    try:
        result = build(args.input, args.output, args.root, args.text)
        print(result if args.text else json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, RecursionError) as error:
        print(json.dumps({'error': str(error), 'action': 'Сверить вход; использовать текст по тем же основаниям. Старые файлы сохранить.'}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
