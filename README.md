# Revisão sistematizada sobre métodos de medição de material particulado

Comparabilidade entre métodos automáticos e gravimétricos na medição de MP10 e
MP2,5 no ar ambiente: revisão sistematizada dos vieses e fatores condicionantes.

## Documentos canônicos

- [`main.tex`](main.tex): manuscrito, com fontes modulares em [`texto/`](texto/).
- [`suplemento.tex`](suplemento.tex): material suplementar, gerado a partir dos
  dados consolidados.
- [`latex/abnt-artigo.sty`](latex/abnt-artigo.sty): artigo em duas colunas.
- [`latex/abnt-revisao.sty`](latex/abnt-revisao.sty): suplemento em uma coluna.
- [`referencias_revisao.bib`](referencias_revisao.bib): bibliografia editorial
  dos 66 relatos e de duas fontes metodológicas.
- [`dados/consolidacao_2026-10-17/`](dados/consolidacao_2026-10-17/): seleção de
  437 registros, extração focal de 66 relatos, 78 estratos e apreciação narrativa.
- [`docs/normalizacao_abnt.md`](docs/normalizacao_abnt.md): normas, implementação,
  fontes e limites dos elementos institucionais.
- [`docs/emendas/emenda_encerramento_2026-10-17_0_7.md`](docs/emendas/emenda_encerramento_2026-10-17_0_7.md):
  registro metodológico vigente da consolidação.

O manuscrito e seu suplemento são construídos em LaTeX neste repositório. PDFs
são produtos da compilação, não versões de edição independentes.

PDFs da versão conferida: [manuscrito](main.pdf) e [suplemento](suplemento.pdf).
A origem e as somas de verificação estão em
[registro de compilação](docs/compilacao_2026-10-17.json).

## Situação científica

Artigo ampliado em duas colunas em 17/10/2026. Foram selecionados 66 relatos entre 84 avaliados
com relato disponível. Permaneceram 32 textos não recuperados e seis referências
com identificação insuficiente; 315 registros foram excluídos por título/resumo
e 18 após avaliação do relato.

A revisão é sistematizada, conduzida por um pesquisador com assistência de IA,
sem segundo revisor humano independente. A conferência autoral das decisões e
estimativas não está documentada. A extração é focal e a apreciação é narrativa;
não houve metanálise, avaliação categórica uniforme de todo o conjunto ou
quantificação definitiva dos estudos independentes. As buscas não foram
reexecutadas na data do encerramento documental.

Antes da submissão, conferir e registrar as decisões e os números mobilizados,
ratificar as alterações metodológicas e adequar a apresentação à modalidade
institucional ou ao veículo. Não declarar conferência humana ou aprovação
acadêmica que não tenha ocorrido.

## Compilação e verificações

Requisitos: TeX Live com `latexmk`, pdfLaTeX, Biber, BibLaTeX, `biblatex-abnt`,
fontes Times, idioma português e pacotes indicados no estilo. A compilação
completa exige Biber; executar apenas pdfLaTeX uma vez não resolve as referências.

```sh
python3 scripts/gerar_suplemento.py
python3 scripts/gerar_figuras.py --check
python3 scripts/verificar_revisao.py
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode suplemento.tex
python3 scripts/verificar_revisao.py --compiled
```

O fluxo [`compilar-latex.yml`](.github/workflows/compilar-latex.yml) executa essas
verificações e compila os dois documentos no GitHub Actions. Os PDFs e os
registros ficam no artefato `revisao-sistematizada-pdfs` da execução.

As figuras vetoriais e o perfil descritivo são derivados dos dados consolidados.
Para regenerá-las, usar `python3 scripts/gerar_figuras.py` com ReportLab
instalado e Poppler para as prévias PNG; a opção `--check` exige apenas a biblioteca padrão de Python.
O gerador do suplemento altera somente a apresentação derivada.

A [revisão editorial](docs/revisao_editorial_2026-10-17_duas_colunas.md) documenta
os seis exemplos consultados, as escolhas de estrutura e as métricas rechecadas.

## Histórico e fontes preservadas

`mpga_rsl.bib` é a exportação original do Zotero e permanece somente leitura.
`protocolo_rsl.tex` registra o protocolo histórico 0.5; a versão 0.6 está em
`docs/historico/` e o encerramento 0.7, em `docs/emendas/`. Os 40 registros das
matrizes anteriores não substituem os dados da pasta de consolidação vigente.

As fontes de `prism-uploads/` e as exportações brutas não foram renomeadas ou
alteradas. O histórico das buscas continua em `docs/metodologia/` e
`dados/buscas/`. O relatório da importação original permanece em
`docs/importacao_prism/`.
