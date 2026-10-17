# Estratégia de busca — revisão de métodos de medição de MP

## Objetivo

Localizar estudos de campo que comparem métodos automáticos ou contínuos com métodos gravimétricos baseados em filtro para a determinação de MP₁₀ e/ou MP₂,₅ no ar ambiente.

Esta é a versão **emendada 0.6**, datada de 5 de outubro de 2026. As buscas da versão 0.3 foram executadas em Scopus e Web of Science em 26 de setembro de 2026, e a busca da versão 0.5 foi executada na PubMed em 5 de outubro de 2026. A ampliação e a posterior delimitação das fontes ocorreram após a triagem, a avaliação de textos completos e a extração preliminar; portanto, essas decisões não serão apresentadas como prospectivas. A versão corrente utiliza Scopus, Web of Science e MEDLINE via PubMed como bases bibliográficas. Não foram utilizados artigos-semente.

## Princípios da busca-piloto

- Bases pesquisadas: Scopus, Web of Science Core Collection e MEDLINE via PubMed.
- Não serão executadas buscas em SciELO, Compendex ou Embase na versão corrente.
- Serão realizadas buscas retrospectivas nas referências e buscas prospectivas de citações dos estudos incluídos.
- Sem restrição inicial de ano, idioma ou tipo de documento.
- Pesquisa em título, resumo e palavras-chave; na Web of Science, o campo `TS` também abrange Keywords Plus.
- Não usar exclusões com `NOT` na busca-piloto.
- Não excluir previamente sensores de baixo custo, ambientes internos ou estudos laboratoriais por termos automáticos; essas exclusões serão feitas na triagem.
- Não incluir PTS/TSP na busca principal.
- Registrar separadamente data, comando, total recuperado e arquivo exportado de cada base.

## Emendas das fontes de informação

A busca em somente Scopus e Web of Science foi inicialmente considerada insuficiente para encerrar a identificação de estudos, pois a revisão combina monitoramento ambiental, engenharia de instrumentação e saúde ambiental. Por isso, as versões 0.4 e 0.5 prepararam a ampliação para PubMed, SciELO, Compendex e Embase.

Na versão 0.6, decidiu-se limitar as bases bibliográficas da revisão a Scopus, Web of Science e MEDLINE via PubMed. As estratégias preparadas para SciELO, Compendex e Embase não foram executadas e foram retiradas do plano corrente. Essa delimitação foi definida em 5 de outubro de 2026, após conhecimento dos resultados iniciais, e será declarada como emenda pós-início.

Para reduzir o risco de perda de estudos, permanecem obrigatórias a busca retrospectiva nas referências e a busca prospectiva de citações de todos os estudos incluídos. Os 64 registros recuperados na PubMed foram deduplicados contra os 119 registros únicos já triados: 33 duplicatas foram confirmadas e 31 registros seguiram para triagem. A triagem excluiu 25 registros e encaminhou seis ao texto completo; todos foram recuperados, cinco foram incluídos e um foi excluído por corresponder a sensor de baixo custo não elegível. As decisões deverão receber segunda avaliação independente. Alterações posteriores receberão nova versão e justificativa.

## Blocos conceituais

### Bloco 1 — material particulado

```text
"particulate matter" OR PM10 OR "PM 10"
OR PM2.5 OR "PM 2.5" OR PM25
```

### Bloco 2 — método gravimétrico

```text
gravimetric OR "filter-based" OR "filter based"
OR "reference method" OR "Federal Reference Method" OR FRM
OR "manual sampler" OR "filter sampler"
OR "high volume sampler" OR "low volume sampler"
```

### Bloco 3 — método automático

```text
"automatic monitor" OR "automatic monitoring"
OR "continuous monitor" OR "continuous monitoring"
OR "real-time monitor" OR BAM OR "beta attenuation monitor"
OR TEOM OR "tapered element oscillating microbalance"
OR FDMS OR "filter dynamics measurement system"
OR SHARP OR nephelometer OR "optical monitor"
```

### Bloco 4 — comparação

```text
compare OR comparison OR agreement OR concordance OR equivalence OR bias
OR validation OR evaluation OR intercomparison OR collocated OR "co-located"
OR "side-by-side" OR performance
```

### Bloco 5 — ambiente externo

```text
"ambient air" OR "air quality"
```

## Scopus

Utilizar a busca avançada. O campo `TITLE-ABS-KEY` pesquisa título, resumo e palavras-chave. A versão 0.3 utiliza termos fechados, sem curingas amplos, para manter equivalência com a consulta da Web of Science.

```text
TITLE-ABS-KEY (
  (
    "particulate matter" OR PM10 OR "PM 10"
    OR PM2.5 OR "PM 2.5" OR PM25
  )
  AND
  (
    gravimetric OR "filter-based" OR "filter based"
    OR "reference method" OR "Federal Reference Method" OR FRM
    OR "manual sampler" OR "filter sampler"
    OR "high volume sampler" OR "low volume sampler"
  )
  AND
  (
    "automatic monitor" OR "automatic monitoring"
    OR "continuous monitor" OR "continuous monitoring"
    OR "real-time monitor"
    OR BAM OR "beta attenuation monitor"
    OR TEOM OR "tapered element oscillating microbalance"
    OR FDMS OR "filter dynamics measurement system"
    OR SHARP OR nephelometer OR "optical monitor"
  )
  AND
  (
    compare OR comparison OR agreement OR concordance OR equivalence OR bias
    OR validation OR evaluation OR intercomparison OR collocated OR "co-located"
    OR "side-by-side" OR performance
  )
  AND
  (
    "ambient air" OR "air quality"
  )
)
```

### Exportação da Scopus

Exportar todos os registros da busca-piloto, quando o limite da base permitir, em RIS ou CSV, incluindo:

- informações bibliográficas;
- título e resumo;
- palavras-chave de autores e indexadas;
- DOI e outros identificadores;
- referências citadas, se disponíveis;
- número de citações;
- informações de financiamento, se disponíveis.

Nome sugerido:

```text
scopus_busca_piloto_v03_AAAAMMDD.ris
```

## Web of Science Core Collection

Utilizar uma única consulta na **Advanced Search / Query Builder**. O campo `TS` pesquisa título, resumo, palavras-chave de autor e Keywords Plus. A consulta utiliza 45 termos fechados e não depende de buscas complementares.

```text
TS=(
  (
    "particulate matter" OR PM10 OR "PM 10"
    OR PM2.5 OR "PM 2.5" OR PM25
  )
  AND
  (
    gravimetric OR "filter-based" OR "filter based"
    OR "reference method" OR "Federal Reference Method" OR FRM
    OR "manual sampler" OR "filter sampler"
    OR "high volume sampler" OR "low volume sampler"
  )
  AND
  (
    "automatic monitor" OR "automatic monitoring"
    OR "continuous monitor" OR "continuous monitoring"
    OR "real-time monitor"
    OR BAM OR "beta attenuation monitor"
    OR TEOM OR "tapered element oscillating microbalance"
    OR FDMS OR "filter dynamics measurement system"
    OR SHARP OR nephelometer OR "optical monitor"
  )
  AND
  (
    compare OR comparison OR agreement OR concordance OR equivalence OR bias
    OR validation OR evaluation OR intercomparison OR collocated OR "co-located"
    OR "side-by-side" OR performance
  )
  AND
  (
    "ambient air" OR "air quality"
  )
)
```

Se for utilizada a caixa de busca comum em vez do Query Builder, selecionar **Topic** e colar apenas o conteúdo interno, retirando `TS=(` no início e o último parêntese no final.

### Exportação da Web of Science

Exportar os registros em RIS, BibTeX ou arquivo de texto, incluindo **Full Record and Cited References**, quando disponível.

Nome sugerido:

```text
wos_busca_piloto_v03_AAAAMMDD.ris
```

## MEDLINE via PubMed — busca executada

A consulta combina o descritor MeSH de material particulado, os subcabeçalhos de métodos e instrumentação de monitoramento ambiental e termos livres em título/resumo. Não aplicar filtros de idioma, data ou tipo documental.

```text
(
  "Particulate Matter"[Mesh]
  OR "particulate matter"[tiab]
  OR PM10[tiab] OR "PM 10"[tiab]
  OR PM2.5[tiab] OR "PM 2.5"[tiab] OR PM25[tiab]
)
AND
(
  gravimetric*[tiab]
  OR "filter based"[tiab] OR "filter-based"[tiab]
  OR "reference method*"[tiab]
  OR "Federal Reference Method*"[tiab] OR FRM[tiab]
  OR "manual sampler*"[tiab] OR "filter sampler*"[tiab]
  OR "high volume sampler*"[tiab] OR "high-volume sampler*"[tiab]
  OR "low volume sampler*"[tiab] OR "low-volume sampler*"[tiab]
)
AND
(
  "automatic monitor*"[tiab] OR "automatic monitoring"[tiab]
  OR "continuous monitor*"[tiab] OR "continuous monitoring"[tiab]
  OR "real time monitor*"[tiab] OR "real-time monitor*"[tiab]
  OR BAM[tiab] OR "beta attenuation monitor*"[tiab]
  OR TEOM[tiab] OR "tapered element oscillating microbalance"[tiab]
  OR FDMS[tiab] OR "filter dynamics measurement system"[tiab]
  OR SHARP[tiab] OR nephelomet*[tiab]
  OR "optical monitor*"[tiab]
)
AND
(
  compar*[tiab] OR agreement[tiab] OR concordan*[tiab]
  OR equivalen*[tiab] OR bias[tiab] OR biases[tiab]
  OR validat*[tiab] OR evaluat*[tiab] OR intercompar*[tiab]
  OR collocat*[tiab] OR "co-locat*"[tiab]
  OR "side-by-side"[tiab] OR performance[tiab]
)
AND
(
  "Environmental Monitoring/instrumentation"[Mesh]
  OR "Environmental Monitoring/methods"[Mesh]
  OR "ambient air"[tiab] OR "air quality"[tiab] OR outdoor[tiab]
)
```

### Registro da execução

- Data: 5 de outubro de 2026.
- Versão da estratégia executada: 0.5.
- Filtros: nenhum filtro de idioma, data ou tipo documental.
- Total recuperado: 64 registros, com 64 PMIDs únicos.
- Período de publicação observado nos resultados: 1997–2024.
- Registros com DOI: 61.
- Arquivo exportado: `pubmed-Particulat-set(1).nbib`.
- Deduplicação confirmada: 31 registros coincidiram por DOI e dois por título, autores, ano e periódico; estes dois últimos foram confirmados pelo usuário em 5 de outubro de 2026. Permaneceram 31 registros novos para triagem.
- Triagem: 25 exclusões por título/resumo e seis registros encaminhados ao texto completo.
- Texto completo: seis relatórios recuperados; cinco estudos incluídos e um excluído.

Arquivo preservado no projeto:

```text
prism-uploads/pubmed-Particulat-set(1).nbib
```

## Avaliação da busca-piloto sem artigos-semente

Em cada base:

1. registrar o total recuperado;
2. ordenar por relevância e examinar os primeiros 100 registros, ou todos quando o total for inferior a 100;
3. classificar informalmente os registros como provavelmente elegíveis, duvidosos ou claramente irrelevantes;
4. registrar os principais motivos de irrelevância;
5. anotar sinônimos, siglas, nomes de equipamentos e expressões recorrentes ainda ausentes;
6. verificar se aparecem comparações de BAM, TEOM ou FDMS com métodos gravimétricos;
7. comparar os resultados entre as bases e identificar termos que funcionaram de forma diferente;
8. alterar a estratégia somente depois dessa avaliação e salvar uma nova versão.

Essa avaliação serve para calibrar a busca, não constitui ainda a triagem definitiva da revisão.

## Ordem para ajustes

### Se a busca recuperar poucos estudos plausíveis

Testar, uma alteração por vez:

1. retirar o bloco de ambiente externo;
2. acrescentar nomes de equipamentos identificados nos resultados;
3. acrescentar `outdoor` ao bloco de ambiente externo;
4. retirar o bloco de comparação, mantendo os três blocos técnicos;
5. acrescentar novos sinônimos gravimétricos encontrados nos artigos.

### Se a busca recuperar muitos registros irrelevantes

Testar, uma alteração por vez:

1. manter obrigatoriamente o bloco de ambiente externo;
2. retirar os termos isolados `performance`, `evaluation` ou `"optical monitor"`;
3. retirar siglas excessivamente ambíguas, uma por vez;
4. exigir termos comparativos próximos a `method*`, `monitor*` ou `instrument*`;
5. somente depois do piloto considerar filtros por tipo de documento.

Não utilizar `NOT sensor*`, `NOT indoor` ou exclusões semelhantes antes de verificar o efeito nos resultados.

## Controle de versões

| Versão | Data | Alteração | Justificativa |
|---|---|---|---|
| 0.1 | 26/09/2026 | Estratégia inicial para Scopus e Web of Science | Início da busca-piloto sem artigos-semente |
| 0.2 | 26/09/2026 | Web of Science dividida em cinco conjuntos, sem curingas amplos | Evitar expansão excessiva e limite máximo de termos |
| 0.3 | 26/09/2026 | Uma única string equivalente para cada base, com termos fechados | Atender ao limite da Web of Science e manter comparabilidade entre bases |
| 0.4 | 27/09/2026 | Inclusão de PubMed e SciELO; Compendex e Embase condicionadas ao acesso; citação retrospectiva e prospectiva | Ampliar a sensibilidade após reconhecer o caráter interdisciplinar da revisão; decisão tomada após conhecimento dos resultados iniciais |
| 0.5 | 27/09/2026 | Inclusão e congelamento pré-execução das strings de PubMed, SciELO, Compendex e Embase | Corrigir a ausência das estratégias completas das bases adicionadas pela emenda 0.4 |
| 0.6 | 05/10/2026 | Execução da PubMed; retirada de SciELO, Compendex e Embase do plano corrente; manutenção das buscas de citações | Delimitar operacionalmente as fontes bibliográficas, preservando transparência sobre a decisão pós-início e suas possíveis limitações de cobertura |