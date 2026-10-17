"""Gera somente a apresentação LaTeX dos dados consolidados; não julga elegibilidade."""
from pathlib import Path
import json,re,sys
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'dados/consolidacao_2026-10-17/consolidacao.json').read_text(encoding='utf-8'))
def tex(value):
 table={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}','β':r'\ensuremath{\beta}','α':r'\ensuremath{\alpha}','µ':r'\ensuremath{\mu}','μ':r'\ensuremath{\mu}','²':r'\textsuperscript{2}','³':r'\textsuperscript{3}','°':r'\textdegree{}','®':r'\textregistered{}','±':r'\ensuremath{\pm}','≥':r'\ensuremath{\geq}','≤':r'\ensuremath{\leq}','₁':'1','₀':'0','₂':'2','₅':'5','–':'--','—':'---','−':'-','‑':'-','“':'``','”':"''"}
 return ''.join(table.get(c,c) for c in str(value)).replace('\n',' ')
def begin(title,cols,headers):
 return ['\\begingroup\\singlespacing\\footnotesize',r'\setlength{\tabcolsep}{3pt}',r'\def\LTcaptype{quadro}',r'\begin{longtable}{'+cols+'}',r'\caption{'+title+r'}\\',r'\hline '+' & '.join(r'\textbf{'+h+'}' for h in headers)+r'\\\hline',r'\endfirsthead',r'\multicolumn{'+str(len(headers))+r'}{r}{\footnotesize Continuação}\\',r'\hline '+' & '.join(r'\textbf{'+h+'}' for h in headers)+r'\\\hline',r'\endhead',r'\multicolumn{'+str(len(headers))+r'}{r}{\footnotesize Continua na página seguinte.}\\',r'\endfoot',r'\endlastfoot']
def end():return [r'\end{longtable}',r'\Fonte{Elaboração própria a partir do registro consolidado e dos relatos identificados.}',r'\endgroup','']
out=[r'% Gerado por scripts/gerar_suplemento.py; editar os dados de origem e regenerar.',r'\TituloPostextual{APÊNDICE A -- REGISTRO METODOLÓGICO E FONTES}','',
tex('Data de encerramento documental: 17 de outubro de 2026. Este suplemento integra a versão de trabalho assistida por IA, sem conferência autoral concluída documentada. A apresentação adota o delineamento de revisão sistematizada de ')+r'\textcite{grant2009}'+tex('. Não constitui pré-registro.'),'',
r'\section*{Cobertura executada e emenda 0.7}',
tex('As bases Scopus e Web of Science foram consultadas em 26/09/2026; PubMed em 05/10/2026. Não foram novamente executadas em 17/10/2026. A busca de citações compreendeu RSL-001, RSL-002, RSL-011, RSL-013 e RSL-021 nas direções retrospectiva e prospectiva, e RSL-020 apenas prospectivamente. Produziu 361 ocorrências e 287 registros novos. O plano de rastrear todos os relatos selecionados não foi executado; a delimitação posterior reflete recursos e encerramento operacional, sem prova de saturação.'),'',
tex('A extração é focal e a apreciação técnica é narrativa. Os 78 estratos organizam relato e fração; não enumeram todas as combinações de sítio, período, instrumento e comparador. Não há classificação global homogênea de risco, metanálise ou total definitivo de estudos independentes. A emenda completa e as versões anteriores são preservadas em docs/emendas/ no repositório.'),'',
r'\section*{Reconciliação da seleção}',
tex('437 registros = 315 exclusões por título/resumo + 6 identificações insuficientes + 32 não recuperados + 18 exclusões após relato + 66 relatos selecionados. Dos 116 encaminhados à recuperação, 84 tiveram relato disponível. A rodada recente de 72 solicitações terminou com 39 PDFs, um texto HTML integral e 32 não recuperados. O pacote de 39 PDFs continha 17 cópias idênticas a arquivos já disponíveis e 22 novos documentos.'),'',
r'\section*{Rastreabilidade, dependência e correções}',
tex('O conjunto vincula RSL-086 e RSL-107 à família de pesquisa de Pittsburgh. A dependência potencial entre outros relatos está registrada na matriz. RSL-003 utiliza a dissertação de Greene (2005), sem contar o congresso vinculado como um estudo adicional. RSL-033 contribui qualitativamente; as diferenças de 30–40% ali descritas comparam TEOM e beta, não filtros. RSL-214 pesa o mesmo filtro do protótipo beta. Em RSL-224, 2017 é o ano do volume e 2016 o da disponibilização online. RSL-101 e RSL-214 receberam correções dos nomes de Jaques, P. A., e Lim, Y. S., confirmadas nos PDFs.'),'',
tex('O valor de 47% em RSL-001 pertence à discussão bibliográfica e não foi mantido como resultado próprio; em RSL-129, r não foi apresentado como R². Resultados gravimétricos e ópticos de RSL-089 foram separados. RSL-376 contribui somente com instrumentos convencionais, com exclusão do AirBeam. Não se substituíram os textos ausentes por estimativas retiradas apenas de resumos.'),'',
r'\section*{Estratégias de busca e dados}',
tex('As estratégias executadas são transcritas no Apêndice E. O histórico, as ocorrências e as sementes permanecem no repositório, nas pastas ')+r'\path{docs/metodologia/}'+tex(' e ')+r'\path{dados/buscas/}'+tex('. Os dados vigentes estão em ')+r'\path{dados/consolidacao_2026-10-17/}'+tex('. As bases anteriores foram preservadas como histórico. A exportação ')+r'\path{mpga_rsl.bib}'+tex(' não foi alterada; ')+r'\path{referencias_revisao.bib}'+tex(' registra os relatos utilizados no manuscrito e neste suplemento.'),'',
r'\section*{Indicadores e abreviaturas}',
tex('Razão entre médias, média de razões, inclinação, diferença de concentração, correlação, coeficiente de determinação, incerteza e erro normalizado não são intercambiáveis. A extração não transforma associação em concordância, conforme ')+r'\textcite{bland1986}'+tex('. Denominador não consolidado significa que a extração focal não o estabeleceu; não prova ausência dessa informação no relato.'),'',
tex('TEOM: Tapered Element Oscillating Microbalance; FDMS: Filter Dynamics Measurement System; FRM: Federal Reference Method; FEM: Federal Equivalent Method; BAM: beta attenuation monitor; SHARP: Synchronized Hybrid Ambient Real-time Particulate; SMPS: Scanning Mobility Particle Sizer; APS: Aerodynamic Particle Sizer; CAMM: Continuous Ambient Mass Monitor; RAMS: Real-time Ambient Mass Sampler; pDR: personal DataRAM; MOUDI: Micro-Orifice Uniform Deposit Impactor. Nomes comerciais identificam modelos; as frações e os contrastes elegíveis permanecem especificados em cada registro.'),'',
r'\TituloPostextual{APÊNDICE B -- CARACTERIZAÇÃO E EXTRAÇÃO FOCAL DOS 66 RELATOS}',
tex('Cada linha representa um relato selecionado e apresenta o resultado focal preservado na matriz. As observações não constituem estimativas independentes, classificação uniforme de risco ou extração exaustiva. A citação em cada linha remete ao relato efetivamente utilizado.'),'']
out+=begin('Caracterização e resultados focais dos relatos selecionados',r'|P{0.18\textwidth}|P{0.25\textwidth}|P{0.28\textwidth}|P{\dimexpr0.29\textwidth-8\tabcolsep-5\arrayrulewidth\relax}|',['Relato e contexto','Métodos e pareamento','Resultado focal','Limites e denominador'])
for e in D['extraction']:
 rid=e['ID'];a=r'\textbf{'+rid+r'}\par\textcite{rsl'+rid[4:]+r'}\par '+tex(e['Fração'])+r'\par '+tex(e['País/local'])
 b=tex(e['Método automático'])+r'\par\medskip '+tex('Comparador: '+e['Comparador gravimétrico'])+r'\par\medskip '+tex(e['Agregação temporal'])
 c=tex(e['Métricas/resultados quantitativos'])
 limit=e.get('Restrição da extração','').strip() or e.get('Alerta de elegibilidade','').strip() or 'Interpretação condicionada ao sítio, período e configuração.'
 d=tex(limit)+r'\par\medskip '+tex(e['N pares/observações'])
 out.append(' & '.join([a,b,c,d])+r'\\\hline')
out+=end()
out += [r'\TituloPostextual{APÊNDICE C -- APRECIAÇÃO TÉCNICA NARRATIVA}',tex('A apreciação registra limitações particulares de desenho e interpretação. Não equivale a um instrumento padronizado de risco de viés, e as avaliações categóricas do piloto não foram generalizadas ao conjunto ampliado.'),'']
out+=begin('Apreciação narrativa dos relatos',r'|P{0.12\textwidth}|P{0.28\textwidth}|P{0.28\textwidth}|P{\dimexpr0.32\textwidth-8\tabcolsep-5\arrayrulewidth\relax}|',['ID','Pareamento e referência','Completude e denominador','Interpretação e fabricantes'])
for a in D['appraisal_narrative']:
 out.append(' & '.join([tex(a['ID']),tex(a['Pareamento e referência']),tex(a['Completude e denominador']),tex(a['Interpretação e aplicabilidade'])+r'\par\medskip '+tex(a['Financiamento e fabricantes'])])+r'\\\hline')
out+=end()
out += [r'\TituloPostextual{APÊNDICE D -- EXCLUSÕES E LACUNAS DOCUMENTAIS}',r'\section*{Exclusões após avaliação do relato}','']
out+=begin('Dezoito exclusões após avaliação do relato',r'|P{0.11\textwidth}|P{0.28\textwidth}|P{\dimexpr0.61\textwidth-6\tabcolsep-4\arrayrulewidth\relax}|',['ID','Identificação','Motivo e evidência'])
for e in D['exclusions']:out.append(' & '.join([tex(e['ID']),tex(e['Título']),tex(e['Motivo']+': '+e['Justificativa'])+r'\par\medskip '+tex(e['Localização'])])+r'\\\hline')
out+=end()
out += [r'\section*{Textos não recuperados}',tex('Indisponibilidade é uma lacuna documental e não uma exclusão por conteúdo. Os resumos destes registros não substituíram leitura integral na síntese.'),'']
metas={m['ID']:m for m in D['metadados_minimos']}
out+=begin('Trinta e dois textos não recuperados',r'|P{0.11\textwidth}|P{0.56\textwidth}|P{\dimexpr0.33\textwidth-6\tabcolsep-4\arrayrulewidth\relax}|',['ID','Título','DOI ou fonte'])
for e in D['selection']:
 if not e['Decisão de trabalho'].startswith('Texto não recuperado'):continue
 m=metas[e['ID']];link=(r'\url{https://doi.org/'+m['DOI']+'}') if m['DOI'] else tex(m.get('Periódico/Fonte','Identificação disponível na matriz'))
 out.append(tex(e['ID'])+' & '+tex(m['Título'])+' & '+link+r'\\\hline')
out+=end()
out += [r'\section*{Identificação insuficiente}',tex('Seis registros permaneceram sem identificação bibliográfica suficiente. Seus identificadores importados foram conservados para possível resolução posterior.'),'']
for e in D['selection']:
 if e['Decisão de trabalho'].startswith('Identificação insuficiente'):out.append(r'\noindent '+tex(e['ID']+'; Scopus EID: '+metas[e['ID']].get('Scopus EID',''))+r'\par')
out += [r'\TituloPostextual{APÊNDICE E -- ESTRATÉGIAS DE BUSCA EXECUTADAS}',tex('As transcrições abaixo reproduzem os comandos preservados no histórico das buscas. Scopus e Web of Science: 26/09/2026; PubMed: 05/10/2026. A base é denominada PubMed, sem presumir que todos os registros pertençam à MEDLINE. Estas transcrições não constituem novas execuções.'),'']
for label,name in [('Scopus','scopus'),('Web of Science Core Collection','wos'),('PubMed','pubmed')]:
 out += [r'\section*{'+label+'}',r'\VerbatimInput[breaklines=true,breakanywhere=true,fontsize=\footnotesize]{dados/consolidacao_2026-10-17/busca_'+name+'.txt}','']
content='\n'.join(out).rstrip()+'\n'
target=R/'latex/suplemento_gerado.tex'
if '--check' in sys.argv:
 if not target.exists() or target.read_text(encoding='utf-8')!=content:raise SystemExit('Suplemento desatualizado: executar python scripts/gerar_suplemento.py')
 print('Suplemento consistente com a consolidação versionada.')
else:
 target.write_text(content,encoding='utf-8',newline='\n');print('Gerado',target.relative_to(R))
