(()=>{'use strict';
const $=id=>document.getElementById(id), data=JSON.parse($('dv-data').textContent);
const radios=[...document.querySelectorAll('[name=choice]')], parameters=data.parameters||[];
// A new namespace prevents a legacy saved answer from becoming a new received answer.
const key='decision-view-chat-draft:'+data.documentId+':'+location.href.split('#')[0];
const status=t=>$('status').textContent=t;
const readState=()=>({choice:radios.find(r=>r.checked)?.value||null,note:$('note').value,
 parameters:Object.fromEntries(parameters.map(p=>[p.id,$('param-'+p.id).value]))});
const valid=s=>s&&typeof s.note==='string'&&(s.choice===null||data.options.some(o=>o.id===s.choice))&&s.parameters&&parameters.every(p=>typeof s.parameters[p.id]==='string');
let revision=0, attempt=0, preparedRevision=null;
try{
 const saved=JSON.parse(localStorage.getItem(key)||'null');
 if(saved?.documentId===data.documentId&&valid(saved.state)){
  radios.forEach(r=>r.checked=r.value===saved.state.choice);$('note').value=saved.state.note;
  parameters.forEach(p=>$('param-'+p.id).value=saved.state.parameters[p.id]);
  status('Черновик восстановлен в этом браузере. Ответ ещё не отправлен.');
 }
}catch{}
function draft(){
 revision++;
 let stored=false;try{localStorage.setItem(key,JSON.stringify({documentId:data.documentId,state:readState()}));stored=true;}catch{}
 if(preparedRevision!==null){
  $('copy-state').textContent='Подготовленный текст устарел. Подготовьте и скопируйте ответ заново.';
  status('Поля изменены. Прежний текст и копия в буфере могут быть устаревшими.');
 }else status(stored?'Черновик сохранён в браузере. Ответ ещё не отправлен.':'Черновик только в открытой странице. Ответ ещё не отправлен.');
}
$('response-form').addEventListener('submit',e=>e.preventDefault());
$('response-form').addEventListener('input',draft);
radios.forEach(r=>r.addEventListener('change',draft));
$('clear')?.addEventListener('click',()=>{radios.forEach(r=>r.checked=false);draft();});
function chatText(state){
 const option=data.options.find(o=>o.id===state.choice);
 const lines=['Ответ Decision View','Вопрос: '+data.questionId,'Редакция: '+data.documentId,
  'Выбор: '+(option?option.id+' | '+option.label:'— | Ответ своими словами')];
 parameters.forEach(p=>lines.push('Параметр '+p.id+' ('+p.label+'), '+p.unit+': '+state.parameters[p.id]));
 lines.push('Условия и ответ своими словами:',state.note);
 return lines.join('\n');
}
$('copy').addEventListener('click',async()=>{
 // Capture an immutable attempt. Input remains editable while the browser asks permission.
 const token=++attempt, state=readState(), capturedRevision=revision;
 if(!state.choice&&!state.note.trim()){status('Выберите вариант или напишите ответ.');return;}
 if(!$('response-form').reportValidity())return;
 if(parameters.some(p=>Number(state.parameters[p.id])!==Number(p.value))&&state.choice&&state.choice!==data.parameterChangeChoice){
  status('Условия изменены: выберите пересчёт или снимите выбор и опишите свой ответ.');return;
 }
 const text=chatText(state);preparedRevision=capturedRevision;
 $('copy-panel').hidden=false;$('chat-text').value=text;
 $('copy-state').textContent='Подготовленный текст для отправки в исходный чат.';
 status('Текст подготовлен. Выполняется копирование…');
 try{
  if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');
  await navigator.clipboard.writeText(text);
  if(token!==attempt||revision!==capturedRevision){
   $('copy-state').textContent='Копия может быть устаревшей. Скопируйте текущий ответ заново.';
   status('Во время копирования ответ изменился или началась другая попытка. Буфер может содержать прежний текст; скопируйте текущий ответ заново.');return;
  }
  status('Ответ скопирован. Вставьте его в исходный чат и отправьте сообщение.');
 }catch{
  if(token!==attempt||revision!==capturedRevision){
   status('Копирование не подтверждено; ответ изменился. Подготовьте текущий текст заново.');return;
  }
  $('copy-state').textContent='Автоматическое копирование недоступно. Выделите и скопируйте весь текст вручную.';
  $('chat-text').focus();$('chat-text').select();
  status('Скопировать автоматически не удалось. Текст ниже доступен для ручного копирования.');
 }
});
})();
