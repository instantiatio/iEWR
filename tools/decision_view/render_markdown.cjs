// Build-time Markdown conversion. The resulting reader has no JavaScript or server dependency.
const fs=require('node:fs'),path=require('node:path');
const {marked}=require('./vendor/marked.cjs');
const input=JSON.parse(fs.readFileSync(0,'utf8'));
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const renderer=new marked.Renderer(),headingCounts=new Map();
renderer.html=({text})=>esc(text);
renderer.heading=function({tokens,depth}){
 const label=this.parser.parseInline(tokens),plain=tokens.map(t=>t.text||'').join('');
 const slug=plain.toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu,'').replace(/\s/g,'-');
 const count=headingCounts.get(slug)||0;headingCounts.set(slug,count+1);
 return `<h${depth} id="${esc(slug+(count?'-'+count:''))}">${label}</h${depth}>`;
};
renderer.link=function({href,tokens}){
 const label=this.parser.parseInline(tokens);
 if(!href||(!/^(https?:|#)/i.test(href)&&/^[a-z][a-z\d+.-]*:/i.test(href))||href.startsWith('//'))return label;
 let destination=href;
 if(!/^(https?:|#)/i.test(href)){
  const index=href.indexOf('#'),file=index<0?href:href.slice(0,index),fragment=index<0?'':href.slice(index);
  destination=path.relative(path.dirname(input.outputPath),path.resolve(path.dirname(input.sourcePath),decodeURIComponent(file))).split(path.sep).map(encodeURIComponent).join('/')+fragment;
 }
 if(/\.zip(?:#.*)?$/i.test(href)){
  const name=path.basename(href.split('#')[0]);
  return `<details class="download"><summary>${label} · ZIP</summary><p>Будет скачан файл ${esc(name)}.</p><a href="${esc(destination)}" download="${esc(name)}">Скачать ZIP</a></details>`;
 }
 const original=/\.md(?:#.*)?$/i.test(href)?' <small>(исходник MD)</small>':'';
 return `<a href="${esc(destination)}"${href.startsWith('#')?'':' target="_blank" rel="noopener noreferrer"'}>${label}${original}</a>`;
};
renderer.image=({text})=>`<span>[Изображение: ${esc(text)}]</span>`;
const body=marked.parse(input.markdown,{renderer,gfm:true});
const sourceLink=path.relative(path.dirname(input.outputPath),input.sourcePath).split(path.sep).map(encodeURIComponent).join('/');
const title=input.title||path.basename(input.sourcePath);
process.stdout.write(`<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"><title>${esc(title)}</title><style>${input.css}\nmain{max-width:1000px}h2{margin:24px 0 10px;font-size:20px}h3{margin-top:20px}table{display:block;overflow-x:auto;margin:15px 0}p,li{overflow-wrap:anywhere}.source-note{padding-bottom:12px;margin-bottom:18px;border-bottom:1px solid #dce3d7}pre{padding:12px;background:#f4f6f1}a small{font-size:11px}.download summary{color:#226446;cursor:pointer}</style></head><body><main><aside class="source-note"><p>Оформленное представление материала · ${esc(input.revision||'')}</p><p class="hint">Источник: <a href="${esc(sourceLink)}" target="_blank" rel="noopener noreferrer">${esc(path.basename(input.sourcePath))} (MD, текст)</a>. Ссылки «исходник MD» ведут к исходным файлам.</p><p class="hint">Если исходник недоступен, запросите у Developing Engineer файл „${esc(path.basename(input.sourcePath))}“ — ${esc(title)}. SHA-256: ${esc(input.sourceSHA256)}.</p></aside><article>${body}</article></main></body></html>`);
