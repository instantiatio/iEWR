"""Read a returned HTML without executing it; record evidence, never apply a decision."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import tempfile
from urllib.parse import unquote, urlsplit
from build import json_text, sha, write_new

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.parts={};self.capture=None;self.context=[];self.in_context=False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs);ident=attrs.get('id')
        if ident in ('dv-data','dv-response','chosen-label','answer-text','answer-parameters'):
            if ident in self.parts:
                raise ValueError('Duplicate data element')
            self.parts[ident]='';self.capture=(tag,ident)
        if ident=='dv-context':
            if self.context:
                raise ValueError('Duplicate decision context')
            self.in_context=True
        if self.in_context:
            if tag=='details':attrs.pop('open',None)
            if tag=='input':
                attrs.pop('checked',None);attrs.pop('disabled',None)
            if ident=='clear':
                attrs.pop('hidden',None)
            self.context.append(('start',tag,sorted(attrs.items())))

    def handle_endtag(self,tag):
        if self.in_context:
            self.context.append(('end',tag))
            if tag=='article':self.in_context=False
        if self.capture and self.capture[0]==tag:self.capture=None

    def handle_data(self,data):
        if self.capture:self.parts[self.capture[1]]+=data
        if self.in_context:self.context.append(('text',data))

def read(path):
    raw=Path(path).read_bytes()
    if len(raw)>2_000_000:raise ValueError('Unexpectedly large Decision View')
    doc=Document(raw.decode('utf-8'))
    doc.data=json.loads(doc.parts['dv-data']);doc.answer=json.loads(doc.parts['dv-response'])
    return raw,doc

def inspect(answer_path,question_path):
    question_bytes,q=read(question_path);answer_bytes,a=read(answer_path)
    if q.answer is not None:raise ValueError('Expected original question file')
    if q.data!=a.data or not q.context or q.context!=a.context:
        raise ValueError('Question content or revision mismatch; manual review required')
    answer=a.answer
    if not isinstance(answer,dict) or answer.get('schema')!=1 or answer.get('kind')!='answer':
        raise ValueError('No completed answer in this file')
    if answer.get('questionId')!=q.data['questionId'] or answer.get('documentId')!=q.data['documentId']:
        raise ValueError('Answer belongs to a different question')
    options={o['id']:o for o in q.data['options']}
    if answer.get('choice') is not None and answer['choice'] not in options:raise ValueError('Unknown choice')
    if not isinstance(answer.get('note'),str) or (not answer.get('choice') and not answer['note'].strip()):
        raise ValueError('Empty answer')
    expected_params={p['id'] for p in q.data.get('parameters',[])}
    if not isinstance(answer.get('parameters'),dict) or set(answer['parameters'])!=expected_params:
        raise ValueError('Parameters do not match question')
    for p in q.data.get('parameters',[]):
        value=answer['parameters'][p['id']]
        if not isinstance(value,str) or not float(value)>=p['min'] or not float(value)<float('inf'):
            raise ValueError('Invalid parameter')
    if (any(answer['parameters'][p['id']]!=str(p['value']) for p in q.data.get('parameters',[]))
        and answer['choice'] and answer['choice']!=q.data.get('parameterChangeChoice')):
        raise ValueError('Changed parameters contradict selected initial scenario')
    label=options[answer['choice']]['label'] if answer['choice'] else 'Ответ своими словами'
    params=' · '.join(p['label']+': '+answer['parameters'][p['id']]+' '+p['unit'] for p in q.data.get('parameters',[]))
    if a.parts['answer-text']!=answer['note'] or a.parts['chosen-label']!=label or a.parts['answer-parameters']!=params:
        raise ValueError('Visible answer differs from recorded answer')
    material_status=[]
    for m in q.data.get('materials',[]):
        if urlsplit(m['path']).scheme:
            state='not-checked'
        else:
            local=(Path(question_path).parent/unquote(m['path'])).resolve()
            state='missing' if not local.is_file() else ('unchanged' if sha(local.read_bytes())==m['sha256'] else 'changed')
        material_status.append({'filename':m['filename'],'role':m.get('role'),'status':state})
        if m.get('source'):
            original=m['source'];local=(Path(question_path).parent/unquote(original['path'])).resolve()
            state='missing' if not local.is_file() else ('unchanged' if sha(local.read_bytes())==original['sha256'] else 'changed')
            material_status.append({'filename':original['filename'],'role':'source-of-'+m.get('role','material'),'status':state})
    semantic={k:answer[k] for k in ('questionId','documentId','choice','note','parameters')}
    return {'schema':1,'kind':'response-evidence','synthetic':q.data.get('synthetic',False),
            'questionId':q.data['questionId'],'documentId':q.data['documentId'],
            'questionFile':str(Path(question_path).resolve()),'questionSHA256':sha(question_bytes),
            'answerFile':str(Path(answer_path).resolve()),'answerSHA256':sha(answer_bytes),
            'responseFingerprint':sha(json_text(semantic).encode()),'exactAnswer':answer,
            'chosenLabel':label,'materials':material_status,
            'interpretation':None,'actions':[],
            'boundary':'Receipt only. Exact words require contextual reading; no permission or effect is inferred.'}

def receive(answer_path,question_path,record_path,handoff_ref):
    if not handoff_ref.strip():raise ValueError('Explicit handoff reference is required')
    result=inspect(answer_path,question_path)
    record_path=Path(record_path)
    if record_path.exists():
        old=json.loads(record_path.read_text())
        if old.get('manualReview'):
            return {'status':'manual-review','reason':'Manual review is still pending; no automatic replacement or resumption.',
                    'record':str(record_path),'incomingAnswer':result['answerFile'],'actionsApplied':False}
        if old.get('responseFingerprint')==result['responseFingerprint']:
            return {'status':'duplicate','record':str(record_path),'actionsApplied':False}
        old['manualReview']={'reason':'A different answer or question was received.',
                             'incomingAnswer':result['answerFile'],'incomingSHA256':result['answerSHA256'],
                             'handoffReference':handoff_ref}
        # This task record is mutable; original question/answer bytes and exactAnswer remain intact.
        # One operator owns this record. Multi-writer arbitration is deliberately outside this helper.
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=record_path.parent,delete=False) as f:
            json.dump(old,f,ensure_ascii=False,indent=2);f.write('\n');temp=f.name
        os.replace(temp,record_path)
        return {'status':'manual-review','reason':'A different answer or question was received; previous evidence remains unchanged.',
                'record':str(record_path),'incomingAnswer':result['answerFile'],'actionsApplied':False}
    result['handoffReference']=handoff_ref
    result['receivedAt']=datetime.now(timezone.utc).isoformat()
    write_new(record_path,json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return {'status':'recorded','record':str(record_path),'actionsApplied':False,'materials':result['materials']}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('answer',type=Path);p.add_argument('--question',type=Path,required=True)
    p.add_argument('--record',type=Path);p.add_argument('--handoff-ref')
    a=p.parse_args()
    try:
        if a.record:
            if not a.handoff_ref:p.error('--record requires --handoff-ref identifying the user message returning the answer')
            result=receive(a.answer,a.question,a.record,a.handoff_ref)
        else:result=inspect(a.answer,a.question)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,OSError) as e:
        p.exit(2,'Cannot process automatically: '+str(e)+'\n')
