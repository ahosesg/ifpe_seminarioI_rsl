# Rotinas da consolidação

`gerar_suplemento.py` gera LaTeX a partir da consolidação versionada;
`verificar_revisao.py` confere integridade, referências e compilação.
Os scripts antigos abaixo pertencem ao fluxo histórico e podem sobrescrever
matrizes anteriores; examinar suas entradas e saídas antes de executá-los.

# Scripts reprodutíveis

- `preparar_pubmed.py`: deduplica a exportação PubMed contra a base inicial.
- `sincronizar_triagem_pubmed.py`: incorpora decisões da planilha de triagem da
  PubMed.
- `preparar_extracao.py`: regenera a matriz de extração em CSV e XLSX.
- `preparar_avaliacao_metodologica.py`: regenera a avaliação metodológica em
  CSV e XLSX.

Os scripts resolvem os caminhos em relação à raiz do projeto. Exemplos:

```bash
python scripts/preparar_extracao.py
python scripts/preparar_avaliacao_metodologica.py
```

As rotinas que sobrescrevem bases devem ser executadas somente após conferir
os arquivos de entrada e manter uma cópia das decisões humanas.
