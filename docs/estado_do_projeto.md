# Estado da RSL após a importação

Atualizado em 17 de outubro de 2026, sem alterações científicas ao export.

O projeto Prism foi importado integralmente para
<https://github.com/ahosesg/ifpe_seminarioI_rsl>. O protocolo recebido é a
versão 0.5 de 5 de outubro de 2026. Consulte o
[relatório de importação](importacao_prism/RELATORIO.md) e o
[manifesto dos 117 arquivos](importacao_prism/manifesto.json).

## Pontos de entrada para continuar

| Trabalho | Arquivo |
| --- | --- |
| Protocolo vigente | [`protocolo_rsl.tex`](../protocolo_rsl.tex) |
| Futuro artigo, ainda vazio | [`main.tex`](../main.tex) |
| Biblioteca recebida | [`mpga_rsl.bib`](../mpga_rsl.bib) |
| Estratégia de busca | [`estrategia_busca.md`](metodologia/estrategia_busca.md) |
| Emenda sobre revisor único | [`emenda_protocolo_2026-10-05_revisor_unico.md`](emendas/emenda_protocolo_2026-10-05_revisor_unico.md) |
| Triagem de citações pendente | [`triagem_citacoes.csv`](../dados/triagem/triagem_citacoes.csv) |
| Extração preliminar | [`extracao_dados.csv`](../dados/extracao/extracao_dados.csv) |
| Avaliação preliminar | [`avaliacao_metodologica.csv`](../dados/avaliacao/avaliacao_metodologica.csv) |

Há 40 publicações na extração e na avaliação, e 287 registros novos de citações
aguardando triagem. O artigo ainda não foi redigido no `main.tex`.

Antes de consolidar a avaliação e a síntese, será necessário harmonizar os
documentos sobre o número de revisores e atualizar o registro tabular de
emendas. Essas divergências já estavam no export e foram preservadas.

Os scripts recebidos podem sobrescrever matrizes existentes. Sua execução
exige examinar entradas, saídas e decisões já registradas. A importação não
executou essas rotinas nem verificou a reprodução científica dos resultados.
