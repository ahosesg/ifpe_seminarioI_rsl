"""Gera figuras descritivas do corpus, sem agregar efeitos de comparação."""
from pathlib import Path
import csv,hashlib,json,sys
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'dados/consolidacao_2026-10-17/consolidacao.json').read_text(encoding='utf-8'))
E=D['extraction'];assert len(E)==66
years=[int(e['Ano da publicação']) for e in E];assert min(years)==1991 and max(years)==2025
bins=[(a,a+4) for a in range(1991,2026,5)]
periods=[{'periodo':f'{a}-{b}','relatos':sum(a<=y<=b for y in years)} for a,b in bins]
fractions={'Apenas MP2,5':0,'Apenas MP10':0,'Ambas as frações':0}
for e in E:
 s=e['Fração'].replace(' ','').replace(',','.')
 fine='2.5' in s;coarse='10' in s
 assert fine or coarse,e['ID']
 fractions['Ambas as frações' if fine and coarse else 'Apenas MP2,5' if fine else 'Apenas MP10']+=1
assert list(fractions.values())==[36,18,12] and sum(p['relatos'] for p in periods)==66
derived={'unidade':'relato selecionado; nao estudo independente','n':66,'periodos':periods,'fracoes':fractions,'fluxo':{'bases_brutas':233,'bases_deduplicadas':150,'novos_por_citacoes':287,'integrados':437,'excluidos_titulo_resumo':315,'identificacao_insuficiente':6,'procurados':116,'nao_recuperados':32,'avaliados':84,'excluidos_apos_relato':18,'incluidos':66}}
assert 150+287==437 and 437-315-6==116 and 116-32==84 and 84-18==66
F=R/'figuras';manifest_path=F/'manifesto_figuras.json'
if '--check' in sys.argv:
 m=json.loads(manifest_path.read_text(encoding='utf-8'))
 assert m['dados']==derived,'Figuras desatualizadas em relacao ao corpus'
 for name,digest in m['sha256'].items():assert hashlib.sha256((F/name).read_bytes()).hexdigest()==digest,name
 print('Figuras: contagens e arquivos consistentes com 66 relatos.');raise SystemExit
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import math,subprocess,shutil
F.mkdir(exist_ok=True)
def finish(c,name):
 c.showPage();c.save()
 poppler=shutil.which('pdftoppm')
 if not poppler:
  bundled=Path(sys.executable).parent.parent/'native/poppler/Library/bin/pdftoppm.exe'
  poppler=str(bundled) if bundled.is_file() else None
 if poppler:subprocess.run([str(poppler),'-png','-singlefile','-r','220',str(F/(name+'.pdf')),str(F/name)],check=True,capture_output=True)
c=canvas.Canvas(str(F/'fluxo_selecao.pdf'),pagesize=(16*cm,9*cm),invariant=1,pageCompression=1)
c.setTitle('Fluxo de selecao dos relatos');c.setAuthor('André Henrique Oliveira Santos')
def box(x,y,w,h,text,fill=(.95,.95,.95)):
 c.setLineWidth(.65);c.setStrokeColorRGB(.2,.2,.2);c.setFillColorRGB(*fill)
 c.roundRect((x-w/2)*cm,(y-h/2)*cm,w*cm,h*cm,.1*cm,stroke=1,fill=1)
 c.setFillColorRGB(0,0,0);c.setFont('Times-Roman',10);lines=text.split('\n')
 for i,line in enumerate(lines):c.drawCentredString(x*cm,y*cm+(len(lines)-1)*6-i*12-3,line)
def arrow(a,b):
 x1,y1=[v*cm for v in a];x2,y2=[v*cm for v in b];c.setStrokeColorRGB(.2,.2,.2);c.setFillColorRGB(.2,.2,.2);c.setLineWidth(.65);c.line(x1,y1,x2,y2)
 ang=math.atan2(y2-y1,x2-x1);size=4
 p=c.beginPath();p.moveTo(x2,y2);p.lineTo(x2-size*math.cos(ang-.48),y2-size*math.sin(ang-.48));p.lineTo(x2-size*math.cos(ang+.48),y2-size*math.sin(ang+.48));p.close();c.drawPath(p,stroke=0,fill=1)
box(4.05,8.25,6.7,1.0,'150 registros das bases\napós deduplicação de 233')
box(11.55,8.25,6.7,1.0,'287 registros novos\nna busca de citações')
box(5.15,6.55,7.5,.92,'437 registros integrados')
arrow((4.05,7.73),(5.15,7.05));arrow((11.55,7.73),(7.3,7.05))
box(12.4,5.7,6.2,1.18,'315 exclusões por título/resumo\n6 identificações insuficientes')
box(5.15,4.83,7.5,.92,'116 relatos procurados')
arrow((5.15,6.04),(5.15,5.34));arrow((8.98,6.4),(9.24,5.93))
box(12.4,3.98,6.2,.92,'32 textos não recuperados')
box(5.15,3.10,7.5,.92,'84 relatos disponíveis e avaliados')
arrow((5.15,4.32),(5.15,3.61));arrow((8.98,4.72),(9.24,4.12))
box(12.4,2.25,6.2,.92,'18 exclusões após avaliação')
box(5.15,1.37,7.5,.92,'66 relatos selecionados',(.87,.91,.94))
arrow((5.15,2.59),(5.15,1.88));arrow((8.98,2.98),(9.24,2.39))
finish(c,'fluxo_selecao')
c=canvas.Canvas(str(F/'perfil_corpus.pdf'),pagesize=(16*cm,7.5*cm),invariant=1,pageCompression=1)
c.setTitle('Perfil descritivo de 66 relatos');c.setAuthor('André Henrique Oliveira Santos')
def bars(x,y,w,h,labels,values,max_value,ticks,percent=False):
 c.setStrokeColorRGB(.25,.25,.25);c.setLineWidth(.5);c.line(x*cm,y*cm,(x+w)*cm,y*cm)
 c.setFont('Times-Roman',9)
 for tick in ticks:
  xx=(x+w*tick/max_value)*cm;c.line(xx,y*cm,xx,y*cm-3);c.drawCentredString(xx,y*cm-14,str(tick))
 c.setFont('Times-Roman',10);c.drawCentredString((x+w/2)*cm,.12*cm,'Número de relatos')
 for i,(label,v) in enumerate(zip(labels,values)):
  yy=y+h-(i+.5)*h/len(labels);bh=.48 if len(labels)>3 else .65
  c.setFillColorRGB(.32,.44,.52);c.rect(x*cm,(yy-bh/2)*cm,w*v/max_value*cm,bh*cm,stroke=0,fill=1)
  c.setFillColorRGB(0,0,0);c.setFont('Times-Roman',9);ls=label.split('\n')
  for j,line in enumerate(ls):c.drawRightString((x-.16)*cm,yy*cm+(len(ls)-1)*5-j*10-3,line)
  val=(f'{v} ({100*v/66:.1f}%)'.replace('.',',') if percent else str(v))
  c.drawString((x+w*v/max_value+.13)*cm,yy*cm-3,val)
c.setFont('Times-Roman',10);c.drawString(.35*cm,6.95*cm,'(a) Período de publicação');c.drawString(8.65*cm,6.95*cm,'(b) Fração reportada')
values=[p['relatos'] for p in periods];maximum=(max(values)//5+2)*5
bars(2.0,1.1,5.65,5.25,[p['periodo'] for p in periods],values,maximum,list(range(0,maximum+1,5)))
bars(10.45,1.1,3.75,5.25,['Apenas\nMP2,5','Apenas\nMP10','Ambas as\nfrações'],list(fractions.values()),60,[0,20,40,60],True)
finish(c,'perfil_corpus')
files=['fluxo_selecao.pdf','perfil_corpus.pdf']
files+=[n for n in ['fluxo_selecao.png','perfil_corpus.png'] if (F/n).exists()]
manifest={'dados':derived,'sha256':{n:hashlib.sha256((F/n).read_bytes()).hexdigest() for n in files}}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
with (R/'dados/consolidacao_2026-10-17/perfil_publicacoes.csv').open('w',encoding='utf-8',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['periodo','relatos'],delimiter=';');writer.writeheader();writer.writerows(periods)
print(json.dumps(derived,ensure_ascii=False))
