import csv
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]

ARQUIVO_XLSX = ROOT / "prism-uploads/triagem_pubmed_novos_decisoes.xlsx"
ARQUIVO_CSV = ROOT / "dados/triagem/triagem_pubmed_novos.csv"
SAIDA_TEXTO_COMPLETO = ROOT / "dados/triagem/triagem_texto_completo_pubmed.csv"
NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def ler_primeira_planilha(caminho):
    with ZipFile(caminho) as arquivo:
        raiz = ElementTree.fromstring(
            arquivo.read("xl/worksheets/sheet1.xml")
        )

    linhas = []
    for linha in raiz.findall(".//x:sheetData/x:row", NS):
        valores = {}
        for celula in linha.findall("x:c", NS):
            referencia = celula.attrib["r"]
            coluna = re.match(r"[A-Z]+", referencia).group()
            valor = celula.find("x:v", NS)
            valores[coluna] = "" if valor is None else (valor.text or "")
        linhas.append(valores)

    cabecalho = linhas[0]
    colunas = {letra: nome for letra, nome in cabecalho.items()}
    registros = []
    for linha in linhas[1:]:
        registros.append(
            {nome: linha.get(letra, "") for letra, nome in colunas.items()}
        )
    return registros


decisoes = {registro["ID"]: registro for registro in ler_primeira_planilha(ARQUIVO_XLSX)}

with ARQUIVO_CSV.open(encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    campos = leitor.fieldnames
    registros = list(leitor)

for registro in registros:
    decisao = decisoes.get(registro["ID"])
    if decisao:
        registro["Decisão"] = decisao.get("Decisão", "")
        registro["Motivo de exclusão"] = decisao.get("Motivo de exclusão", "")
        observacao = decisao.get("Observações", "").strip()
        if observacao:
            registro["Observações"] = observacao

with ARQUIVO_CSV.open("w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(registros)

campos_texto_completo = [
    "ID",
    "Título",
    "Ano",
    "Decisão título/resumo",
    "Situação do texto",
    "Arquivo analisado",
    "Decisão texto completo",
    "Motivo de exclusão no texto completo",
    "Evidência/observação",
    "Família do estudo/sobreposição",
    "DOI",
    "Autores",
    "Periódico/Fonte",
]

avancam = [
    registro
    for registro in registros
    if registro["Decisão"] in {"Incluir", "Avaliar texto completo"}
]

with SAIDA_TEXTO_COMPLETO.open("w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos_texto_completo)
    escritor.writeheader()
    for registro in avancam:
        escritor.writerow(
            {
                "ID": registro["ID"],
                "Título": registro["Título"],
                "Ano": registro["Ano"],
                "Decisão título/resumo": registro["Decisão"],
                "Situação do texto": "A localizar",
                "Arquivo analisado": "",
                "Decisão texto completo": "",
                "Motivo de exclusão no texto completo": "",
                "Evidência/observação": registro["Observações"],
                "Família do estudo/sobreposição": "",
                "DOI": registro["DOI"],
                "Autores": registro["Autores"],
                "Periódico/Fonte": registro["Periódico/Fonte"],
            }
        )

contagens = {}
for registro in registros:
    decisao = registro["Decisão"] or "Sem decisão"
    contagens[decisao] = contagens.get(decisao, 0) + 1

for decisao, quantidade in sorted(contagens.items()):
    print(f"{decisao}: {quantidade}")
print(f"Encaminhados ao texto completo: {len(avancam)}")