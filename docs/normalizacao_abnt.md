# Apresentação do artigo e do suplemento em LaTeX

O manuscrito canônico está em `main.tex` e `texto/`. Adota o gênero artigo,
em duas colunas, com título, autoria, resumo e abstract em largura integral.
O suplemento mantém uma coluna para permitir a leitura das matrizes extensas.
Os PDFs são produtos de compilação dessas fontes.

## Normas e escolhas editoriais

| Norma | Implementação e alcance |
| --- | --- |
| ABNT NBR 6022:2018 | Estrutura de artigo: elementos iniciais, introdução, métodos, resultados, discussão, conclusão e referências. Corpo 12 e espaçamento simples. Projeto gráfico em duas colunas, com quadros, tabelas e figuras extensos em largura integral. |
| ABNT NBR 14724:2024 | Mantidos papel A4, margens superior/esquerda de 3 cm e inferior/direita de 2 cm e hierarquia tipográfica. Capa, folha de rosto, sumário e início de seções primárias em nova página pertencem ao suplemento de apresentação acadêmica. O artigo não é apresentado como uma dissertação monográfica. |
| ABNT NBR 6023:2025 | Referências alfabéticas com `biblatex-abnt`, sobrenomes em caixa alta na lista, alinhamento à esquerda, espaçamento simples e separação entre entradas. DOI e endereço quando disponíveis. A saída do pacote é conferida após Biber; o software não substitui a norma. |
| ABNT NBR 10520:2023 | Citações autor-data, caixa normal dos sobrenomes nas chamadas e distinção entre citações narrativas e parentéticas. Não há transcrição direta longa no artigo. |
| ABNT NBR 6024:2012 | Numeração progressiva até cinco níveis configurada; apenas seção e subseção são necessárias no corpo atual. Referências sem número. |
| ABNT NBR 6028:2021 | Resumo informativo e abstract em parágrafo único; faixa editorial de 100–250 palavras para o artigo. Palavras-chave separadas por ponto e vírgula e terminadas por ponto. |
| ABNT NBR 6027:2012 | Sumário automático do suplemento. O artigo dispensa sumário, conforme sua estrutura de gênero. |

O estilo do artigo é `latex/abnt-artigo.sty`; o suplemento utiliza
`latex/abnt-revisao.sty`. A fonte Times é implementada por `mathptmx`.
Família tipográfica, recuo de 1 em no artigo e distância de 0,8 cm entre
colunas são escolhas editoriais. Legendas, fontes, notas e células dos
quadros/tabelas usam corpo 10 uniforme no artigo; o texto corrido usa corpo 12.
A paginação do artigo é arábica desde sua primeira página. Os elementos
pré-textuais e a paginação do suplemento são independentes.

As tabelas apresentam resultados quantitativos; os quadros organizam desenhos,
condições e implicações interpretativas. Títulos ficam acima e fontes e notas,
abaixo. As duas figuras são vetoriais e derivadas dos dados consolidados;
as contagens descrevem relatos recuperados, sem representar efeitos agrupados.

## Autoria e identificação

São usados apenas os dados conhecidos do autor e da vinculação ao IFPE.
Não foram inventados contato, orientador, banca, aprovação, assinatura, ficha
catalográfica ou datas de submissão e aceite. A retirada da identificação
administrativa de versão de trabalho não altera o método: o artigo informa
pesquisador único, assistência de IA e ausência de segundo revisor independente.
O histórico técnico continua registrando que a conferência autoral não está
documentada.

## Bibliografia e conferência de resultados

`mpga_rsl.bib` permanece inalterado. A bibliografia editorial contém os 66
relatos selecionados e duas fontes metodológicas. O artigo imprime os itens
nele citados; o suplemento cita os 66 relatos. Os seis exemplos consultados
como modelos de escrita estão documentados em
[revisão editorial](revisao_editorial_2026-10-17_duas_colunas.md), sem serem
confundidos com evidência sobre medição de partículas.

As correções bibliográficas anteriores foram conservadas: Greene (2005),
dissertação; Dinoi et al. (2017), volume publicado após disponibilização online
em 2016; Jaques, P. A., em RSL-101; Lim, Y. S., em RSL-214. A ampliação textual
também esclarece médias geométricas em RSL-089 e média dos desvios relativos
diários em RSL-085; seleção e tamanho do corpus não foram alterados.

## Fontes normativas consultadas

- NBR 6022:2018, disponibilizada pela UFRB:
  <https://www2.ufrb.edu.br/bcet/images/NBR_6022-2018.pdf>.
- NBR 14724:2024, disponibilizada pela UFES:
  <https://engenhariaedesenvolvimentosustentavel.ufes.br/sites/engenhariaedesenvolvimentosustentavel.ufes.br/files/field/anexo/abnt_nbr_14724.pdf>.
- NBR 6023:2025 e demais normas, biblioteca da Universidade Nilton Lins:
  <https://universidadeniltonlins.com.br/biblioteca/normas-da-abnt/>.
- Orientação da Unicamp sobre NBR 6023:2025:
  <https://www3.eco.unicamp.br/biblioteca/images/arquivos/NBR60232025Referencias.pdf>.
- NBR 10520:2023, disponibilizada pela UFOPA:
  <https://ibef.ufopa.edu.br/media/file/site/ibef/documentos/2023/539ca74865f4abf0dc9c181e1124a284.pdf>.
- NBR 6024:2012, disponibilizada pela Fatec Zona Sul:
  <https://fateczonasul.edu.br/wp-content/uploads/2023/03/NBR-6024.pdf>.
- Orientações sobre NBR 6028:2021, Sistema de Bibliotecas da UFJ:
  <https://sibi.ufj.edu.br/resumo-resenha-e-recensao-abnt-nbr-60282021/>.
- NBR 6027:2012, disponibilizada pelo IFAL:
  <https://www2.ifal.edu.br/o-ifal/administracao/licitacoes-e-contratos/atas/arquivos/abnt-nbr-6027_2012-norma-sumario.pdf/@@download/file/ABNT-NBR-6027_2012%20-%20norma%20sum%C3%A1rio.pdf>.
