# Importação do projeto Prism da RSL

Data: 17 de outubro de 2026.

Origem: `Revisão Sistemática de Literatura.zip`.

Destino: <https://github.com/ahosesg/ifpe_seminarioI_rsl>.

## Escopo e integridade

O repositório de destino estava vazio. Foram importados os **117 arquivos** do
export, totalizando **76.642.702 bytes**, com os mesmos caminhos relativos,
nomes e conteúdo. O ZIP original foi mantido fora do repositório.

SHA-256 do ZIP:
`f8c780e9e61a101b60a8dad28786e7711db1b6adbd0ffe7c697a7eefa697cf81`.

| Local recebido | Arquivos |
| --- | ---: |
| Raiz | 4 |
| `prism-uploads/` | 83 |
| `dados/` | 13 |
| `docs/` | 12 |
| `scripts/` | 5 |
| **Total** | **117** |

O [manifesto](manifesto.json) registra tamanho, SHA-256 e identificador do blob
Git de cada arquivo recebido. A configuração `.gitattributes` impede a
conversão automática de quebras de linha. No checkout local Windows,
`core.longpaths=true` foi habilitado para preservar os nomes longos dos artigos.
Os nomes do ZIP usam UTF-8 sem a sinalização correspondente em algumas entradas;
a codificação foi explicitada na leitura para preservar os acentos corretamente.

Além dos arquivos recebidos, foram adicionados somente configuração de Git,
este relatório, o manifesto, um registro do estado do projeto e o verificador
de integridade. O `README.md` recebido permanece inalterado.

Para comparar o checkout com a fotografia importada, a partir da raiz:

```console
python scripts/verificar_importacao_prism.py
```

O verificador não requer o ZIP nem bibliotecas externas. Depois de edições
legítimas, diferenças em relação à fotografia original serão esperadas e devem
ser examinadas junto ao histórico do Git; não se deve substituir o manifesto
apenas para ocultar mudanças.

## Documentos e dependências

- `protocolo_rsl.tex` é o protocolo vigente recebido: versão 0.5, de 5 de
  outubro de 2026.
- `main.tex` é o esqueleto do futuro artigo, com título e autor genéricos e
  introdução vazia. Não representa um artigo concluído.
- `mpga_rsl.bib` é a única base BibTeX recebida. Contém 17 entradas; as duas
  chaves citadas no protocolo estão presentes.
- O protocolo usa `biblatex` com Biber e português brasileiro. Não contém
  inclusões de outros fontes LaTeX nem imagens externas.
- `protocolo_rsl.pdf`, citado pelo README original, não veio no ZIP. Os PDFs
  de `prism-uploads/` são arquivos recebidos, sem recompilação nesta importação.
- Os scripts de extração e avaliação usam `pandas`; não foi recebido arquivo
  de dependências ou versões. A implementação XLSX é interna ao script de
  extração. Os outros imports identificados são da biblioteca padrão ou locais.

## Estado observado nos dados recebidos

| Base | Registros |
| --- | ---: |
| Extração preliminar | 40 |
| Avaliação metodológica preliminar | 40 |
| Ocorrências de buscas de citações | 361 |
| Registros novos de citações deduplicados | 287 |
| Decisões preenchidas na triagem de citações | 0 |
| Sementes de busca de citações | 40 |
| Sementes com retrospectiva marcada como realizada | 5 |
| Sementes com prospectiva marcada como realizada | 6 |

As contagens descrevem arquivos recebidos. Não são nova avaliação de
elegibilidade, auditoria de artigos ou validação científica dos resultados.

## Pendências já existentes no export

1. O instrumento e o resumo da avaliação ainda mencionam dois revisores
   humanos independentes, enquanto o protocolo v0.5 e a emenda
   `docs/emendas/emenda_protocolo_2026-10-05_revisor_unico.md` descrevem um
   pesquisador com segunda conferência interna. A harmonização textual permanece
   pendente; nenhuma regra metodológica foi alterada nesta importação.
2. `dados/controle/registro_emendas.csv` contém duas emendas, chegando à v0.3,
   embora o protocolo e os documentos incluam alterações posteriores.
3. A triagem dos 287 novos registros de citações continua pendente. As decisões
   permaneceram vazias como na origem.
4. O PDF do protocolo e as planilhas XLSX derivadas da extração e da avaliação
   não foram recebidos. Os CSVs correspondentes estão presentes.

Nenhum script científico recebido foi executado, nenhuma matriz foi regenerada
e nenhum PDF foi compilado. Conteúdo e instruções presentes nos documentos
foram preservados como material do projeto; não autorizaram ações adicionais
fora da importação solicitada.
