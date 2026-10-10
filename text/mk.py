import json,sys,subprocess
d=json.load(open('/tmp/claude-0/tx/raw.json'))
commit=subprocess.run(['git','-C','/home/claude/wicker','rev-parse','--short','HEAD'],capture_output=True,text=True).stdout.strip()
SECT=[('A','The title screen and menu'),('B','How to play'),('C','The top bar, buttons and selection'),
 ('D','Tribes, people, buildings and spells'),('E','The campaign screens'),('F','The twenty levels'),
 ('G','Messages during play'),('H','Building tiles, spell hints and the Tribe panel'),
 ('I','Pause, victory and defeat'),('J','The model workshop')]
def sect_html(l):
  if 241<=l<=280:return 'B'
  if 222<=l<=240:return 'A'
  if 198<=l<=209:return 'J'
  if 285<=l<=305:return 'E'
  if 307<=l<=325:return 'I'
  return 'C'
CTXS={'TRIBES':'D','UT':'D','BT':'D','SP':'D','SPDESC':'D','drawPreview':'A','openMenu':'A','showContinue':'A','buildWorld':'A','loadGame':'A',
 'updHUD':'C','togglePause':'C','fsChange':'C','toggleFull':'C','selSummary':'C','focusShaman':'C',
 'openCampaign':'E','showLevel':'E','DIFFNAME':'E','goalText':'E','arm':'H','renderTribe':'H',
 'endWatch':'I','REJOICE':'I','endGame':'I','frame':'I','SHAPES':'J'}
def sect_js(e):
  c,l=e['ctx'],e['line']
  if c.startswith('Level'):return 'F'
  if c.startswith('ws'):return 'J'
  if c in CTXS:return CTXS[c]
  if c=='const':
    if l<=2187 or 2236<=l<=2250:return 'H'
    if 2251<=l<=2262 or 2277<=l<=2292:return 'C'
    if 2263<=l<=2268:return 'I'
    if 2344<=l<=2349:return 'E'
    if l>=2449:return 'J'
  return 'G'
HINT={'label':'name','pl':'plural','info':'description','n':'name','intro':'introduction','news':'listed as new','title':'title','err':'when placing a building','name':'name'}
FN={'swampKill':'bog','killUnit':'Cunning Woman falls','destroyBld':'tomb falls','sacrifice':'altar offering','light':'wicker burning','crown':'May Queen crowned',
 'offerQueen':'May Queen offered','desert':'desertion','startRitual':'entombment','entomb':'entombment','unload':'balloon','updUnit':'','updBld':'','tryCast':'casting',
 'castSpell':'casting','aiThink':'rival attack','aiAttack':'rival attack','aiHangRaid':'rival attack','tribeUpkeep':'','breakTribe':'broken tribe','finishTribe':'tribe finished',
 'invokeArma':'All-against-all','startArma':'All-against-all','drawOverlay':'floating label','onTap':'tapping','command':'orders','orderMove':'orders','beginGame':'game start','beginWatch':'watch mode',
 'REJOICE':'Rejoice! line','validSpot':'when placing a building'}
import re
def friendly(t):
  def f(m):
    x=m.group(1)
    if x in ('…',):return '{…}'
    if '?' in x and "'" in x:return '{…}'
    if re.search(r'\.name$',x):return '{tribe}'
    if x.startswith('UT['):return '{unit}'
    if 'label' in x or x=='nm':return '{building}'
    if re.fullmatch(r's\.n|SPK\[k\]\.n',x):return '{spell}'
    if x.startswith('SPDESC'):return '{spell description}'
    if x=='who':return '{who}'
    if x.startswith('wsLabel'):return '{model}'
    if x=='st':return '{…}'
    if x.startswith('DIFFNAME'):return '{difficulty}'
    if x.startswith('SCEN[') and 'title' in x:return '{level title}'
    if 'join' in x:return '{list}'
    if 'message' in x:return '{error}'
    return '{number}'
  return re.sub(r'\{([^{}]*)\}',f,t)
entries=[]
for e in d['html']:
  t=e['text']
  entries.append(dict(sec=sect_html(e['line']),text=t,hint=('tooltip' if e['key']=='title' else 'screen-reader label' if e['key']=='aria-label' else ''),src=e,lvl=None))
for e in d['js']:
  if e['text'].strip() in ('use strict',):continue
  s=sect_js(e);lvl=e['ctx'] if s=='F' else None
  h=HINT.get(e['key'],'') if s in 'DF' or e['key']=='err' else FN.get(e['ctx'],'')
  if e['ctx']=='SPDESC':h='spell description'
  if e['ctx']=='SHAPES' and e['key']=='args':h='slider'
  entries.append(dict(sec=s,text=friendly(e['text']),hint=h,src=e,lvl=lvl,key=e['key']))
# order: html entries ordered by line within section come first only for A,B,C,E,I,J in natural order
seen={};outE=[]
for en in entries:
  k=en['text']
  if en['sec']=='F' and en.get('key')=='title':en['n']=1;en['locs']=[en['src']];outE.append(en);continue
  if k in seen:
    seen[k]['n']+=1;seen[k]['locs'].append(en['src']);seen[k].setdefault('secs',[seen[k]['sec']]).append(en['sec'])
    if en['sec']=='F':en['ref']=seen[k];outE.append(en)
    continue
  en['n']=1;en['locs']=[en['src']];seen[k]=en;outE.append(en)
L=[]
L.append('WICKER: ALL THE WRITTEN TEXT IN THE GAME')
L.append('Taken from the published game, version 45 (commit %s).'%commit)
L.append('')
L.append('HOW TO EDIT THIS FILE')
L.append('Each piece of text sits under a line starting ### with a number. Change the text under it as you like, then send the file back. Leave the ### lines exactly as they are, because the number is how each change finds its way back to the right place in the game.')
L.append('Text in {curly brackets} is filled in by the game as it runs: {tribe} is the name of a tribe, {building}, {unit} and {spell} are names of those things, {number} is a number, and {…} is a word or phrase the game picks, usually one of the entries listed just after it. Move it around within the sentence if you like, but keep the brackets and what is inside them. Where you see (s), the game adds an s when the number is more than one.')
L.append('If you want to leave a note for me rather than change the wording, put it on its own line starting with //.')
L.append('Text that the game uses in several places is listed once, with a note saying how many places; your change will apply everywhere it appears unless you add a // note saying otherwise (\"Box\", for instance, is both the selection button and a workshop shape). A few very short scraps (single lowercase words glued into longer messages) may not appear here; if you spot wording in the game that is missing from this file, just quote it in a note.')
L.append('Some messages are built from pieces, so a piece that starts with " · " or a comma is the tail of a longer line. These are marked "continues a line".')
L.append('')
idn=0;ids={}
for code,title in SECT:
  es=[e for e in outE if e['sec']==code]
  if not es:continue
  L.append('='*72);L.append(code+'. '+title.upper());L.append('='*72);L.append('')
  lastlvl=None
  for e in es:
    if code=='F' and e['lvl']!=lastlvl:
      lastlvl=e['lvl'];L.append('--- '+lastlvl+' ---');L.append('')
    if e.get('ref'):
      x='%s (see %s)'%(e['text'],e['ref']['tag'])
      if L[-2].startswith('Listed as new in this level: '):L[-2]=L[-2][:-1]+', '+x+'.'
      else:L.append('Listed as new in this level: '+x+'.');L.append('')
      continue
    idn+=1;tag='%04d'%idn;e['tag']=tag;ids[tag]={'text':e['text'],'locs':[{'line':x['line'],'ctx':x['ctx'],'key':x['key'],'spans':x['spans']} for x in e['locs']]}
    notes=[]
    if e['hint']:notes.append(e['hint'])
    if e['n']>1:
      oth=sorted(set(e.get('secs',[]))-{code})
      notes.append('used in %d places'%e['n']+(', also in section '+' and '.join(oth) if oth else ''))
    t=e['text']
    if t[:1] in ',·' or t.startswith(' ·') or t.startswith(' ('):notes.append('continues a line')
    L.append('### '+tag+('   ('+'; '.join(notes)+')' if notes else ''))
    L.append(t.strip() if not t.startswith(' ') else t)
    L.append('')
open('/home/claude/wicker/text/wicker-text.txt','w').write('\n'.join(L))
json.dump({'commit':commit,'entries':ids},open('/home/claude/wicker/text/wicker-text-map.json','w'),indent=0)
print(idn)
