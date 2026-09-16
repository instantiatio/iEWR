(()=>{'use strict';
const $=id=>document.getElementById(id), data=JSON.parse($('dv-data').textContent);
const radios=[...document.querySelectorAll('[name=choice]')], parameters=data.parameters||[];
const key='decision-view-one-answer:'+data.documentId+':'+location.href.split('#')[0];
const embedded=JSON.parse($('dv-response').textContent);
let state={choice:null,note:'',parameters:Object.fromEntries(parameters.map(p=>[p.id,String(p.value)]))}, answer=null, savedHTML=null;
const status=t=>$('status').textContent=t;
const valid=s=>s&&typeof s.note==='string'&&(s.choice===null||data.options.some(o=>o.id===s.choice))&&s.parameters&&parameters.every(p=>typeof s.parameters[p.id]==='string');
function store(){try{localStorage.setItem(key,JSON.stringify({documentId:data.documentId,answer,state}));return true;}catch{return false;}}
function showAnswer(){
 radios.forEach(r=>{r.checked=r.value===answer.choice;r.disabled=true;});$('clear')?.setAttribute('hidden','');
 $('response-form').hidden=true;$('answer-record').hidden=false;
 $('chosen-label').textContent=data.options.find(o=>o.id===answer.choice)?.label||'Ответ своими словами';
 $('answer-text').textContent=answer.note;
 $('answer-parameters').textContent=parameters.map(p=>p.label+': '+answer.parameters[p.id]+' '+p.unit).join(' · ');
 $('save').textContent='Скачать тот же ответ';status('Ответ сохранён в этой форме. Для передачи верните файл в задачу.');
}
if(embedded){
 if(!valid(embedded)||embedded.questionId!==data.questionId||embedded.documentId!==data.documentId){$('save').disabled=true;status('Файл ответа повреждён. Обратитесь к Developing Engineer.');return;}
 answer=embedded;
}else{try{const local=JSON.parse(localStorage.getItem(key)||'null');if(local?.documentId===data.documentId){if(valid(local.answer)&&local.answer.questionId===data.questionId&&local.answer.documentId===data.documentId)answer=local.answer;else if(valid(local.state))state=local.state;}}catch{}}
if(answer)showAnswer();else{
 radios.forEach(r=>r.checked=r.value===state.choice);$('note').value=state.note;
 parameters.forEach(p=>$('param-'+p.id).value=state.parameters[p.id]);
 if(state.choice||state.note)status('Черновик восстановлен в этом браузере.');
}
function draft(){if(answer)return;state={choice:radios.find(r=>r.checked)?.value||null,note:$('note').value,parameters:Object.fromEntries(parameters.map(p=>[p.id,$('param-'+p.id).value]))};status(store()?'Черновик сохранён в браузере.':'Черновик только в открытой странице: сохраните ответ перед закрытием.');}
$('response-form').addEventListener('submit',e=>e.preventDefault());
radios.forEach(r=>r.addEventListener('change',draft));$('response-form').addEventListener('input',draft);
$('clear')?.addEventListener('click',()=>{if(!answer){radios.forEach(r=>r.checked=false);draft();}});
const safeJSON=v=>JSON.stringify(v).replaceAll('<','\\u003c').replaceAll('\u2028','\\u2028').replaceAll('\u2029','\\u2029');
$('save').addEventListener('click',()=>{try{
 if(!answer){
  draft();if(!state.choice&&!state.note.trim()){status('Выберите вариант или напишите ответ.');return;}
  if(!$('response-form').reportValidity())return;
  if(parameters.some(p=>state.parameters[p.id]!==String(p.value))&&state.choice&&state.choice!==data.parameterChangeChoice){status('Условия изменены: выберите пересчёт или снимите выбор и опишите свой ответ.');return;}
  answer={schema:1,kind:'answer',questionId:data.questionId,documentId:data.documentId,...state,savedAt:new Date().toISOString()};
  store();showAnswer();
 }
 if(!savedHTML){
  const copy=document.documentElement.cloneNode(true);
  copy.querySelector('#dv-response').textContent=safeJSON(answer);
  copy.querySelectorAll('[name=choice]').forEach(r=>{r.disabled=true;if(r.value===answer.choice)r.setAttribute('checked','');else r.removeAttribute('checked');});
  copy.querySelector('#note').textContent=answer.note;
  parameters.forEach(p=>copy.querySelector('#param-'+p.id).setAttribute('value',answer.parameters[p.id]));
  copy.querySelector('#status').textContent='Сохранённый ответ. Для передачи верните файл в задачу.';
  savedHTML='<!doctype html>\n'+copy.outerHTML;
 }
 const a=document.createElement('a'),url=URL.createObjectURL(new Blob([savedHTML],{type:'text/html;charset=utf-8'}));
 a.href=url;a.download=data.answerFilename;a.click();setTimeout(()=>URL.revokeObjectURL(url),30000);
 status('Файл подготовлен к скачиванию. Если скачивание не началось, нажмите ещё раз.');
}catch{status('Скачать не удалось. Ответ остаётся здесь; повторите скачивание.');}});
})();
