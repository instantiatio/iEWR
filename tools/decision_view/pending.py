"""Render an explicit, read-only pending-question projection. No owner mutation.

Cooperative local files only. The caller supplies scope, order and assessments;
digests and structural checks establish neither authority nor permission.
"""
import argparse
from collections import Counter
from datetime import datetime
from hashlib import sha256
from html import escape
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import quote, urlsplit


STATES = {
    "ready": "Нужен ответ",
    "preparing": "Готовится",
    "needs-recipient": "Нужен адресат",
    "conditions": "Ответ получен, проверяются условия",
    "conflict": "Конфликт или устарело",
    "closed": "Применено либо отказано — см. основания",
}
LIMIT = 1024 * 1024


try:  # CLI and package imports retain the existing public helper names.
    from .snapshot import fields, text, sequence, timestamp, local_path, read_local, unique_object, relative_href
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from snapshot import fields, text, sequence, timestamp, local_path, read_local, unique_object, relative_href


def render(data, input_path, output_path, root):
    """Return HTML bytes, diagnostics, and read bindings for the publication check."""
    fields(data, 'schema scope asOf coverage items', 'projection')
    if type(data['schema']) is not int or data['schema'] != 1:
        raise ValueError('Поддерживается только schema:1')
    text(data['scope'], 'scope')
    timestamp(data['asOf'], 'asOf', False)
    fields(data['coverage'], 'sources omissions', 'coverage')
    sequence(data['items'], 'items')
    bindings, diagnostics = {}, []
    esc = lambda value: escape(str(value), quote=True)

    def string_list(values, where):
        sequence(values, where)
        for value in values:
            text(value, where)
        return '<ul>' + ''.join('<li>' + esc(v) + '</li>' for v in values) + '</ul>' if values else '<p>Не указано.</p>'

    def reference(ref, where, gaps):
        if ref is None:
            gaps.append(f'{where}: основание не установлено')
            return '<span>Не установлено</span>'
        fields(ref, 'label path sha256', where)
        text(ref['label'], where + '.label')
        text(ref['path'], where + '.path', True)
        if ref['sha256'] is not None and (not isinstance(ref['sha256'], str) or
                not re.fullmatch('[a-f0-9]{64}', ref['sha256'])):
            raise ValueError(f'{where}: неверный SHA-256')
        if ref['path'] is None:
            gaps.append(f'{where}: источник вне доступной локальной проверки')
            return esc(ref['label']) + ' — локальный источник не указан'
        name = ref['path']
        parsed = urlsplit(name)
        if (parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or
                '\\' in name or ':' in name or name.startswith('/') or
                any(ord(c) < 32 for c in name) or '%' in name):
            raise ValueError(f'{where}: нужна относительная локальная ссылка без URL/fragment')
        path = local_path(input_path.parent / name, root)
        if not path.is_file():
            gaps.append(f'{where}: файл отсутствует')
            return esc(ref['label']) + ' — файл отсутствует: ' + esc(name)
        raw = read_local(path, 32 * LIMIT)
        actual = sha256(raw).hexdigest()
        if path in bindings and bindings[path] != actual:
            raise ValueError(f'{where}: источник изменился между чтениями')
        bindings[path] = actual
        if ref['sha256'] is None:
            gaps.append(f'{where}: ожидаемый digest не установлен')
        elif actual != ref['sha256']:
            gaps.append(f'{where}: digest не совпадает, нужна сверка')
        href = relative_href(path, output_path.parent)
        return (f'<a href="{esc(href)}">{esc(ref["label"])}</a>'
                f'<small>Файл: {esc(name)} · ожидаемый SHA-256: {esc(ref["sha256"] or "не установлен")}'
                f' · прочитанный: {actual}</small>')

    def references(values, where, gaps):
        sequence(values, where)
        return '<ul>' + ''.join('<li>' + reference(v, where, gaps) + '</li>' for v in values) + '</ul>' if values else '<p>Нет записей в проекции.</p>'

    omissions = string_list(data['coverage']['omissions'], 'coverage.omissions')
    coverage_gaps = []
    coverage = references(data['coverage']['sources'], 'coverage.sources', coverage_gaps)
    if not data['coverage']['sources']:
        coverage_gaps.append('Источники охвата не указаны')
    diagnostics.extend(coverage_gaps)
    keys, graph, entries = set(), {}, {}
    required = ('id revision subject question role decider contribution gateBasis authority '
                'state missingInput answerBy deadlineBasis validUntil priorityReason '
                'dependsOn externalDependencies dependentActions independentWork '
                'response conditions revocation effects sources refreshWhen')
    for item in data['items']:
        fields(item, required, 'item')
        for field in ('id', 'revision', 'subject', 'role', 'contribution', 'priorityReason', 'refreshWhen'):
            text(item[field], field)
        text(item['decider'], 'decider', True)
        if not isinstance(item['state'], str) or item['state'] not in STATES:
            raise ValueError('Неизвестное состояние показа')
        key = (item['id'], item['revision'])
        if key in keys:
            raise ValueError('Повтор ID + revision')
        keys.add(key)
        entries[key] = item
        sequence(item['dependsOn'], 'dependsOn')
        deps = []
        for dependency in item['dependsOn']:
            fields(dependency, 'id revision', 'dependsOn')
            text(dependency['id'], 'dependsOn.id')
            text(dependency['revision'], 'dependsOn.revision')
            deps.append((dependency['id'], dependency['revision']))
        if len(deps) != len(set(deps)):
            raise ValueError('Повтор локальной зависимости')
        graph[key] = deps

    def cyclic(start):
        todo, seen = list(graph[start]), set()
        while todo:
            key = todo.pop()
            if key == start:
                return True
            if key not in seen:
                seen.add(key)
                todo.extend(graph.get(key, []))
        return False

    def anchor(key):
        return 'q-' + sha256(json.dumps(key, ensure_ascii=False).encode()).hexdigest()

    def labelled(label, content):
        return '<div class="field"><h3>' + label + '</h3>' + content + '</div>'

    cards = []
    for item in data['items']:
        key = (item['id'], item['revision'])
        gaps = []
        question = reference(item['question'], 'Вопрос', gaps)
        authority = reference(item['authority'], 'Полномочия', gaps)
        gate = reference(item['gateBasis'], 'Основание участия человека', gaps)
        if item['decider'] is None:
            gaps.append('Адресат / decider не установлен')
        timestamp(item['answerBy'], 'answerBy')
        timestamp(item['validUntil'], 'validUntil')
        for field, label in (('answerBy', 'Нужный момент ответа'), ('validUntil', 'Срок действия основания')):
            if item[field] is not None and datetime.fromisoformat(item[field].replace('Z', '+00:00')) < datetime.fromisoformat(data['asOf'].replace('Z', '+00:00')):
                gaps.append(label + ' предшествует моменту снимка; нужна сверка')
        deadline = reference(item['deadlineBasis'], 'Основание срока', gaps) if item['deadlineBasis'] is not None or item['answerBy'] is not None or item['validUntil'] is not None else 'Сроки не установлены'
        missing = string_list(item['missingInput'], 'missingInput')
        if item['state'] == 'ready' and item['missingInput']:
            gaps.append('Заявленная готовность требует сверки: есть недостающий вход')
        if item['state'] == 'ready' and item['response'] is not None:
            gaps.append('Заявлен новый ответ при уже сохранённом ответе: сверить предмет')
        if item['state'] == 'conditions' and item['response'] is None:
            gaps.append('Заявлен полученный ответ без ссылки на него')
        if item['revocation'] is not None:
            gaps.append('Указан отзыв: сверить текущие основания и фактические эффекты')
        if cyclic(key):
            gaps.append('Цикл локальных зависимостей: требуется разбор')
        dependency_lines = []
        for dep in graph[key]:
            label = esc(dep[0] + ' / ' + dep[1])
            if dep not in keys:
                gaps.append('Зависимость вне выборки: ' + dep[0] + ' / ' + dep[1])
                dependency_lines.append(label + ' — вне выборки, не подтверждена')
            else:
                dependency_lines.append(f'<a href="#{anchor(dep)}">{label}</a> — {STATES[entries[dep]["state"]]}; это не подтверждение выполнения условия')
        dependencies = '<ul>' + ''.join('<li>' + d + '</li>' for d in dependency_lines) + '</ul>' if dependency_lines else '<p>Локальные зависимости не указаны.</p>'
        external = references(item['externalDependencies'], 'Внешняя зависимость', gaps)
        dependent = string_list(item['dependentActions'], 'dependentActions')
        independent = string_list(item['independentWork'], 'independentWork')
        response = reference(item['response'], 'Ответ', gaps) if item['response'] is not None else 'Ответ в проекции отсутствует; это не отказ.'
        revocation = reference(item['revocation'], 'Отзыв', gaps) if item['revocation'] is not None else 'Отзыв в проекции не указан; отсутствие отзыва не проверяется автоматически.'
        sequence(item['conditions'], 'conditions')
        conditions = []
        for condition in item['conditions']:
            fields(condition, 'text owner criterion evidence', 'condition')
            text(condition['text'], 'condition.text')
            text(condition['owner'], 'condition.owner', True)
            text(condition['criterion'], 'condition.criterion', True)
            if condition['owner'] is None or condition['criterion'] is None or not condition['evidence']:
                gaps.append('Условие: владелец, критерий или evidence не установлены')
            conditions.append('<li>' + esc(condition['text']) + '<p>Проверяющий: ' + esc(condition['owner'] or 'не установлен') + ' · критерий: ' + esc(condition['criterion'] or 'не установлен') + '</p>' + references(condition['evidence'], 'Evidence условия', gaps) + '</li>')
        sources = references(item['sources'], 'Источники строки', gaps)
        if not item['sources']:
            gaps.append('Источники строки не указаны')
        effects = references(item['effects'], 'Фактические эффекты', gaps)
        diagnostics.extend(f'{key[0]}/{key[1]}: {gap}' for gap in gaps)
        warnings = '<ul>' + ''.join('<li>' + esc(gap) + '</li>' for gap in gaps) + '</ul>' if gaps else '<p>Структурных пробелов не обнаружено; основания действия всё равно проверяются отдельно.</p>'
        cards.append(f'<article id="{anchor(key)}"><p class="state">{STATES[item["state"]]} — оценка составителя</p>'
                     f'<h2>{esc(item["id"])} / {esc(item["revision"])} · {esc(item["subject"])}</h2>'
                     f'<p><b>{esc(item["role"])}</b> · адресат: {esc(item["decider"] or "не установлен")}</p>'
                     f'<p>Нужный вклад: {esc(item["contribution"])}</p><p>Причина порядка: {esc(item["priorityReason"])}</p>'
                     + labelled('Вопрос', question) + labelled('Пробелы и ограничения', warnings)
                     + labelled('Срок ответа и срок действия', f'<p>Ответ нужен: {esc(item["answerBy"] or "неизвестно")} · действие основания до: {esc(item["validUntil"] or "неизвестно")}</p>{deadline}')
                     + labelled('Недостающий вход', missing)
                     + labelled('Все необходимые зависимости (AND)', dependencies + external)
                     + labelled('Зависимое действие', dependent) + labelled('Независимое разрешённое продолжение — по основаниям составителя', independent)
                     + labelled('Ответ', response) + labelled('Условия', '<ul>' + ''.join(conditions) + '</ul>' if conditions else '<p>Условия в проекции не указаны.</p>')
                     + labelled('Отзыв', revocation) + labelled('Фактические эффекты', effects)
                     + '<details><summary>Прямые основания и источники</summary>'
                     + labelled('Основание участия человека', gate) + labelled('Полномочия', authority)
                     + labelled('Источники строки', sources) + '</details>'
                     + labelled('Когда сверить и обновить', '<p>' + esc(item['refreshWhen']) + '</p>') + '</article>')
    counts = Counter(i['state'] for i in data['items'])
    summary = ' · '.join(f'{label}: {counts[state]}' for state, label in STATES.items())
    empty = '<p>В выбранной проекции нет вопросов. Это не доказывает отсутствие ожиданий вне её охвата.</p>' if not cards else ''
    html = '''<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Ожидаемые решения</title><style>
''' + (Path(__file__).parent / 'style.css').read_text(encoding='utf-8') + '''
article,.coverage{border:1px solid var(--border);padding:24px;margin:24px 0}small{display:block}.state{font-weight:650}li,p,h2{white-space:pre-wrap}
</style></head><body><main><h1>Ожидаемые решения</h1>'''
    html += (f'<p>{esc(data["scope"])}</p><p>Снимок на {esc(data["asOf"])}</p>'
             '<p class="notice">Только навигация. Снимок не обновляется автоматически и не разрешает действий. Перед использованием сверить текущие источники, условия, отзывы и эффекты. Ответы даются по отдельным вопросам.</p>'
             f'<p>{esc(summary)}</p><section class="coverage"><h2>Охват и непроверенное</h2>{coverage}<h3>Не проверено / не включено</h3>{omissions}'
             + '<ul>' + ''.join('<li>' + esc(gap) + '</li>' for gap in coverage_gaps) + '</ul></section>' + empty + ''.join(cards)
             + '</main></body></html>')
    return html.encode('utf-8'), diagnostics, bindings


def build(input_path, output_path, root):
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
    html, diagnostics, bindings = render(data, input_path, output_path, root)
    bindings[input_path] = sha256(raw).hexdigest()
    for path, digest in bindings.items():
        local_path(path, root)
        if sha256(read_local(path, 32 * LIMIT)).hexdigest() != digest:
            raise ValueError('Основание изменилось во время подготовки; повторно сверить источники')
    # Exclusive creation prevents replacement by competing cooperative writers.
    # This is not an atomic snapshot of sources and destination or host isolation.
    with output_path.open('xb') as target:
        target.write(html)
    if output_path.read_bytes() != html:
        raise ValueError('Результат изменился после записи; сохранить файл для разбора')
    return {'path': str(output_path), 'bytes': len(html), 'sha256': sha256(html).hexdigest(),
            'input_sha256': sha256(raw).hexdigest(), 'diagnostics': diagnostics,
            'limit': 'Static local snapshot; no permission, delivery, response assessment or execution.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--root', default='.')
    args = parser.parse_args()
    try:
        result = build(Path(args.input), Path(args.output), Path(args.root))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, RecursionError) as error:
        print(json.dumps({'error': str(error), 'action': 'Сверить вход; использовать отдельные вопросы. Существующие результаты не заменять.'}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
