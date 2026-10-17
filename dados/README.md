# Dados vigentes da revisão sistematizada

O estado consolidado de 17/10/2026 está em [consolidacao_2026-10-17/](consolidacao_2026-10-17/).
Os diretórios anteriores descritos abaixo preservam etapas históricas.

# Dados da revisão

## `controle/`

Registro estruturado das emendas ao protocolo.

## `buscas/`

Execuções das buscas, deduplicação da PubMed e controle das buscas de citações.
`ocorrencias_busca_citacoes.csv` preserva cada ocorrência; não deve ser
substituído pela base deduplicada.

## `triagem/`

Bases de seleção por título/resumo, texto completo e citações. As colunas de
decisão de `triagem_citacoes.csv` permanecem vazias até o início formal dessa
triagem.

## `extracao/`

Matriz de extração preliminar. O arquivo `.xlsx`, quando necessário, é gerado
por `scripts/preparar_extracao.py` no mesmo diretório.

## `avaliacao/`

Matriz de avaliação metodológica. O arquivo `.xlsx`, quando necessário, é
gerado por `scripts/preparar_avaliacao_metodologica.py` no mesmo diretório.

Os CSVs são as versões abertas e auditáveis adotadas como referência.
