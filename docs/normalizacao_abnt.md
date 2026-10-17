# Apresentação da revisão em LaTeX

Versão de trabalho de 17/10/2026. O texto canônico está em `main.tex` e `texto/`;
`suplemento.tex` reúne a documentação extensa. O PDF é produto de compilação,
não fonte editável independente.

## Normas adotadas e implementação

| Norma | Aplicação |
| --- | --- |
| ABNT NBR 14724:2024 | Papel A4; apresentação em uma face; margens esquerda/superior de 3 cm e direita/inferior de 2 cm; corpo 12; entrelinhas 1,5; seções primárias em nova página; paginação arábica exibida a partir do texto, com pré-textuais contados desde a folha de rosto; identificação de quadros/tabelas acima e fonte abaixo. |
| ABNT NBR 6023:2025 | Referências em ordem alfabética; estilo `biblatex-abnt`; nomes e campos bibliográficos conferidos; destaque tipográfico uniforme; alinhamento à esquerda, espaçamento simples e separação entre entradas; DOI e endereço quando disponíveis. |
| ABNT NBR 10520:2023 | Chamadas em autor-data, caixa normal nos sobrenomes no texto e distinção entre chamadas narrativas e parentéticas; citações ligadas à bibliografia. Não há citações diretas longas no manuscrito. |
| ABNT NBR 6024:2012 | Numeração progressiva sem pontuação separando número e título; hierarquia até cinco níveis configurada, utilizando apenas os necessários; elementos não numerados diferenciados. |
| ABNT NBR 6028:2021 | Resumo informativo e abstract em parágrafo único, entre 150 e 500 palavras; palavras-chave separadas por ponto e vírgula e terminadas por ponto. |
| ABNT NBR 6027:2012 | Sumário automático, com títulos correspondentes ao texto, páginas à direita e hiperlinks; pré-textuais fora do sumário; referências e apêndices incluídos. |

A família Times é implementada por `mathptmx`. A ABNT não determina uma família
tipográfica única; o recuo de 1,25 cm é uma escolha editorial consistente,
não exigência atribuída à norma. Quadros extensos usam fonte menor uniforme.

## Alcance dos elementos institucionais

O documento é uma revisão em elaboração, não uma dissertação defendida. Capa,
folha de rosto, resumo, abstract e sumário foram gerados com os dados conhecidos.
Não foram inventados orientador, banca, data de aprovação, assinaturas ou ficha
catalográfica. A folha de aprovação e os dados de catalogação, quando exigidos
para a modalidade institucional final, dependem desses dados e da tramitação
real. Portanto, a configuração não é uma declaração de atendimento integral
a todos os elementos administrativos de uma dissertação final aprovada.

O status de conferência autoral e o uso de IA estão descritos nos métodos e no
registro de trabalho. A revisão editorial não converte decisões assistidas por
IA em decisões humanas confirmadas.

## Bibliografia

`mpga_rsl.bib` é a exportação original e permanece inalterado. O manuscrito e o
suplemento usam `referencias_revisao.bib`, com 66 relatos selecionados e duas
fontes metodológicas. A bibliografia do manuscrito imprime somente os itens
nele citados. O suplemento cita todos os relatos utilizados.

Correções explícitas: Greene (2005), dissertação correspondente ao registro de
congresso de 2004; Dinoi et al., volume de 2017, online em 2016; Jaques, P. A.,
no RSL-101; Lim, Y. S., no RSL-214. Os nomes da exportação anterior permanecem
disponíveis no campo `Autores exportados` dos dados consolidados.

## Fontes normativas consultadas

- Texto da NBR 14724:2024 disponibilizado pela UFES:
  <https://engenhariaedesenvolvimentosustentavel.ufes.br/sites/engenhariaedesenvolvimentosustentavel.ufes.br/files/field/anexo/abnt_nbr_14724.pdf>.
- NBR 6023:2025 e demais normas disponibilizadas pela biblioteca da Universidade Nilton Lins:
  <https://universidadeniltonlins.com.br/biblioteca/normas-da-abnt/>.
- Orientação da biblioteca do Instituto de Economia da Unicamp sobre NBR 6023:2025:
  <https://www3.eco.unicamp.br/biblioteca/images/arquivos/NBR60232025Referencias.pdf>.
- NBR 10520:2023 disponibilizada pela UFOPA:
  <https://ibef.ufopa.edu.br/media/file/site/ibef/documentos/2023/539ca74865f4abf0dc9c181e1124a284.pdf>.
- NBR 6024:2012 disponibilizada pela Fatec Zona Sul:
  <https://fateczonasul.edu.br/wp-content/uploads/2023/03/NBR-6024.pdf>.
- Orientações sobre NBR 6028:2021 do Sistema de Bibliotecas da UFJ:
  <https://sibi.ufj.edu.br/resumo-resenha-e-recensao-abnt-nbr-60282021/>.
- NBR 6027:2012 disponibilizada pelo IFAL:
  <https://www2.ifal.edu.br/o-ifal/administracao/licitacoes-e-contratos/atas/arquivos/abnt-nbr-6027_2012-norma-sumario.pdf/@@download/file/ABNT-NBR-6027_2012%20-%20norma%20sum%C3%A1rio.pdf>.

O estilo bibliográfico é uma implementação de software, não substitui a norma.
Sua saída deve ser conferida após compilação. A compatibilidade da caixa das
chamadas é ajustada separadamente da caixa alta dos sobrenomes na lista.
