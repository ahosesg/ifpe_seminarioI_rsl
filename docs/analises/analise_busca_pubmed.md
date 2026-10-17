# Análise da busca na PubMed

Data da execução: 5 de outubro de 2026.  
Estratégia executada: versão 0.5.  
Arquivo adotado: `prism-uploads/pubmed-Particulat-set(1).nbib`.

## Resultado da exportação

- 64 registros;
- 64 PMIDs únicos;
- 61 registros com DOI;
- todos os registros classificados como artigos de periódico na exportação;
- anos de publicação observados: 1997–2024;
- nenhum filtro de idioma, data ou tipo documental registrado na estratégia.

## Relação entre as duas exportações PubMed

O projeto também contém `prism-uploads/pubmed-Particulat-set.nbib`. Os arquivos não são idênticos em nível de bytes porque apresentam ordem e alguns metadados diferentes, mas contêm exatamente os mesmos 64 PMIDs. Portanto, representam uma única busca e não devem ser somados.

## Deduplicação confirmada contra o conjunto anterior

- 31 registros coincidiram com registros já existentes por DOI;
- dois registros coincidiram por título, autores, ano e periódico: RSL-067/PMID 11686245 e RSL-012/PMID 26314097;
- essas duas coincidências foram confirmadas pelo usuário em 5 de outubro de 2026;
- 31 registros novos foram encaminhados para triagem;
- as duplicatas estão registradas em `dados/buscas/deduplicacao_pubmed.csv`;
- os registros novos estão em `dados/triagem/triagem_pubmed_novos.csv`, identificados provisoriamente como RSL-120 a RSL-150.

## Triagem de título e resumo

A triagem dos 31 registros novos foi concluída pelo usuário em 5 de outubro de 2026:

- 5 registros classificados como `Incluir`;
- 1 registro classificado como `Avaliar texto completo`;
- 25 registros excluídos por título e resumo;
- 6 registros encaminhados à localização e avaliação do texto completo.

Os registros que avançaram foram RSL-126, RSL-129, RSL-136, RSL-143, RSL-144 e RSL-145. As decisões completas e os motivos de exclusão estão em `dados/triagem/triagem_pubmed_novos.csv`; a fila de textos completos está em `dados/triagem/triagem_texto_completo_pubmed.csv`.

## Avaliação dos textos completos

Os seis textos encaminhados foram recuperados e avaliados em 5 de outubro de
2026:

- cinco estudos foram incluídos: RSL-126, RSL-129, RSL-136, RSL-144 e
  RSL-145;
- um estudo foi excluído: RSL-143, porque o QT-50 é apresentado como sensor
  óptico de baixo custo e não como método ambiental equivalente, de referência
  ou *research grade*;
- nenhum dos seis relatórios adicionais permaneceu como não recuperado.

As decisões e as evidências estão em
`dados/triagem/triagem_texto_completo_pubmed.csv`. Os cinco estudos incluídos
foram acrescentados a `dados/extracao/extracao_dados.csv` e
`dados/avaliacao/avaliacao_metodologica.csv`.

## Consequência para o fluxo PRISMA

Após a avaliação integral, os números provisórios do projeto são:

- registros identificados anteriormente em Scopus e Web of Science: 169;
- registros adicionais identificados na PubMed: 64;
- total bruto identificado em bases: 233;
- duplicatas anteriores: 50;
- duplicatas adicionais confirmadas da PubMed: 33;
- registros únicos após a inclusão da PubMed: 150;
- registros avaliados por título e resumo: 150;
- registros excluídos por título e resumo: 90, sendo 25 da busca adicional;
- relatórios originais procurados para recuperação: 60;
- relatórios originais não recuperados: 17, todos do conjunto anterior;
- relatórios originais avaliados integralmente: 43;
- uma fonte alternativa foi aceita e avaliada para o RSL-003;
- documentos avaliados integralmente, incluindo a fonte alternativa: 44;
- documentos excluídos após leitura integral: 4;
- documentos incluídos após leitura integral: 40;
- estudos independentes: no máximo 39, porque RSL-086 e RSL-107 pertencem à
  mesma família.

As contagens permanecem provisórias até o encerramento das tentativas de
recuperação dos 17 relatórios anteriores e a conclusão das buscas de citações.