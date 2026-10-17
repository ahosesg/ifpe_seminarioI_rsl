import csv
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARQUIVO_PUBMED = ROOT / "prism-uploads/pubmed-Particulat-set(1).nbib"
ARQUIVO_EXISTENTE = ROOT / "dados/triagem/triagem_titulo_resumo.csv"
SAIDA_NOVOS = ROOT / "dados/triagem/triagem_pubmed_novos.csv"
SAIDA_DUPLICATAS = ROOT / "dados/buscas/deduplicacao_pubmed.csv"

CONFIRMACOES_POR_TITULO = {
    ("RSL-067", "11686245"): "Confirmada pelo usuário em 05/10/2026",
    ("RSL-012", "26314097"): "Confirmada pelo usuário em 05/10/2026",
}


def normalizar_titulo(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = texto.encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", texto)


def normalizar_doi(texto):
    texto = (texto or "").strip().lower()
    texto = re.sub(r"^https?://(dx\.)?doi\.org/", "", texto)
    return texto.rstrip("/.,;)")


def primeiro(registro, campo):
    return registro.get(campo, [""])[0]


def extrair_doi(registro):
    for campo in ("LID", "AID"):
        for valor in registro.get(campo, []):
            correspondencia = re.search(r"10\.\d{4,9}/\S+", valor, re.I)
            if correspondencia:
                return normalizar_doi(correspondencia.group(0))
    return ""


def extrair_ano(registro):
    correspondencia = re.search(r"(?:19|20)\d{2}", primeiro(registro, "DP"))
    return correspondencia.group(0) if correspondencia else ""


def ler_nbib(caminho):
    texto = caminho.read_text(encoding="utf-8-sig", errors="replace")
    texto = texto.replace("\r\n", "\n").strip()
    registros = []
    for bloco in re.split(r"\n\s*\n(?=PMID-)", texto):
        registro = {}
        campo_atual = None
        for linha in bloco.splitlines():
            correspondencia = re.match(r"^([A-Z0-9]{2,4})\s*-\s?(.*)$", linha)
            if correspondencia:
                campo_atual = correspondencia.group(1)
                registro.setdefault(campo_atual, []).append(
                    correspondencia.group(2).strip()
                )
            elif campo_atual and linha.startswith("      "):
                registro[campo_atual][-1] += " " + linha.strip()
        registros.append(registro)
    return registros


with ARQUIVO_EXISTENTE.open(encoding="utf-8-sig", newline="") as arquivo:
    registros_existentes = list(csv.DictReader(arquivo))

por_doi = {}
por_titulo = {}
for registro in registros_existentes:
    doi = normalizar_doi(registro.get("DOI"))
    titulo = normalizar_titulo(registro.get("Título"))
    if doi:
        por_doi.setdefault(doi, []).append(registro)
    if titulo:
        por_titulo.setdefault(titulo, []).append(registro)

novos = []
duplicatas = []
for registro in ler_nbib(ARQUIVO_PUBMED):
    doi = extrair_doi(registro)
    titulo = primeiro(registro, "TI")
    titulo_normalizado = normalizar_titulo(titulo)
    coincidencias = por_doi.get(doi, []) if doi else []
    criterio = "DOI" if coincidencias else ""
    if not coincidencias:
        coincidencias = por_titulo.get(titulo_normalizado, [])
        criterio = "Título exato normalizado" if coincidencias else ""

    if coincidencias:
        for coincidencia in coincidencias:
            identificador = coincidencia.get("ID", "")
            pmid = primeiro(registro, "PMID")
            confirmacao = (
                "Não necessária — DOI idêntico"
                if criterio == "DOI"
                else CONFIRMACOES_POR_TITULO.get((identificador, pmid), "")
            )
            duplicatas.append(
                {
                    "PMID": pmid,
                    "Título PubMed": titulo,
                    "DOI": doi,
                    "ID existente": identificador,
                    "Título existente": coincidencia.get("Título", ""),
                    "Critério de correspondência": criterio,
                    "Confirmação manual": confirmacao,
                }
            )
        continue

    novos.append(registro)

campos_triagem = [
    "ID",
    "Título",
    "Resumo",
    "Decisão",
    "Motivo de exclusão",
    "Observações",
    "Ano",
    "Autores",
    "Periódico/Fonte",
    "DOI",
    "Tipo documental",
    "Base de origem",
    "Palavras-chave",
]

with SAIDA_NOVOS.open("w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos_triagem)
    escritor.writeheader()
    for numero, registro in enumerate(novos, start=120):
        escritor.writerow(
            {
                "ID": f"RSL-{numero:03d}",
                "Título": primeiro(registro, "TI"),
                "Resumo": primeiro(registro, "AB"),
                "Decisão": "",
                "Motivo de exclusão": "",
                "Observações": f"PMID: {primeiro(registro, 'PMID')}",
                "Ano": extrair_ano(registro),
                "Autores": "; ".join(registro.get("FAU", [])),
                "Periódico/Fonte": primeiro(registro, "JT"),
                "DOI": extrair_doi(registro),
                "Tipo documental": "Artigo",
                "Base de origem": "PubMed",
                "Palavras-chave": "; ".join(registro.get("MH", [])),
            }
        )

campos_duplicatas = [
    "PMID",
    "Título PubMed",
    "DOI",
    "ID existente",
    "Título existente",
    "Critério de correspondência",
    "Confirmação manual",
]
with SAIDA_DUPLICATAS.open("w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos_duplicatas)
    escritor.writeheader()
    escritor.writerows(duplicatas)

print(f"Registros PubMed: {len(novos) + len(duplicatas)}")
print(f"Duplicatas confirmadas: {len(duplicatas)}")
print(f"Registros novos para triagem: {len(novos)}")