"""Stdlib renderer: ready decision data -> one portable HTML; never overwrite."""
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import time
from urllib.parse import quote, urlsplit

HERE = Path(__file__).resolve().parent
PRESETS = {'short-decision': 'Основания', 'comparison': 'Что различает варианты', 'acceptance': 'Основания приёмки'}
esc = lambda value: html.escape(str(value), quote=True)
sha = lambda value: hashlib.sha256(value).hexdigest()

def json_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')

def write_new(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Hashes and sizes refer to exact UTF-8 bytes, independent of host newlines.
    with path.open('xb') as f:
        f.write(text.encode('utf-8'))

def table_html(table):
    return '<div class="table-wrap"><table><caption>'+esc(table['title'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in table['columns'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in row)+'</tr>' for row in table['rows'])+'</tbody></table></div>'

def render(source, output, source_dir):
    if source.get('decisionRequired') is False:
        return None
    d = json.loads(json.dumps(source))
    if d['kind'] not in PRESETS:
        raise ValueError('Unknown content preset')
    for key in ('questionId', 'question', 'subject', 'recipient', 'recommendation', 'waiting'):
        if not isinstance(d.get(key), str) or not d[key].strip():
            raise ValueError('Missing '+key)
    options = d.get('options', [])
    attention = d.get('attention')
    if attention is not None:
        if (not isinstance(attention, dict) or set(attention) != {'mode', 'reason'}
                or attention.get('mode') not in ('GLANCE', 'STANDARD', 'DEEP')
                or not isinstance(attention.get('reason'), str) or not attention['reason'].strip()):
            raise ValueError('attention requires mode GLANCE/STANDARD/DEEP and reason')
    ids = [o['id'] for o in options]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r'[a-zA-Z0-9_-]+', i) for i in ids):
        raise ValueError('Invalid option IDs')
    d['options'] = options
    d['schema'] = 1
    output = Path(output).resolve()
    d['answerFilename'] = output.stem.removesuffix('-question')+'-answer.html'
    for material in d.get('materials', []):
        parsed = urlsplit(material['path'])
        if parsed.scheme not in ('', 'http', 'https') or material['path'].startswith('//'):
            raise ValueError('Unsupported material link')
        if not parsed.scheme:
            local = (Path(source_dir)/material['path']).resolve()
            if not local.is_file():
                raise ValueError('Material unavailable during build: '+str(local))
            digest = sha(local.read_bytes())
            if material.get('sha256') and material['sha256'] != digest:
                raise ValueError('Material revision mismatch: '+material['filename'])
            if local.name != material['filename']:
                raise ValueError('Material filename mismatch')
            material['sha256'] = digest
            material['bytes'] = local.stat().st_size
            if local.suffix.lower() == '.md':
                script=HERE/'render_markdown.cjs'
                css=(HERE/'style.css').read_text(encoding='utf-8')
                reader_id=sha(local.read_bytes()+script.read_bytes()+(HERE/'vendor/marked.cjs').read_bytes()+css.encode())[:10]
                reader=output.parent/'decision-view-materials'/(local.stem+'-'+reader_id+'.html')
                payload={'markdown':local.read_text(encoding='utf-8'),'sourcePath':str(local),
                         'outputPath':str(reader),'title':material['title'],'revision':material.get('revision'),
                         'sourceSHA256':digest,'css':css}
                rendered=subprocess.run(['node',str(script)],input=json.dumps(payload),text=True,capture_output=True,check=True,timeout=20).stdout
                if reader.exists():
                    if reader.read_text(encoding='utf-8')!=rendered:raise ValueError('Existing reader differs; preserve it and issue a new representation')
                else:write_new(reader,rendered)
                material['source']={'path':quote(os.path.relpath(local,output.parent),safe='/'),
                                    'filename':local.name,'sha256':digest}
                local=reader
                material['filename']=reader.name
                saved=reader.read_bytes()
                material['sha256']=sha(saved)
                material['bytes']=len(saved)
            if local.name.endswith('.er.json'):
                from er import render as render_er
                raw=local.read_bytes()
                rendered=render_er(json.loads(raw),local.name,digest)
                reader=output.parent/'decision-view-materials'/(local.name[:-8]+'-'+sha(rendered.encode())[:10]+'.html')
                if reader.exists():
                    if reader.read_text(encoding='utf-8')!=rendered:raise ValueError('ER reader collision')
                else:write_new(reader,rendered)
                material['source']={'path':quote(os.path.relpath(local,output.parent),safe='/'),
                                    'filename':local.name,'sha256':digest}
                local=reader;material['filename']=reader.name
                saved=reader.read_bytes()
                material['sha256']=sha(saved);material['bytes']=len(saved)
            if local.suffix.lower() == '.zip':material['presentation']='download'
            material['path'] = quote(os.path.relpath(local, output.parent), safe='/')
        elif parsed.path.lower().endswith('.zip'):
            material['presentation']='download'
    d['documentId'] = sha(json_text(d).encode())
    blocks = []
    if d.get('synthetic'):
        blocks.append('<p class="notice">Учебный пример · данные и ответы синтетические, решения проекта не принимаются.</p>')
    blocks.append('<header><div class="meta">DECISION VIEW · '+esc(d['questionId'])+'</div><h1>'+esc(d['question'])+'</h1><p class="meta">'+esc(d['subject'])+' · '+esc(d['recipient'])+'</p>')
    if d.get('why'):
        blocks.append('<p>'+esc(d['why'])+'</p>')
    blocks.append('</header><section class="recommendation"><h2>Рекомендация</h2><p>'+esc(d['recommendation'])+'</p></section>')
    blocks.append('<div class="facts">')
    for key, title in [('basis', PRESETS[d['kind']]), ('limits', 'Важные ограничения')]:
        if d.get(key):
            blocks.append('<section class="'+key+'"><h2>'+title+'</h2><ul>'+''.join('<li>'+esc(x)+'</li>' for x in d[key])+'</ul></section>')
    blocks.append('</div>')
    if attention:
        blocks.append('<p class="attention"><strong>Глубина: '+esc(attention['mode'])
                      +'</strong> · '+esc(attention['reason'])
                      +'. Условия, варианты и последствия видны полностью; точные основания доступны в деталях. Режим не задаёт время чтения.</p>')
    if d.get('table'):
        blocks.append(table_html(d['table']))
    for section in d.get('sections', []):
        blocks.append('<section><h2>'+esc(section['title'])+'</h2><p>'+esc(section['text'])+'</p></section>')
    if d.get('details'):
        opened = ' open' if attention and attention['mode'] == 'DEEP' else ''
        blocks.append('<details'+opened+'><summary>Точный предмет и основание</summary><p>'+esc(d['details'])+'</p></details>')
    blocks.append('<p class="waiting"><strong>До ответа: </strong>'+esc(d['waiting'].removeprefix('До ответа '))+'</p>')
    if d.get('materials'):
        blocks.append('<section class="materials" aria-label="Материалы">')
        for m in d['materials']:
            title=m['title']+' · '+m.get('revision','')
            fallback='Если ссылка не открывается, запросите у Developing Engineer файл „'+m['filename']+'“ — '+title+'.'
            if m.get('presentation')=='download':
                size=(' · '+format(m['bytes']/1048576,'.2f').replace('.',',')+' МиБ') if m.get('bytes') is not None else ''
                blocks.append('<details class="download"><summary>'+esc(m['title'])+' · ZIP'+size+'</summary><p>Будет скачан файл <strong>'+esc(m['filename'])+'</strong>'+size+'.</p><a class="download-confirm" href="'+esc(m['path'])+'" download="'+esc(m['filename'])+'">Скачать ZIP</a></details><span class="fallback">'+esc(fallback)+'</span>')
            else:
                blocks.append('<p><a target="_blank" rel="noopener noreferrer" href="'+esc(m['path'])+'">'+esc(m['title'])+'</a> — '+esc(m.get('linkPurpose',''))+'<span class="fallback">'+esc(fallback)+'</span></p>')
            if m.get('role') == 'decision-evidence':
                blocks.append('<p class="evidence-limit">Без доступа к этому материалу его основания нельзя независимо проверить; используйте только указанную редакцию.</p>')
        blocks.append('</section>')
    if options:
        blocks.append('<fieldset><legend>Ваш ответ</legend>')
        for n, o in enumerate(options, 1):
            blocks.append('<label class="choice"><input form="response-form" type="radio" name="choice" value="'+esc(o['id'])+'"><span><strong>'+str(n)+'. '+esc(o['label'])+'</strong><small>'+esc(o['consequence'])+'</small></span></label>')
        blocks.append('</fieldset><button class="clear" id="clear" type="button">Снять выбор</button>')
    parameter_html=''
    if d.get('parameters'):
        parameter_html='<div class="parameters">'+''.join('<label>'+esc(p['label'])+', '+esc(p['unit'])+'<input id="param-'+esc(p['id'])+'" type="number" step="any" min="'+esc(p['min'])+'" value="'+esc(p['value'])+'" required></label>' for p in d['parameters'])+'</div><p class="hint">Изменённые условия сохранятся с ответом. Расчёт для них нужно выполнить до зависимого выбора.</p>'
    replacements={'TITLE':d.get('title',d['question']), 'CSS':(HERE/'style.css').read_text(encoding='utf-8'), 'CONTENT':''.join(blocks), 'PARAMETERS':parameter_html, 'DATA':json_text(d), 'APP':(HERE/'app.js').read_text(encoding='utf-8')}
    replacements['TITLE']=esc(replacements['TITLE'])
    template=(HERE/'page.html.in').read_text(encoding='utf-8')
    return re.sub(r'__(TITLE|CSS|CONTENT|PARAMETERS|DATA|APP)__', lambda m:replacements[m[1]], template)

def build(source, output, source_dir):
    started=time.perf_counter()
    if Path(output).exists():raise FileExistsError(output)
    result=render(source,output,source_dir)
    if result is None:
        return {'decisionView':False,'reason':'No missing human decision'}
    write_new(output,result)
    saved=Path(output).read_bytes()
    return {'path':str(Path(output).resolve()),'bytes':len(saved),'sha256':sha(saved),'buildSeconds':round(time.perf_counter()-started,4)}

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('data',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    print(json.dumps(build(json.loads(a.data.read_text(encoding='utf-8')),a.output,a.data.parent),ensure_ascii=False,indent=2))
