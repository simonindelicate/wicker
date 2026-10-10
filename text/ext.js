// Extracts player-facing text from wicker.html into entries {id,ctx,line,text,spans}
const fs=require('fs');
const acorn=require('/opt/node-tools/node_modules/acorn');
const walk=require('/opt/node-tools/node_modules/acorn-walk');
const src=fs.readFileSync(process.argv[2],'utf8');
const sStart=src.indexOf('<script>\n',src.indexOf('three.min.js'))+9, sEnd=src.indexOf('</script>',sStart);
const js=src.slice(sStart,sEnd);
const lineOf=off=>src.slice(0,off).split('\n').length;
const ast=acorn.parse(js,{ecmaVersion:2022,locations:false,ranges:false});
const out=[];
const TEXTKEYS=new Set(['label','pl','n','info','intro','title','news','name','desc','txt','text','msg','tip','sub','line','goalText','hint','cap','h','t','lab','why','note','short','win','lose']);
const BADCALL=/^\$$|console\.|querySelector|getElementById|EventListener|localStorage|getItem|setItem|removeItem|createElement|classList|setAttribute|getAttribute|^sfx$|\.sfx$|^tone|matchMedia|getContext|toDataURL|setProperty|dispatchEvent|postMessage|^Error$|closest|\.dataset/;
const CMP=new Set(['===','!==','==','!=','in','<','>']);
function looksText(t){
  const s=t.replace(/\{[^}]*\}/g,' ').replace(/<[^>]*>/g,' ').trim();
  if(!/[A-Za-z]{2}/.test(s))return false;
  if(/^#|^\.|rgba?\(|hsla?\(|px\b|=>|^[a-z-]+:|;\s*$|\bvar\(|^\d/.test(s))return false;
  if(/^[a-z0-9_\-:.\/ ]+$/.test(s)&&!/[a-z] [a-z]/.test(s))return false; // ids, 'a b' css-ish
  if(/^(bold|normal|italic)\b|\bserif\b|monospace|Georgia/.test(s))return false;
  return /·/.test(t)||/[A-Z]/.test(s)||/[a-z]+ [a-z]+/.test(s)||/[!?.,]/.test(s);
}
// Ancestor-aware walk
const consumed=new Set();
function calleeName(c){return js.slice(c.start,c.end)}
function render(node){ // returns {text,spans} for + chains / templates / literals
  const spans=[];let text='';
  const ph=n=>{let s=js.slice(n.start,n.end).replace(/\s+/g,' ');
    if(/^[\w.+\-\[\]]+(===|>)1\?'':'s'$|^[\w.+\-\[\]]+>1\?'s':''$/.test(s))return '\u0001(s)\u0002';
    if(/===1\?'':'s'$/.test(s))return '\u0001(s)\u0002';
    return '\u0001{'+(s.length<=28?s:'…')+'}\u0002'};
  (function go(n){
    if(n.type==='Literal'&&typeof n.value==='string'){text+=n.value;spans.push([n.start,n.end]);}
    else if(n.type==='TemplateLiteral'){n.quasis.forEach((q,i)=>{text+=q.value.cooked;spans.push([q.start,q.end]);if(n.expressions[i])text+=ph(n.expressions[i])})}
    else if(n.type==='BinaryExpression'&&n.operator==='+'&&hasStr(n)){go(n.left);go(n.right)}
    else text+=ph(n);
  })(node);
  return {text,spans};
}
function hasStr(n){if(!n)return false;if(n.type==='Literal'&&typeof n.value==='string')return true;if(n.type==='TemplateLiteral')return true;if(n.type==='BinaryExpression'&&n.operator==='+')return hasStr(n.left)||hasStr(n.right);return false}
function ctxName(anc){
  const top=anc.find(a=>a.type==='FunctionDeclaration'||a.type==='VariableDeclaration')||anc[1];let name='(top)';
  if(top){if(top.type==='FunctionDeclaration')name=top.id.name;
    else if(top.type==='VariableDeclaration')name=top.declarations.map(d=>d.id.name||'').join(',');
    else if(top.type==='ExpressionStatement'){const s=js.slice(top.start,Math.min(top.end,top.start+60));const m=s.match(/[A-Za-z_$][\w$.]*/);name=m?m[0]:'(expr)'}
    else name=top.type}
  // level in SCEN
  if(name==='SCEN'){const arr=anc.find(a=>a.type==='ArrayExpression');const lvl=anc.find((a,i)=>a.type==='ObjectExpression'&&anc[i-1]===arr);
    if(arr&&lvl){const i=arr.elements.indexOf(lvl);const tp=lvl.properties.find(p=>p.key&&(p.key.name==='title'));name='Level '+(i+1)+(tp?' — '+tp.value.value:'')}}
  // nearest property key
  let key='';for(let i=anc.length-1;i>=0;i--){const a=anc[i];if(a.type==='Property'&&a.key){key=a.key.name||a.key.value;break}}
  return {name,key};
}
walk.fullAncestor(ast,(node,anc)=>{
  const isStr=(node.type==='Literal'&&typeof node.value==='string')||node.type==='TemplateLiteral';
  if(!isStr)return;
  // climb to top of + chain
  let top=node,i=anc.length-2;
  while(i>=0&&anc[i].type==='BinaryExpression'&&anc[i].operator==='+'){top=anc[i];i--}
  // template literal nested inside chain also okay
  if(consumed.has(top.start+':'+top.end))return;consumed.add(top.start+':'+top.end);
  const parent=anc[i];const ancTop=anc.slice(0,i+1);
  // exclusions by context
  if(parent){
    if(parent.type==='Property'&&parent.key===top)return;
    if(parent.type==='MemberExpression'&&parent.property===top)return;
    if(parent.type==='BinaryExpression'&&CMP.has(parent.operator))return;
    if(parent.type==='SwitchCase')return;
    if(parent.type==='CallExpression'||parent.type==='NewExpression'){const cn=calleeName(parent.callee);if(BADCALL.test(cn))return;
      if(/\.(includes|indexOf|startsWith|endsWith|split|replace|join|slice|toFixed|padStart|has|get|set|delete|add)$/.test(cn)&&!/toast|say|msg/i.test(cn))return}
    if(parent.type==='AssignmentExpression'){const l=js.slice(parent.left.start,parent.left.end);if(/\.(style|className|id|type|fillStyle|strokeStyle|font|textAlign|textBaseline|globalCompositeOperation|cursor|display|background|color|src|href|key|dataset|lineCap|lineJoin)\b|style\./.test(l))return}
  }
  const {text:raw,spans}=render(top);
  const {name,key}=ctxName(ancTop.concat([top]));
  const segs=/</.test(raw.replace(/\u0001[^\u0002]*\u0002/g,''))?raw.split(/<(?:[^>\u0001]|\u0001[^\u0002]*\u0002)*>/):[raw];
  for(let seg of segs){const text=seg.replace(/[\u0001\u0002]/g,'').replace(/\s+/g,' ');if(!/[A-Za-z]{2}/.test(text.replace(/\{[^}]*\}/g,'')))continue;
  if(/^[a-z]+[A-Z][A-Za-z0-9]*$|^XYZ$|void main|gl_|^nfA$/.test(text.trim()))continue;
  const forced=TEXTKEYS.has(key)&&/[A-Za-z]{3}/.test(text)&&!/^[a-z]+$/.test(text)||((key==='pl'||key==='label')&&/[a-z]{3}/.test(text));
  if(!forced&&!(/\{/.test(text)&&/[a-z]{3}/.test(text.replace(/\{[^}]*\}/g,'')))&&!(segs.length>1&&/[a-z]{3}/.test(text))&&!looksText(text))continue;
  out.push({ctx:name,key,line:lineOf(sStart+top.start),text:segs.length>1?text.trim():text,spans:spans.map(([a,b])=>[a+sStart,b+sStart])});}
});
// HTML body text
const bStart=src.indexOf('<div id="app">'),bEnd=src.indexOf('<script',bStart);
const body=src.slice(bStart,bEnd);
const re=/>([^<>]+)</g;let m;
const hid=[];
while((m=re.exec(body))){const t=m[1];if(!/[A-Za-z]{2}/.test(t))continue;const off=bStart+m.index+1+(t.length-t.trimStart().length);hid.push({ctx:'HTML',key:'',line:lineOf(off),text:t.trim().replace(/\s+/g,' '),spans:[[off,off+t.trim().length]]})}
const ra=/(title|aria-label|placeholder)="([^"]+)"/g;
while((m=ra.exec(body))){const off=bStart+m.index+m[1].length+2;hid.push({ctx:'HTML',key:m[1],line:lineOf(off),text:m[2],spans:[[off,off+m[2].length]]})}
hid.sort((a,b)=>a.spans[0][0]-b.spans[0][0]);
out.sort((a,b)=>a.spans[0][0]-b.spans[0][0]);
fs.writeFileSync(process.argv[3],JSON.stringify({html:hid,js:out},null,1));
console.log('html',hid.length,'js',out.length);
