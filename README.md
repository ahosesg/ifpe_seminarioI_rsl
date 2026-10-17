# Revisão sistemática sobre métodos de medição de material particulado

Projeto da revisão sistemática e análise bibliométrica sobre a comparabilidade
entre métodos automáticos e gravimétricos para MP₁₀ e MP₂,₅ no ar ambiente.

Documento iniciado em 26 de setembro de 2026. Protocolo atualmente na versão
0.5, de 5 de outubro de 2026.

## Estrutura do repositório

```text
.
├── main.tex                 # manuscrito do artigo, ainda em preparação
├── protocolo_rsl.tex        # fonte principal do protocolo
├── protocolo_rsl.pdf        # versão compilada para leitura
├── mpga_rsl.bib             # exportação do Zotero; somente leitura
├── docs/                    # documentação metodológica, emendas e análises
│   ├── emendas/
│   ├── metodologia/
│   └── analises/
├── dados/                   # bases tabulares produzidas pela revisão
│   ├── controle/
│   ├── buscas/
│   ├── triagem/
│   ├── extracao/
│   └── avaliacao/
├── scripts/                 # rotinas reprodutíveis de preparação dos dados
└── prism-uploads/           # fontes brutas e arquivos enviados ao projeto
```

Os arquivos LaTeX e a biblioteca bibliográfica permanecem na raiz para manter
a compilação simples no Prism. Os arquivos de `prism-uploads/` não devem ser
renomeados nem movidos: seus caminhos são usados na rastreabilidade das buscas.

## Pontos de entrada

- `protocolo_rsl.tex`: protocolo metodológico vigente.
- `main.tex`: ponto de entrada do futuro artigo.
- `docs/metodologia/estrategia_busca.md`: estratégias e histórico das buscas.
- `docs/metodologia/instrumento_avaliacao_metodologica.md`: instrumento por
  domínios.
- `docs/emendas/emenda_metodologica_2026-10-05.md`: emenda que fundamenta a
  versão 0.5.
- `dados/buscas/sementes_busca_citacoes.csv`: controle das buscas de citações.
- `dados/buscas/ocorrencias_busca_citacoes.csv`: todas as ocorrências, com a
  proveniência preservada.
- `dados/triagem/triagem_citacoes.csv`: registros novos deduplicados para a
  futura triagem.
- `dados/extracao/extracao_dados.csv`: extração preliminar dos estudos
  incluídos.
- `dados/avaliacao/avaliacao_metodologica.csv`: julgamentos metodológicos
  preliminares.

Mais detalhes estão nos índices de [documentação](docs/README.md),
[dados](dados/README.md), [scripts](scripts/README.md) e
[fontes brutas](prism-uploads/README.md).

## Situação em 5 de outubro de 2026

- buscas bibliográficas principais executadas em Scopus, Web of Science e
  PubMed;
- 40 documentos incluídos após a avaliação integral disponível;
- 17 publicações originais registradas como não recuperadas;
- revisão conduzida por um pesquisador, com segunda conferência interna;
- buscas retrospectiva e prospectiva de citações em andamento;
- seis sementes já possuem ao menos uma direção processada, cinco delas com as
  duas direções concluídas;
- 361 ocorrências de citações registradas;
- 287 registros novos deduplicados aguardando triagem;
- nenhuma decisão de elegibilidade foi preenchida na base de citações.

## Biblioteca bibliográfica

`mpga_rsl.bib` é uma exportação da biblioteca sincronizada no Zotero e deve ser
tratado como somente leitura.

- Não editar, reordenar, deduplicar ou corrigir o arquivo manualmente.
- Não alterar chaves de citação diretamente no `.bib`.
- Corrigir metadados no Zotero e substituir a exportação completa.
- Utilizar nos arquivos LaTeX somente as chaves presentes na exportação atual.

## Fluxo de trabalho

1. Preservar as exportações brutas em `prism-uploads/`.
2. Registrar cada execução em `dados/buscas/registro_buscas.csv`.
3. Deduplicar sem alterar os arquivos brutos.
4. Manter seleção, extração e avaliação em seus respectivos subdiretórios de
   `dados/`.
5. Registrar mudanças metodológicas em `docs/emendas/` e
   `dados/controle/registro_emendas.csv`.
6. Executar os scripts sempre a partir da raiz ou por seu caminho completo; os
   caminhos internos são resolvidos em relação à raiz do projeto.
7. Atualizar a busca antes da submissão e relatar o fluxo conforme PRISMA 2020.

## Regras de reprodutibilidade

- Distinguir estudo, publicação, comparação e estimativa.
- Preservar todas as proveniências quando um registro aparece em várias
  sementes ou direções.
- Manter MP₁₀ e MP₂,₅ separados nas sínteses principais.
- Não forçar meta-análise quando os desenhos, instrumentos ou métricas forem
  incompatíveis.
- Registrar toda alteração feita após o conhecimento dos resultados como
  emenda datada.
- Não considerar ferramentas de IA como autoras ou revisoras independentes.