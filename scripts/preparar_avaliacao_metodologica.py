import csv
from collections import Counter
from pathlib import Path

import pandas as pd

from preparar_extracao import write_xlsx


ROOT = Path(__file__).resolve().parents[1]
EXTRACAO = ROOT / "dados/extracao"
SAIDA = ROOT / "dados/avaliacao"

BAIXO = "Baixo risco"
ALGUMAS = "Algumas preocupações"
ALTO = "Alto risco"
INSUF = "Informação insuficiente"

DOMAINS = [
    ("D1", "Seleção e descrição do local e do período"),
    ("D2", "Colocalização e coincidência temporal"),
    ("D3", "Adequação e rastreabilidade do método gravimétrico"),
    ("D4", "Calibração, manutenção e controle de qualidade do método automático"),
    ("D5", "Completude, exclusões e tratamento dos dados"),
    ("D6", "Cobertura da faixa de concentração e das condições ambientais"),
    ("D7", "Adequação das análises de concordância e comparabilidade"),
    ("D8", "Transparência e completude do relato"),
    ("D9", "Risco de relato seletivo e conflitos de interesse"),
]


# Ordem: D1 a D9. Os julgamentos foram aplicados com as regras congeladas no
# docs/metodologia/instrumento_avaliacao_metodologica.md antes da consolidação
# desta matriz.
RATINGS = {
    "RSL-001": [BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-002": [BAIXO, ALTO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-003": [BAIXO, ALGUMAS, BAIXO, ALGUMAS, ALGUMAS, BAIXO, ALGUMAS, BAIXO, INSUF],
    "RSL-011": [BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-013": [ALGUMAS, BAIXO, ALGUMAS, BAIXO, ALGUMAS, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-020": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-021": [ALGUMAS, BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-024": [BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-027": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, INSUF],
    "RSL-029": [BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-044": [BAIXO, ALTO, BAIXO, ALGUMAS, BAIXO, BAIXO, ALTO, BAIXO, INSUF],
    "RSL-045": [BAIXO, BAIXO, BAIXO, ALGUMAS, INSUF, BAIXO, ALGUMAS, ALGUMAS, INSUF],
    "RSL-049": [BAIXO, BAIXO, BAIXO, ALGUMAS, INSUF, BAIXO, ALGUMAS, ALGUMAS, INSUF],
    "RSL-057": [BAIXO, BAIXO, BAIXO, BAIXO, INSUF, BAIXO, ALGUMAS, BAIXO, ALGUMAS],
    "RSL-061": [BAIXO, ALGUMAS, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-064": [BAIXO, BAIXO, ALGUMAS, BAIXO, INSUF, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-066": [BAIXO, BAIXO, BAIXO, ALGUMAS, INSUF, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-069": [BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, BAIXO, ALGUMAS, BAIXO, INSUF],
    "RSL-073": [ALGUMAS, BAIXO, BAIXO, ALGUMAS, BAIXO, ALGUMAS, BAIXO, BAIXO, INSUF],
    "RSL-076": [BAIXO, BAIXO, ALGUMAS, ALGUMAS, ALGUMAS, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-082": [BAIXO, BAIXO, BAIXO, ALGUMAS, INSUF, ALGUMAS, BAIXO, BAIXO, INSUF],
    "RSL-085": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-086": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, ALGUMAS],
    "RSL-089": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, INSUF],
    "RSL-090": [ALGUMAS, BAIXO, BAIXO, ALGUMAS, INSUF, ALGUMAS, ALGUMAS, BAIXO, INSUF],
    "RSL-091": [BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, ALTO],
    "RSL-095": [BAIXO, BAIXO, BAIXO, ALGUMAS, INSUF, BAIXO, ALGUMAS, BAIXO, INSUF],
    "RSL-101": [BAIXO, BAIXO, BAIXO, ALTO, ALTO, ALGUMAS, BAIXO, BAIXO, ALGUMAS],
    "RSL-103": [BAIXO, BAIXO, ALGUMAS, ALGUMAS, BAIXO, BAIXO, ALGUMAS, BAIXO, INSUF],
    "RSL-105": [BAIXO, BAIXO, BAIXO, BAIXO, ALTO, BAIXO, BAIXO, BAIXO, INSUF],
    "RSL-106": [BAIXO, BAIXO, BAIXO, ALGUMAS, BAIXO, BAIXO, ALGUMAS, BAIXO, INSUF],
    "RSL-107": [BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, BAIXO, ALGUMAS],
    "RSL-111": [BAIXO, BAIXO, ALGUMAS, BAIXO, INSUF, ALGUMAS, ALGUMAS, ALGUMAS, BAIXO],
    "RSL-112": [BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, ALGUMAS, ALGUMAS, ALGUMAS, INSUF],
    "RSL-113": [BAIXO, BAIXO, BAIXO, ALGUMAS, ALGUMAS, BAIXO, BAIXO, BAIXO, INSUF],
}


SPECIAL = {
    ("RSL-002", "D2"): "O TEOM foi comparado à média de amostradores de alto volume de estações NABEL próximas, e não a um comparador estritamente colocalizado; a variação espacial pode alterar inclinação e viés.",
    ("RSL-003", "D2"): "As séries foram pareadas por sítio, mas a dissertação não descreve com a mesma precisão a distância/altura de todos os pares, especialmente para o comparador IMPROVE de Look Rock.",
    ("RSL-013", "D1"): "A campanha é bem contextualizada, mas combina aerossol ambiente e concentrado; somente o subconjunto ambiente representa diretamente o cenário elegível.",
    ("RSL-013", "D5"): "São relatados 39 testes totais, porém o denominador do subconjunto estritamente ambiente não está claramente separado em todos os resultados.",
    ("RSL-020", "D6"): "Há 38 locais externos e 303 pares, mas a conclusão é derivada de campanhas residenciais específicas e não de cobertura anual completa.",
    ("RSL-021", "D1"): "Os sítios fixos são descritos, porém foram selecionados dentro de um estudo de exposição de 21 crianças, o que limita a representatividade ambiental ampla.",
    ("RSL-027", "D6"): "As campanhas cobrem verão e inverno, mas cada período é curto e alguns estratos têm somente 9–20 pares.",
    ("RSL-044", "D2"): "O BAM da Embaixada dos EUA e o impactador Harvard estavam em pontos diferentes de Kuwait City; não há demonstração de que amostraram a mesma massa de ar.",
    ("RSL-044", "D7"): "A análise atribui a diferença aos métodos usando pares de locais distintos; correlação alta não separa viés instrumental de variabilidade espacial.",
    ("RSL-057", "D9"): "Há participação de autor ligado ao desenvolvimento do SES/TEOM e não foi identificada declaração formal de conflito; os resultados favorecem a configuração testada.",
    ("RSL-061", "D2"): "A validação local utiliza comparações apropriadas, mas a aplicação regional corrige TEOM em outros pontos com um único FDMS; esses dois usos devem permanecer separados.",
    ("RSL-064", "D3"): "O Partisol é identificável, porém o objetivo demonstra perdas químico-dependentes no próprio filtro; a massa gravimétrica não funciona como padrão sem erro neste cenário.",
    ("RSL-073", "D1"): "O ambiente de fundo é descrito, mas as datas completas da campanha não ficaram disponíveis no relato extraído.",
    ("RSL-076", "D3"): "Teflon e quartzo apresentaram diferenças de 5–10%; a escolha do substrato modifica o comparador e não há um único valor gravimétrico inequívoco.",
    ("RSL-085", "D9"): "Não foi localizada declaração explícita de conflitos na extração; não há, contudo, indício de participação de fabricante ou seleção de resultados.",
    ("RSL-086", "D9"): "O estudo declara financiamento do Electric Power Research Institute, Departamento de Energia e autoridade local; não há evidência direta de fabricante, mas o financiador setorial justifica cautela.",
    ("RSL-090", "D1"): "O sítio rural de Harwell é identificado, mas o período completo de comparação não está claramente apresentado no material extraído.",
    ("RSL-091", "D3"): "O texto usa um amostrador 'FRM-type', mas fornece menos rastreabilidade do comparador que dos protótipos TEOM/SES.",
    ("RSL-091", "D9"): "Todos os autores eram empregados ou dirigentes da Rupprecht & Patashnick, fabricante do TEOM/SES, e não houve avaliação independente descrita.",
    ("RSL-101", "D4"): "Houve perda de controle de temperatura e problemas no sistema de secagem, com perda de dados; as falhas podem ter alterado diferentemente CAMM, RAMS e TEOM diferencial.",
    ("RSL-101", "D5"): "A campanha teve muitos dados ausentes em agosto e somente 15 diferenças pareadas na análise massa–nitrato; a completude baixa ameaça a estabilidade das estimativas.",
    ("RSL-101", "D9"): "Um coautor era ligado à Rupprecht & Patashnick; a equipe é majoritariamente acadêmica, mas não foi identificada declaração formal de conflito.",
    ("RSL-103", "D3"): "Foram usados filtros em desvio como comparador; o sistema é gravimétrico e colocalizado, mas sua rastreabilidade a um FRM completo é limitada.",
    ("RSL-105", "D5"): "A captura do FDMS foi de 57% em Pinnacle/Addison e 65% em Queens, com grandes lacunas por problemas operacionais e incapacidade de validar dados; a sazonalidade pode ser afetada.",
    ("RSL-107", "D9"): "O estudo declara financiamento do Electric Power Research Institute, Departamento de Energia e autoridade local; não há fabricante declarado, mas existe interesse setorial potencial.",
    ("RSL-111", "D5"): "O artigo principal não informa o número de pares gravimetria–nefelômetro para as duas campanhas externas.",
    ("RSL-111", "D8"): "Equações são apresentadas, mas o número de pares e os R² específicos de cada ambiente não aparecem no texto principal; parte da documentação depende do suplemento.",
    ("RSL-111", "D9"): "O financiamento é declarado como recurso da Democritus University of Thrace e não há participação comercial identificada.",
    ("RSL-112", "D5"): "A comparação colocalizada ocorreu de 11/04 a 19/06/1996, mas o número exato de pares válidos e eventuais exclusões não são explicitados.",
    ("RSL-112", "D7"): "É apresentada regressão forçada pela origem (TEOM=0,93×Partisol) e r=0,73, sem intercepto livre, incerteza ou análise de diferenças.",
    ("RSL-112", "D8"): "O artigo completo permite verificar a conclusão, mas a comparação principal aparece sobretudo em figura digitalizada e faltam denominadores analíticos.",
}


D9_DEFAULT = {
    BAIXO: "Financiamento/conflitos são informados e não foi identificada participação comercial ou indício de seleção de resultados.",
    ALGUMAS: "Existe interesse institucional/setorial ou participação comercial potencial; não há evidência suficiente de distorção, mas a independência merece cautela.",
    ALTO: "A avaliação foi conduzida pelo fabricante ou sob interesse comercial direto, sem salvaguarda independente suficiente.",
    INSUF: "O documento não apresenta declaração suficientemente clara de conflitos e financiamento para excluir relato seletivo.",
}


def generic_justification(code, rating, row):
    if code == "D1":
        if rating == BAIXO:
            return f"Local e período estão descritos: {row['País/local']}; {row['Período de medição']}. O contexto é {row['Contexto/local de monitoramento']}."
        if rating == ALGUMAS:
            return f"O contexto é identificável ({row['País/local']}), mas a seleção ou o período ({row['Período de medição']}) limita a representatividade ou está incompletamente descrito."
        return "Local, período ou processo de seleção não permitem julgamento seguro."
    if code == "D2":
        if rating == BAIXO:
            return f"O relato sustenta comparação espacial e temporal apropriada: {row['Colocalização/coincidência']}; agregação {row['Agregação temporal']}."
        if rating == ALGUMAS:
            return f"A comparação é plausível, mas algum detalhe espacial/temporal permanece incompleto: {row['Colocalização/coincidência']}."
        if rating == ALTO:
            return f"A comparação não assegura a mesma massa de ar ou coincidência adequada: {row['Colocalização/coincidência']}."
        return "Colocalização, altura, distância ou regra de pareamento não são informadas suficientemente."
    if code == "D3":
        if rating == BAIXO:
            return f"O comparador é identificável e tecnicamente adequado: {row['Comparador gravimétrico']}."
        if rating == ALGUMAS:
            return f"O comparador é plausível ({row['Comparador gravimétrico']}), mas há rastreabilidade incompleta ou artefato relevante parcialmente tratado."
        if rating == ALTO:
            return f"O comparador ({row['Comparador gravimétrico']}) apresenta limitação grave para representar a fração/massa de referência."
        return f"A descrição do comparador é insuficiente: {row['Comparador gravimétrico']}."
    if code == "D4":
        if rating == BAIXO:
            return f"Tecnologia e configuração são descritas, com controle operacional suficiente no texto: {row['Método automático']}."
        if rating == ALGUMAS:
            return f"O equipamento é identificado ({row['Método automático']}), mas calibração, manutenção ou critérios de validade não estão completos para todas as séries."
        if rating == ALTO:
            return f"Foram observadas falhas ou controle inadequado com potencial de alterar o resultado do método automático: {row['Método automático']}."
        return "A configuração e o controle de qualidade do método automático não permitem julgamento."
    if code == "D5":
        if rating == BAIXO:
            return f"Denominadores e tratamento dos dados são suficientemente rastreáveis. Número relatado: {row['N pares/observações']}."
        if rating == ALGUMAS:
            return f"Há informação parcial sobre pares, perdas ou exclusões ({row['N pares/observações']}), sem evidência de seleção grave, mas com incerteza residual."
        if rating == ALTO:
            return f"Perdas, exclusões ou baixa completude podem alterar materialmente a comparação. Informação disponível: {row['N pares/observações']}."
        return f"Não é possível julgar completude e exclusões; denominador disponível: {row['N pares/observações']}."
    if code == "D6":
        if rating == BAIXO:
            return f"A duração e o desenho cobrem condições coerentes com a conclusão: {row['Período de medição']}; fatores examinados: {row['Fatores condicionantes']}."
        if rating == ALGUMAS:
            return f"A cobertura é útil, mas curta, sazonal ou restrita para generalizações amplas: {row['Período de medição']}."
        if rating == ALTO:
            return "A faixa de concentração ou as condições são incompatíveis com a generalização apresentada."
        return "Faixa de concentração e condições ambientais não são descritas suficientemente."
    if code == "D7":
        if rating == BAIXO:
            return f"A análise apresenta medidas quantitativas pertinentes à comparabilidade: {row['Métricas/resultados quantitativos']}."
        if rating == ALGUMAS:
            return f"A análise informa associação/regressão, mas concordância, incerteza, intercepto ou dependência recebem tratamento limitado: {row['Métricas/resultados quantitativos']}."
        if rating == ALTO:
            return f"A análise não separa adequadamente viés instrumental de outras fontes ou interpreta associação como concordância: {row['Métricas/resultados quantitativos']}."
        return "Os procedimentos ou resultados quantitativos não podem ser reconstruídos."
    if code == "D8":
        if rating == BAIXO:
            return "Métodos, resultados e limitações são suficientemente rastreáveis no documento completo."
        if rating == ALGUMAS:
            return f"A conclusão principal é verificável, mas faltam detalhes ou valores aparecem apenas em figuras/suplementos. Estado: {row['Status da extração']}."
        if rating == ALTO:
            return "O relato é fragmentário ou contraditório a ponto de impedir verificação adequada."
        return "O documento acessível não permite avaliar a completude do relato."
    if code == "D9":
        return D9_DEFAULT[rating]
    raise KeyError(code)


def overall(ratings):
    critical = [1, 2, 4, 6]  # D2, D3, D5 e D7
    high_codes = [DOMAINS[i][0] for i, rating in enumerate(ratings) if rating == ALTO]
    if any(ratings[index] == ALTO for index in critical) or len(high_codes) >= 2:
        reason = "Alto risco em domínio crítico" if any(ratings[index] == ALTO for index in critical) else "Alto risco em dois ou mais domínios"
        return "Alto risco global", f"{reason}: {', '.join(high_codes)}."
    if any(rating in {ALGUMAS, INSUF, ALTO} for rating in ratings):
        flagged = [DOMAINS[i][0] for i, rating in enumerate(ratings) if rating != BAIXO]
        return "Algumas preocupações globais", f"Sem alto risco em domínio crítico, mas há limitações ou informação insuficiente em: {', '.join(flagged)}."
    return "Baixo risco global", "Todos os domínios foram classificados como baixo risco."


def main():
    with (EXTRACAO / "extracao_dados.csv").open(encoding="utf-8-sig", newline="") as f:
        source_rows = list(csv.DictReader(f))
    ids = {row["ID"] for row in source_rows}
    if ids != RATINGS.keys():
        raise RuntimeError(f"IDs divergentes: extração={sorted(ids)} avaliação={sorted(RATINGS)}")

    output = []
    for row in source_rows:
        study_ratings = RATINGS[row["ID"]]
        item = {
            "ID": row["ID"],
            "Título": row["Título"],
            "Ano": row["Ano da publicação"],
            "Família/sobreposição": row["Família/sobreposição"],
        }
        for (code, name), rating in zip(DOMAINS, study_ratings):
            item[f"{code} — {name}"] = rating
            item[f"{code} — Justificativa"] = SPECIAL.get(
                (row["ID"], code), generic_justification(code, rating, row)
            )
        global_rating, global_reason = overall(study_ratings)
        item["Sinalização global"] = global_rating
        item["Justificativa global"] = global_reason
        item["Revisor/etapa"] = "Avaliação piloto por um revisor; requer segunda avaliação independente"
        output.append(item)

    df = pd.DataFrame(output)
    SAIDA.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAIDA / "avaliacao_metodologica.csv", index=False, encoding="utf-8-sig")

    summary_rows = []
    for index, (code, name) in enumerate(DOMAINS):
        counts = Counter(RATINGS[row["ID"]][index] for row in source_rows)
        summary_rows.append(
            {
                "Domínio": f"{code} — {name}",
                BAIXO: counts[BAIXO],
                ALGUMAS: counts[ALGUMAS],
                ALTO: counts[ALTO],
                INSUF: counts[INSUF],
            }
        )
    global_counts = Counter(row["Sinalização global"] for row in output)
    summary_rows.extend(
        [
            {"Domínio": "GLOBAL — Baixo risco", BAIXO: global_counts["Baixo risco global"], ALGUMAS: "", ALTO: "", INSUF: ""},
            {"Domínio": "GLOBAL — Algumas preocupações", BAIXO: "", ALGUMAS: global_counts["Algumas preocupações globais"], ALTO: "", INSUF: ""},
            {"Domínio": "GLOBAL — Alto risco", BAIXO: "", ALGUMAS: "", ALTO: global_counts["Alto risco global"], INSUF: ""},
        ]
    )
    summary = pd.DataFrame(summary_rows)

    rules = pd.DataFrame(
        [
            ["Baixo risco", "Relato suficiente e sem limitação material identificada."],
            ["Algumas preocupações", "Limitação ou omissão plausivelmente relevante, sem comprometimento grave demonstrado."],
            ["Alto risco", "Limitação com probabilidade substancial de alterar direção ou magnitude."],
            ["Informação insuficiente", "Relato não permite julgamento; não equivale automaticamente a alto risco."],
            ["Global alto", "Alto risco em D2, D3, D5 ou D7; ou alto risco em dois ou mais outros domínios."],
            ["Global com preocupações", "Nenhum domínio crítico em alto risco, mas existe preocupação, insuficiência ou alto risco não crítico isolado."],
            ["Global baixo", "Todos os nove domínios em baixo risco."],
        ],
        columns=["Regra", "Aplicação"],
    )

    widths = [12, 52, 10, 34]
    for _ in DOMAINS:
        widths.extend([23, 70])
    widths.extend([28, 58, 45])
    write_xlsx(
        SAIDA / "avaliacao_metodologica.xlsx",
        [
            ("Avaliação", df, widths),
            ("Resumo", summary, [60, 18, 24, 18, 24]),
            ("Regras", rules, [30, 110]),
        ],
    )

    print(f"Avaliados {len(df)} documentos")
    print("Global:", dict(global_counts))


if __name__ == "__main__":
    main()