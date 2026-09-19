"""Bounded ER JSON -> readable, offline SVG/HTML. Does not inspect or mutate databases."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import textwrap

esc=lambda s:html.escape(str(s),quote=True)
CARDINALITIES={'1','0..1','1..*','0..*','?'}
KEYS={'PK','FK','UK'}

def validate(model):
    if model.get('schema')!=1 or not model.get('title') or not model.get('revision'):
        raise ValueError('ER requires schema=1, title and revision')
    entities=model.get('entities',[]);relations=model.get('relationships',[])
    if not 1<=len(entities)<=50 or len(relations)>200:raise ValueError('ER supports 1..50 entities and at most 200 relationships')
    ids={}
    for entity in entities:
        ident=entity['id']
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*',ident) or ident in ids:raise ValueError('Invalid or duplicate entity ID')
        fields=entity.get('attributes',[])
        if not fields or len(fields)>100:raise ValueError('Each entity requires 1..100 attributes')
        names=set()
        for field in fields:
            if not field.get('name') or field['name'] in names or not field.get('type'):raise ValueError('Attribute name/type missing or duplicated')
            if not isinstance(field.get('keys',[]),list) or not set(field.get('keys',[]))<=KEYS:raise ValueError('Unknown attribute key')
            names.add(field['name'])
        ids[ident]=names
    for relation in relations:
        for end in ('from','to'):
            if relation.get(end) not in ids:raise ValueError('Relationship refers to an unknown entity')
            if relation.get(end+'Cardinality') not in CARDINALITIES:raise ValueError('Explicit cardinality required at both ends; use ? for unknown')
            if relation.get(end+'Attribute') not in ids[relation[end]]:raise ValueError('Relationship refers to an unknown attribute')
    return entities,relations

def render(model,source_name='',source_sha=''):
    entities,relations=validate(model)
    degree={e['id']:0 for e in entities};used=dict(degree)
    for relation in relations:
        degree[relation['from']]+=1;degree[relation['to']]+=1
    positions={};nodes=[];edges=[];row_y=70
    columns=min(2,len(entities));box_w=350;gap=220;left=100
    for index,entity in enumerate(entities):
        x=left+(index%columns)*(box_w+gap)
        label=entity.get('label',entity['id'])
        title_lines=textwrap.wrap(label,34) or ['']
        header=16+len(title_lines)*20
        rows=[]
        for field in entity['attributes']:
            keys=', '.join(field.get('keys',[]))
            label=field['name']+' : '+field['type']+(' ['+keys+']' if keys else '')
            rows.append(textwrap.wrap(label,43) or [''])
        height=max(header+12+sum(len(r)*18+6 for r in rows),header+28*(degree[entity['id']]+1))
        positions[entity['id']]={'x':x,'y':row_y,'w':box_w,'h':height,'header':header,'entity':entity}
        node=f'<g class="entity" id="entity-{esc(entity["id"])}"><rect x="{x}" y="{row_y}" width="{box_w}" height="{height}" rx="7" fill="white" stroke="#525252"/>'
        node+=f'<path d="M{x},{row_y+header} H{x+box_w}" stroke="#c6c6c6"/>'
        for n,line in enumerate(title_lines):node+=f'<text x="{x+14}" y="{row_y+24+n*20}" font-size="16" font-weight="650">{esc(line)}</text>'
        y=row_y+header+22
        for lines in rows:
            for line in lines:node+=f'<text x="{x+14}" y="{y}" font-size="13">{esc(line)}</text>';y+=18
            y+=6
        nodes.append(node+'</g>')
        if index%columns==columns-1 or index==len(entities)-1:
            row_y=max(p['y']+p['h'] for p in positions.values())+150
    relation_rows=[]
    def port(ident):
        used[ident]+=1;p=positions[ident]
        return p['y']+p['header']+(p['h']-p['header'])*used[ident]/(degree[ident]+1)
    for n,r in enumerate(relations,1):
        a,b=positions[r['from']],positions[r['to']]
        ay=port(r['from']);by=port(r['to'])
        if a['x']<b['x']:
            ax=a['x']+a['w'];bx=b['x'];mid=(ax+bx)/2+(n%3-1)*12
            route=f'M{ax},{ay} H{mid} V{by} H{bx}';label_x=mid+8;label_y=(ay+by)/2-10
            start_x=ax+8;end_x=bx-8;start_anchor='start';end_anchor='end'
        elif a['x']>b['x']:
            ax=a['x'];bx=b['x']+b['w'];mid=(ax+bx)/2+(n%3-1)*12
            route=f'M{ax},{ay} H{mid} V{by} H{bx}';label_x=mid+8;label_y=(ay+by)/2-10
            start_x=ax-8;end_x=bx+8;start_anchor='end';end_anchor='start'
        else:
            ax=bx=a['x'];mid=ax-45-(n%3)*14
            route=f'M{ax},{ay} H{mid} V{by} H{bx}';label_x=mid-8;label_y=(ay+by)/2
            start_x=ax-8;end_x=bx-8;start_anchor=end_anchor='end'
        edges.append(f'<g class="relationship" data-from="{esc(r["from"])}" data-to="{esc(r["to"])}"><path d="{route}" fill="none" stroke="#525252" stroke-width="2"/><text x="{label_x}" y="{label_y}" font-size="13">R{n}</text><text x="{start_x}" y="{ay-7}" text-anchor="{start_anchor}" font-size="13">{esc(r["fromCardinality"])}</text><text x="{end_x}" y="{by-7}" text-anchor="{end_anchor}" font-size="13">{esc(r["toCardinality"])}</text></g>')
        def ref(end):return esc(positions[r[end]]['entity'].get('label',r[end])+'.'+r[end+'Attribute'])
        relation_rows.append('<tr><th>R'+str(n)+'</th><td>'+ref('from')+' ↔ '+ref('to')+'</td><td>На один '+esc(a['entity'].get('label',r['from']))+': '+esc(r['toCardinality'])+' '+esc(b['entity'].get('label',r['to']))+';<br>на один '+esc(b['entity'].get('label',r['to']))+': '+esc(r['fromCardinality'])+' '+esc(a['entity'].get('label',r['from']))+'.</td><td>'+esc(r.get('label',''))+'</td></tr>')
    width=left*2+columns*box_w+(columns-1)*gap;height=max(p['y']+p['h'] for p in positions.values())+60
    svg=f'<svg id="diagram" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="diagram-title diagram-desc"><title id="diagram-title">{esc(model["title"])}</title><desc id="diagram-desc">Сущности, атрибуты и связи. Точные кратности и названия полей продублированы в таблице под схемой.</desc><g font-family="system-ui, sans-serif" fill="#161616">'+''.join(edges+nodes)+'</g></svg>'
    notes=''.join('<li>'+esc(t)+'</li>' for t in model.get('notes',[]))
    return '''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"><title>'''+esc(model['title'])+'''</title><style>
''' + (Path(__file__).parent/'style.css').read_text(encoding='utf-8') + '''
main{max-width:1200px}.controls{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:24px 0}.viewport{overflow:auto;border:1px solid var(--border);max-height:75vh;cursor:grab;touch-action:pan-x pan-y}.viewport.dragging{cursor:grabbing}svg{display:block;max-width:none}svg text{paint-order:stroke;stroke:white;stroke-width:3px;stroke-linejoin:round}.table{overflow:auto}@media print{.controls{display:none}.viewport{overflow:visible;max-height:none}svg{width:100%!important;height:auto!important}}
</style></head><body><main><p class="meta">ER-диаграмма · '''+esc(model['revision'])+'''</p><h1>'''+esc(model['title'])+'''</h1><p>'''+esc(model.get('purpose',''))+'''</p><p class="meta">PK — первичный ключ; FK — внешний ключ; UK — уникальный ключ. 1 — ровно один; 0..1 — необязательная связь; 1..* — один и более; 0..* — ноль и более; ? — не установлено.</p><div class="controls" hidden id="controls"><button id="zoom-out" aria-label="Уменьшить">−</button><output id="zoom-level"></output><button id="zoom-in" aria-label="Увеличить">+</button><button id="fit">Уместить по ширине</button><span class="meta">Перемещение: перетаскивание или прокрутка</span></div><div class="viewport" id="viewport">'''+svg+'''</div><h2>Связи и кратности</h2><div class="table"><table><thead><tr><th>ID</th><th>Связанные поля</th><th>Смысл кратности</th><th>Условие</th></tr></thead><tbody>'''+''.join(relation_rows)+'''</tbody></table></div>'''+('<ul>'+notes+'</ul>' if notes else '')+'''<p class="meta">Схема показывает переданную модель; подключение к БД, проверка SQL и миграции не выполняются. Изменение масштаба не является ответом или изменением модели.</p><p class="meta">Источник: '''+esc(source_name)+''' · SHA-256: '''+esc(source_sha)+'''</p><noscript><p>Схема и таблица доступны без JavaScript; для большой схемы используйте прокрутку.</p></noscript></main><script>
(()=>{const svg=document.getElementById('diagram'),box=document.getElementById('viewport'),out=document.getElementById('zoom-level');const w=svg.viewBox.baseVal.width,h=svg.viewBox.baseVal.height;let scale=1,drag=null;
function zoom(value){scale=Math.min(3,Math.max(.2,value));svg.style.width=w*scale+'px';svg.style.height=h*scale+'px';out.textContent=Math.round(scale*100)+'%';}
document.getElementById('controls').hidden=false;document.getElementById('zoom-in').onclick=()=>zoom(scale*1.25);document.getElementById('zoom-out').onclick=()=>zoom(scale/1.25);document.getElementById('fit').onclick=()=>zoom((box.clientWidth-2)/w);
box.addEventListener('pointerdown',e=>{if(e.pointerType==='touch')return;drag={x:e.clientX,y:e.clientY,left:box.scrollLeft,top:box.scrollTop};box.setPointerCapture(e.pointerId);box.classList.add('dragging');e.preventDefault();});
box.addEventListener('pointermove',e=>{if(drag){box.scrollLeft=drag.left+drag.x-e.clientX;box.scrollTop=drag.top+drag.y-e.clientY;}});function stop(){drag=null;box.classList.remove('dragging');}box.addEventListener('pointerup',stop);box.addEventListener('pointercancel',stop);zoom(Math.min(1,(box.clientWidth-2)/w));})();
</script></body></html>'''

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    raw=a.source.read_bytes();result=render(json.loads(raw),a.source.name,hashlib.sha256(raw).hexdigest())
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('xb') as f:f.write(result.encode('utf-8'))
