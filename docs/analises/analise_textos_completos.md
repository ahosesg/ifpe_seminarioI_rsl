# Análise dos textos completos disponíveis

Data da análise inicial: **27 de setembro de 2026**.  
Atualização da busca PubMed: **5 de outubro de 2026**.

## Escopo da análise

Após a triagem de título e resumo, 54 registros foram encaminhados para
recuperação do texto completo. Entre os arquivos anexados foram identificados:

- 37 textos correspondentes às publicações originalmente selecionadas;
- uma dissertação relacionada ao RSL-003, aceita como relatório alternativo
  completo do estudo;
- 16 registros sem qualquer texto correspondente entre os anexos.

O projeto de dissertação `prism-uploads/0_main-12.pdf` e os documentos metodológicos do PRISMA
não integram esta seleção.

## Resultado da leitura integral

Entre os 37 textos correspondentes às publicações selecionadas:

| Decisão | Quantidade |
|---|---:|
| Incluir | 34 |
| Excluir após leitura integral | 3 |
| Total avaliado | 37 |

A dissertação correspondente ao RSL-003 foi aceita como relatório alternativo.
Assim, foram avaliados 38 documentos no total, dos quais 35 foram incluídos e
três foram excluídos.

## Atualização dos textos provenientes da PubMed

Os seis relatórios adicionais foram recuperados e avaliados integralmente:

| Decisão | Quantidade |
|---|---:|
| Incluir | 5 |
| Excluir após leitura integral | 1 |
| Total avaliado | 6 |

Foram incluídos RSL-126, RSL-129, RSL-136, RSL-144 e RSL-145. O RSL-143 foi
excluído porque o artigo apresenta o QT-50 como sensor óptico de baixo custo,
sem classificá-lo como método ambiental equivalente, de referência ou
*research grade*, conforme exige o protocolo.

## Exclusões após leitura integral

| ID | Motivo |
|---|---|
| RSL-009 | O artigo descreve o desenho, os equipamentos e as hipóteses do Fresno Supersite, mas não apresenta resultados quantitativos da comparação entre métodos. |
| RSL-033 | O documento é um resumo de duas páginas do European Aerosol Conference, com resultados preliminares e documentação insuficiente para a extração. |
| RSL-117 | O estudo caracteriza a qualidade do ar em Suva, mas não apresenta comparação pareada entre o Osiris e o método gravimétrico para PM2,5; a calibração gravimétrica informada refere-se a TSP. |
| RSL-143 | O QT-50 é apresentado como sensor óptico de baixo custo, categoria excluída da análise principal pelo protocolo. |

## Inclusões com restrições de extração

- **RSL-020:** extrair somente a comparação externa entre nefelômetro e
  impactador Harvard PM2,5; desconsiderar resultados internos e pessoais.
- **RSL-021:** extrair somente as medições fixas externas ou da estação central;
  desconsiderar exposição pessoal e medições internas.
- **RSL-089:** o instrumento foi desenvolvido para exposição pessoal, mas o
  ensaio analisado utilizou ar ambiente externo e instrumentos co-localizados,
  incluindo FRM.
- **RSL-111:** utilizar apenas as duas campanhas externas e desconsiderar a
  campanha em ambiente interno.

## Publicações relacionadas

- **RSL-003:** a dissertação de David S. Greene foi aceita como relatório
  alternativo completo. A publicação de congresso e a dissertação deverão
  permanecer vinculadas à mesma família de estudo, usando-se a dissertação para
  a extração dos dados.
- **RSL-086 e RSL-107:** pertencem à mesma família PARIES/Pittsburgh. O RSL-107
  amplia o modelo apresentado no RSL-086 para 97 amostradores em 47 sítios. Os
  dois relatórios não devem ser tratados como estudos independentes.
- **RSL-001 e RSL-113:** possuem os mesmos autores, mas descrevem campanhas
  distintas. O RSL-001 utiliza dados de 2007--2008 em Gdynia; o RSL-113 utiliza
  dados de 2010 em Gdańsk.
- **RSL-144 e RSL-105:** utilizam os mesmos sítios de New York e pertencem ao
  mesmo programa de monitoramento, mas abrangem períodos sucessivos e não
  sobrepostos. Devem permanecer vinculados para controlar dependência de sítio
  e programa.
- **RSL-129 e RSL-145:** pertencem ao programa CRPAQS, mas descrevem campanhas
  distintas. O RSL-129 corresponde a Bakersfield em 1998--1999; o RSL-145
  abrange a Califórnia central em 1999--2001. O RSL-009 é um artigo relacionado
  ao desenho do Fresno Supersite, excluído por não apresentar resultados
  quantitativos elegíveis.

## Publicações originais não recuperadas

Além da publicação original do RSL-003, não foram localizados textos para:

- RSL-005;
- RSL-010;
- RSL-012;
- RSL-022;
- RSL-026;
- RSL-031;
- RSL-039;
- RSL-051;
- RSL-058;
- RSL-059;
- RSL-063;
- RSL-065;
- RSL-084;
- RSL-093;
- RSL-102;
- RSL-109.

Esses registros não devem ser classificados como exclusões por conteúdo. Caso
as tentativas de obtenção sejam encerradas, deverão ser informados como
**relatórios não recuperados**.

## Contagens provisórias para o fluxo da revisão

| Etapa | Quantidade |
|---|---:|
| Registros avaliados por título e resumo | 150 |
| Registros excluídos por título e resumo | 90 |
| Publicações originais procuradas para leitura integral | 60 |
| Publicações originais não recuperadas | 17 |
| Publicações originais avaliadas integralmente | 43 |
| Fonte alternativa aceita e avaliada | 1 |
| Documentos avaliados integralmente | 44 |
| Publicações excluídas após leitura integral | 4 |
| Documentos incluídos após leitura integral | 40 |
| Decisões pendentes | 0 |

As contagens ainda são provisórias. O total de estudos será menor que o total de
publicações porque RSL-086 e RSL-107 representam a mesma família de estudo. Com
as informações atuais, os 40 documentos incluídos representam no máximo 39
estudos, e outras sobreposições deverão ser verificadas durante a extração.

## Arquivos produzidos

- `dados/triagem/triagem_texto_completo.xlsx`: planilha principal da seleção integral;
- `dados/triagem/triagem_texto_completo.csv`: cópia para intercâmbio e preservação dos dados.
- `dados/triagem/triagem_texto_completo_pubmed.csv`: decisões integrais dos seis relatórios
  adicionais da PubMed.