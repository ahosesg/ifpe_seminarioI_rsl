# Análise da busca-piloto — versão 0.3

Data da execução: **26 de setembro de 2026**.

## Arquivos analisados

- Scopus: `prism-uploads/export_06ceccbc-1419-4509-8101-a7880fc7d3b0_2026-09-26T213743.098109787.ris`
- Web of Science: `prism-uploads/savedrecs.ris`

## Contagens

| Indicador | Scopus | Web of Science |
|---|---:|---:|
| Registros recuperados | 105 | 64 |
| Registros com resumo | 104 | 64 |
| Registros com DOI | 85 | 60 |
| Primeiro ano recuperado | 1982 | 1994 |
| Último ano recuperado | 2026 | 2026 |

A reunião das bases produziu 169 registros antes da deduplicação. Foram identificados 50 pares coincidentes por DOI ou título normalizado, resultando em **119 referências únicas**.

### Tipos documentais

- Scopus: 88 artigos, 16 trabalhos de conferência e um registro classificado como `conference review`.
- Web of Science: 64 artigos.

Não será aplicado filtro automático de tipo documental nesta etapa. Resumos de evento e documentos sem método completo serão excluídos durante a seleção.

## Avaliação preliminar da relevância

A inspeção dos títulos, resumos e palavras-chave mostra que a estratégia recuperou aproximadamente **50 a 60 estudos potencialmente compatíveis** com a comparação entre métodos automáticos e gravimétricos de MP₁₀ ou MP₂,₅ em ar ambiente. Essa estimativa não substitui a triagem formal.

Entre os principais grupos de registros claramente fora do escopo estão:

- cerca de 20 estudos de sensores de baixo custo;
- aproximadamente 15 a 20 estudos em ambientes internos, exposição pessoal, fontes de emissão ou contextos ocupacionais;
- estudos de composição química, carbono, elementos-traço ou identificação de fontes sem comparação da concentração em massa;
- estudos exclusivamente laboratoriais ou de câmara;
- trabalhos de modelagem, previsão ou aplicação de índices de qualidade do ar;
- revisões e documentos sem dados primários.

## Evidências de que a estratégia possui boa recuperação

A busca localizou estudos diretamente relacionados a diferentes tecnologias, períodos e referenciais, incluindo:

- avaliação do TEOM em comparação com métodos gravimétricos para MP₁₀ e MP₂,₅;
- comparação de amostrador de baixo volume com monitor por beta-atenuação;
- testes de campo de beta-absorção contra método gravimétrico de referência;
- avaliação de fatores que influenciam medidas gravimétricas e por beta-atenuação;
- comparação entre monitores FEM e amostradores FRM para MP₂,₅;
- avaliação de equipamentos SHARP, TEOM-FDMS e BAM;
- estudos de correção de perdas de componentes voláteis no TEOM.

A Web of Science acrescentou estudos relevantes não recuperados pela Scopus, enquanto a Scopus apresentou maior cobertura total e recuperou trabalhos de conferência e estudos mais antigos. As duas bases, portanto, devem ser mantidas.

## Conclusão da busca-piloto

A string 0.3 apresentou equilíbrio aceitável entre recuperação e ruído para uma revisão sistemática. O volume de 119 referências únicas é administrável, e a presença de dezenas de comparações diretamente pertinentes indica que o tema é viável.

Neste momento, **não se recomenda estreitar a busca** com operadores `NOT`, filtros de idioma, período ou tipo documental. O ganho de precisão poderia excluir estudos relevantes mais antigos ou trabalhos que mencionam sensores de baixo custo apenas como contexto.

## Próxima etapa

1. Importar as duas exportações em uma coleção própria no Zotero ou em ferramenta de triagem, sem alterar `mpga_rsl.bib`.
2. Deduplicar os 50 pares identificados.
3. Realizar a seleção formal das 119 referências únicas por título e resumo.
4. Registrar para cada referência uma decisão: incluir, excluir ou dúvida.
5. Recuperar os textos completos dos registros incluídos ou duvidosos.
6. Registrar um motivo padronizado para cada exclusão após leitura integral.

## Verificação da exportação `Versão1.ris`

O arquivo `prism-uploads/Versão1.ris` contém **140 registros únicos**, sem grupos duplicados por DOI ou título normalizado. Entretanto, ele reúne duas coleções com finalidades diferentes:

- **119 registros** provenientes das buscas na Scopus e na Web of Science;
- **21 referências metodológicas**, que não foram identificadas pelas strings da revisão e não devem entrar na triagem.

As 21 referências metodológicas correspondem a:

- 15 artigos de revisão utilizados como modelos de estrutura;
- declaração e documento de explicação do PRISMA 2020;
- declaração e explicação do PRISMA-P;
- PRISMA-S;
- SWiM.

Para a seleção dos estudos e para o futuro fluxograma PRISMA, o número correto após a deduplicação permanece **119**, e não 140. A exportação destinada à triagem deverá conter somente esses 119 registros. As referências metodológicas deverão permanecer em uma coleção separada no Zotero.

## Validação da exportação limpa `Versão1_2.ris`

O arquivo `prism-uploads/Versão1_2.ris` foi validado como conjunto oficial para a triagem por título e resumo:

- 119 registros;
- 119 referências únicas;
- nenhuma duplicata por DOI ou título normalizado;
- nenhuma das 21 referências metodológicas;
- 104 artigos e 15 trabalhos de conferência;
- 118 registros com resumo;
- 97 registros com DOI.

Essa exportação substitui `Versão1.ris` para todas as etapas de seleção. O número inicial da triagem após remoção de duplicatas será, portanto, **119**.

## Planilha de triagem

A exportação limpa foi convertida nos arquivos
`dados/triagem/triagem_titulo_resumo.xlsx` e
`dados/triagem/triagem_titulo_resumo.csv`. A planilha principal contém os 119 registros e oferece
campos padronizados para decisão, motivo de exclusão e observações. O arquivo CSV é
uma cópia de segurança para intercâmbio, mas a triagem deverá ser realizada
preferencialmente no arquivo XLSX.