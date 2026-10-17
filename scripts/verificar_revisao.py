"""Verificações de integridade da revisão e, opcionalmente, da compilação."""
from pathlib import Path
import json,re,hashlib,sys,collections
R=Path(__file__).resolve().parents[1];S=R/'dados/consolidacao_2026-10-17'
D=json.loads((S/'consolidacao.json').read_text(encoding='utf-8'));manifest=json.loads((S/'manifesto.json').read_text(encoding='utf-8'))
assert hashlib.sha256((R/'mpga_rsl.bib').read_bytes()).hexdigest()==manifest['mpga_rsl_bib_sha256'],'Exportação original modificada'
selected={x['ID'] for x in D['selection'] if x['Decisão de trabalho']=='Incluir na síntese'}
assert len(D['selection'])==437 and len(selected)==66
assert len(D['extraction'])==66 and selected=={x['ID'] for x in D['extraction']}
assert len(D['comparison_strata'])==78 and all(x['Relato'] in selected for x in D['comparison_strata'])
assert len(D['appraisal_narrative'])==66 and selected=={x['ID'] for x in D['appraisal_narrative']}
assert len(D['exclusions'])==18
assert sum(D['counts'].values())==437
keys=re.findall(r'@\w+\{([^,]+),',(R/'referencias_revisao.bib').read_text(encoding='utf-8'))
assert len(keys)==len(set(keys))==68
texts=[*R.glob('texto/*.tex'),R/'latex/suplemento_gerado.tex']
cites=set()
for p in texts:
 t=p.read_text(encoding='utf-8');assert '\ufffd' not in t,p
 assert all(ord(c)>=32 or c in '\n\t' for c in t),'Caractere de controle inválido em '+str(p)
 for match in re.finditer(r'\\(?:textcite|parencite|cite|nocite)(?:\[[^\]]*\])*\{([^}]+)\}',t):cites.update(k.strip() for k in match[1].split(','))
assert not cites-set(keys),'Citações sem referência: '+str(cites-set(keys))
for file in ['main.tex','suplemento.tex']:
 t=(R/file).read_text(encoding='utf-8')
 for item in re.findall(r'\\(?:input|usepackage)\{([^}]+)\}',t):
  if '/' in item or item in ['latex/metadados']:
   assert (R/(item+('.sty' if 'abnt-revisao' in item else '.tex'))).exists(),item
wc={}
for name in ['resumo','abstract']:
 t=(R/f'texto/{name}.tex').read_text(encoding='utf-8').split('\\vspace')[0]
 t=re.sub(r'\\MPdez\{\}', 'MP10',t);t=re.sub(r'\\MPdoiscinco\{\}', 'MP2,5',t);t=t.replace('\\noindent','')
 wc[name]=len(t.split());assert 150<=wc[name]<=500,(name,wc[name])
assert 'conferência autoral' in (R/'texto/metodos.tex').read_text(encoding='utf-8')
assert len(re.findall(r'\\chapter\{', '\n'.join((R/f'texto/{n}.tex').read_text(encoding='utf-8') for n in ['introducao','metodos','resultados','discussao','conclusao'])))==5
if '--compiled' in sys.argv:
 for name in ['main','suplemento']:
  assert (R/f'{name}.pdf').stat().st_size>20000,name
  log=(R/f'{name}.log').read_text(encoding='utf-8',errors='replace')
  for pattern in [r'Citation .+ undefined',r'Reference .+ undefined',r'There were undefined references',r'Please \(re\)run Biber',r'Undefined control sequence',r'LaTeX Error']:
   assert not re.search(pattern,log,re.I),(name,pattern)
  bbl=(R/f'{name}.bbl').read_text(encoding='utf-8',errors='replace')
  assert r'\entry{' in bbl,name
 print('Compilação: PDFs presentes; chamadas e referências resolvidas.')
print(json.dumps({'registros':437,'relatos':66,'estratos':78,'referencias':len(keys),'citacoes_resolvidas':len(cites),'palavras':wc,'exportacao_original':'preservada'},ensure_ascii=False))
