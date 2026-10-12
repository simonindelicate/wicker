import json,re,subprocess,sys
d=json.load(open('/tmp/claude-0/tx2/raw.json'))
commit=subprocess.run(['git','-C','/home/claude/wicker','rev-parse','--short','HEAD'],capture_output=True,text=True).stdout.strip()
sys.path.insert(0,'/home/claude/wicker/text')
def friendly(t):
  def f(m):
    x=m.group(1)
    if x=='…' or '?' in x:return '{…}'
    if 'where' in x:return '{place}'
    if re.search(r'\.name$',x) or x in('T.name','C2.name','o.name'):return '{tribe}'
    if x.startswith('UT['):return '{unit}'
    if 'label' in x or x=='nm':return '{building}'
    if re.fullmatch(r's\.n|SPK\[k\]\.n|SPK\[armed\]\.n',x):return '{spell}'
    if x.startswith('SPDESC'):return '{spell description}'
    if x=='who':return '{who}'
    if x.startswith('DIFFNAME') or 'diffName' in x:return '{difficulty}'
    if x.startswith('SCEN[') and 'title' in x:return '{level title}'
    if 'message' in x:return '{error}'
    if '?' in x and ("'" in x or '`' in x):return '{…}'
    return '{number}'
  t=re.sub(r'\$\{((?:[^{}]|\{[^{}]*\})*)\}',lambda m:'{'+m.group(1)+'}',t)
  return re.sub(r'\{((?:[^{}]|\{[^{}]*\})*)\}',f,t)
SKIPCTX={'TOKS','wsPanel','SHAPES','FILM_P','tuneBuild','wsStatus','openTokens','useKeepsake','keepsake','updHUD','toggleFull','fsChange','togglePause','DIFFNAME','TRIBES','SP','use','renderTribe','drawOverlay'}
SKIPCTX|={c for c in [e['ctx'] for e in d['js']] if c.startswith('ws')}
def words(t):return len(re.findall(r"[A-Za-z’'\-]+",re.sub(r'\{[^}]*\}','',t)))
def html_sec(l):
  if 213<=l<237:return None          # workshop
  if 258<=l<=299:return 'B'
  if 303<=l<313:return 'H'
  if 313<=l<346 and not (326<=l<338):return None   # tokens sheet, film tuning panel
  if 326<=l<338:return None
  if l>=346:return 'G'
  return 'A'
SECT=[('A','The title screen'),('B','How to play'),('C','The twenty levels'),('D','Spells'),('E','Buildings and people'),('F','Messages during play'),('G','Pause, victory, defeat and rejoicing'),('H','The campaign screens')]
CTXSEC={'SPDESC':'D','BT':'E','UT':'E','REJOICE':'G','endGame':'G','endWatch':'G','openCampaign':'H','goalText':'H','showLevel':'H','drawPreview':'A','showContinue':'A','loadGame':'A','buildWorld':'A'}
DROP={'The numbers are copied. Paste them to Claude.','Test mode: open every level (wins in test mode are not recorded)','Abandon and choose a new world','raiders dragged to the altar',
 'Too close to another building','Too steep to build on','Too close to the waterline','A hedge needs firm, level ground','The ground is too broken to build on. Flatten it first',
 'Now tap where the hedge ends','No hedge could be laid there','(A hedge is at most {number} long.)','The balloon cannot set down there','No dry land close enough to unload',
 'Only balloonists can reach a balloon','Tap a tribe at the top to find it. The speed button goes up to four times.','Continue your game · {number} min, {…}, seed {number}',
 'Your game is restored, {number} minute(s) in.','You cannot build on land you have not explored','Only warriors and archers can stand guard','They cannot stand guard there',
 'Everything is open to you.','The osses will not listen until their captives are home'}
ent=[]
for e in d['html']:
  s=html_sec(e['line'])
  if not s or e['key'] in('title','aria-label','placeholder'):continue
  ent.append((s,e,None))
for e in d['js']:
  c=e['ctx']
  if c in SKIPCTX:continue
  if c.startswith('Level'):s='C'
  else:s=CTXSEC.get(c,'F')
  if c=='const':continue
  ent.append((s,e,c))
seen=set();out={k:[] for k,_ in SECT}
for s,e,c in ent:
  t=friendly(e['text']).strip('\n')
  if not t.strip():continue
  lvl=c if (c and c.startswith('Level')) else None
  keep_any=(c=='REJOICE') or (lvl and e['key'] in('title','intro')) or c=='SPDESC'
  if lvl and e['key'] not in('title','intro'):continue
  if e['key'] in('label','pl','n','name') and not lvl:continue
  if not keep_any and words(t)<5:continue
  if t in seen:continue
  if 'uniform ' in t or 'vec3' in t or t.startswith('Continue your game') or 'lengths of hedge' in t:continue
  if t.strip() in DROP or t.startswith('History is a wheel') and '{number} of 20' in t:continue
  seen.add(t);out[s].append((t,e,lvl))
L=['WICKER: THE WORDS (current game, commit %s)'%commit,'',
 'Edit any text under a ### line and send the file back; leave the ### lines alone. Words in {curly brackets} are filled in by the game ({tribe}, {number} and so on; {…} is a phrase the game picks), so keep them, though you can move them. (s) means the game adds an s for more than one. A line starting // is a note to me. Names, buttons and one-word labels are left out.','']
ids={};n=0
for code,title in SECT:
  es=out[code]
  if not es:continue
  L+=['='*60,code+'. '+title.upper(),'='*60,'']
  last=None
  for t,e,lvl in es:
    if lvl and lvl!=last:last=lvl;L+=['--- '+lvl+' ---','']
    n+=1;tag='%03d'%n;ids[tag]={'text':e['text'],'shown':t,'ctx':e.get('ctx'),'key':e.get('key'),'line':e['line']}
    L+=['### '+tag,t,'']
open('/home/claude/wicker/text/wicker-words.txt','w').write('\n'.join(L))
json.dump({'commit':commit,'entries':ids},open('/home/claude/wicker/text/wicker-words-map.json','w'),indent=0,ensure_ascii=False)
print(n,{k:len(v) for k,v in out.items()})
