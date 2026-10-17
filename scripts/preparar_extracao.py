import csv
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TRIAGEM = ROOT / "dados/triagem"
SAIDA = ROOT / "dados/extracao"


def d(
    local,
    periodo,
    contexto,
    fracao,
    automatico,
    comparador,
    colocalizacao,
    agregacao,
    n,
    metricas,
    fatores,
    achado,
    restricoes="",
    alerta="",
    familia="",
    status="Extração preliminar concluída; conferir números no texto antes da síntese final",
):
    return {
        "País/local": local,
        "Período de medição": periodo,
        "Contexto/local de monitoramento": contexto,
        "Fração": fracao,
        "Método automático": automatico,
        "Comparador gravimétrico": comparador,
        "Colocalização/coincidência": colocalizacao,
        "Agregação temporal": agregacao,
        "N pares/observações": n,
        "Métricas/resultados quantitativos": metricas,
        "Fatores condicionantes": fatores,
        "Achado principal": achado,
        "Restrição da extração": restricoes,
        "Alerta de elegibilidade": alerta,
        "Família/sobreposição": familia,
        "Status da extração": status,
    }


DATA = {
    "RSL-001": d(
        "Polônia — Gdynia, estação AM9",
        "07/02/2007–09/02/2008; análises sazonais em 2007–2008",
        "Estação urbana/de fundo da rede ARMAAG",
        "PM10",
        "Eberline por atenuação beta; TEOM",
        "Digitel de alto volume, gravimétrico",
        "Lado a lado; períodos de 24 h",
        "24 h",
        "Ao menos 40 pares por ensaio de equivalência; total exato a confirmar",
        "Diferenças de até 47%; os instrumentos automáticos não atenderam estritamente à PN-EN 12341 nos estratos sazonais",
        "Estação do ano, composição do aerossol, meteorologia e fator de correção",
        "A equivalência dependeu de correções específicas; um fator único não representou adequadamente todas as condições.",
        familia="ARMAAG — campanha de Gdynia distinta de RSL-113",
    ),
    "RSL-002": d(
        "Suíça — Zurique-Hönggerberg",
        "Inverno de 2005/2006",
        "Sítio urbano; comparação com a rede nacional NABEL",
        "PM10 (PM1 também medido, fora do desfecho principal)",
        "TEOM com entrada sequencial e aquecimento a 50 °C",
        "Digitel DAH-80 de alto volume da rede NABEL",
        "Comparação temporal com médias de estações próximas; não estritamente colocalizada",
        "24 h",
        "Não informado na extração preliminar",
        "R²=0,96; inclinação por eixo principal reduzido=0,61",
        "Perdas de material semivolátil e água pelo aquecimento; inverno",
        "O TEOM acompanhou a variação temporal, mas apresentou concentração sistematicamente menor que o método de alto volume.",
        alerta="Confirmar se a representação da mesma massa de ar atende ao critério, pois o comparador foi derivado de estações próximas.",
    ),
    "RSL-003": d(
        "Estados Unidos — East Tennessee: Knoxville/Knox County e Look Rock",
        "Abril de 2002–abril de 2003",
        "Um sítio urbano e um rural",
        "PM2,5",
        "TEOM",
        "FRM em Knox County; IMPROVE gravimétrico em Look Rock",
        "Medições correspondentes por sítio; verificar detalhes de colocalização do IMPROVE",
        "24 h",
        "Não informado na extração preliminar",
        "Knox: inclinação=1,0111, intercepto=-0,1396, R²=0,9181. Look Rock: inclinação=1,1363, intercepto=2,583, R²=0,9606",
        "Temperatura ambiente e caráter urbano/rural",
        "Houve forte associação com os comparadores e não se observou efeito consistente e importante da temperatura nos dois sítios.",
        restricoes="A dissertação foi aceita como relatório completo alternativo à publicação de congresso não localizada.",
        familia="East Tennessee — dissertação vinculada ao registro do congresso",
    ),
    "RSL-011": d(
        "Estados Unidos — EPA Region 5: Wisconsin, Michigan e Illinois",
        "2000–2002",
        "Mayville, Grand Rapids, Chicago e East St. Louis",
        "PM2,5",
        "TEOM; monitor beta; nefelômetro",
        "FRM gravimétrico",
        "Comparações colocalizadas por sítio",
        "Horária agregada para 24 h",
        "FRM: 332 em Mayville, 971 em Grand Rapids, 119 em Chicago e 113 em East St. Louis",
        "TEOM: correlação linear mínima 0,7924 e ajuste não linear até 0,9370; resultados próprios por instrumento/sítio",
        "Temperatura, umidade relativa, sítio e tecnologia",
        "Modelos não lineares e meteorológicos melhoraram TEOM e nefelômetro; o monitor beta foi relativamente menos sensível às variáveis meteorológicas.",
        restricoes="Manter estimativas por instrumento e por sítio como dependentes dentro da mesma publicação.",
    ),
    "RSL-013": d(
        "Estados Unidos — Sul da Califórnia",
        "Campanha de campo; datas exatas a confirmar",
        "Aerossol ambiente e aerossol concentrado; apenas o subconjunto ambiente é diretamente aplicável",
        "PM2,5",
        "DataRAM/MIE modificado, espalhamento de luz",
        "Massa gravimétrica com correção para nitrato",
        "Ensaios simultâneos no sistema de campo",
        "Tempo real comparado a amostras integradas",
        "39 testes totais; número do subconjunto ambiente a confirmar",
        "Razão DataRAM/gravimetria no ambiente=0,93±0,17; aerossol concentrado=1,23±0,20",
        "Diâmetro médio de massa, distribuição de tamanho e composição",
        "O tamanho das partículas explicou mais a resposta óptica que a composição; o desempenho foi melhor para diâmetros médios de 0,4–0,7 µm.",
        restricoes="Separar resultados de aerossol ambiente dos ensaios com concentração artificial.",
    ),
    "RSL-020": d(
        "Estados Unidos — Seattle",
        "Campanhas residenciais; datas exatas a confirmar",
        "Áreas externas de residências; resultados indoor e pessoais não entram",
        "PM2,5",
        "Nefelômetro Radiance",
        "Impactador Harvard gravimétrico, validado contra FRM",
        "Colocalizado nos pontos externos",
        "24 h",
        "303 pares em 38 locais externos",
        "R²=0,88 no subconjunto externo",
        "Fonte/composição do aerossol; ambiente de medição",
        "O nefelômetro apresentou boa correspondência externa com o impactador; relações indoor e pessoais não devem ser misturadas à síntese ambiental.",
        restricoes="Extrair somente o subconjunto outdoor.",
    ),
    "RSL-021": d(
        "Estados Unidos — Sul da Califórnia",
        "Campanha com 21 crianças asmáticas; datas exatas a confirmar",
        "Sítios fixos externos/centrais; medições pessoais e indoor excluídas da síntese",
        "PM2,5",
        "Personal DataRAM (pDR) em diferentes configurações",
        "Impactador Harvard gravimétrico",
        "Colocalizado nas medições fixas externas",
        "24 h",
        "Não informado para cada configuração na extração preliminar",
        "Após controle de qualidade/correção por umidade, R² nos sítios fixos aproximadamente 0,53–0,72",
        "Umidade relativa, configuração do instrumento e ambiente",
        "A umidade elevada alterou a resposta óptica; o controle de qualidade e a correção meteorológica melhoraram a comparabilidade.",
        restricoes="Extrair somente medições fixas externas/centrais.",
    ),
    "RSL-024": d(
        "Estados Unidos — Carolina do Norte e região IA/IL",
        "Períodos multissazonais; datas exatas a confirmar",
        "Greensboro/Winston-Salem/High Point e Davenport/Moline/Rock Island",
        "PM2,5",
        "TEOM",
        "Partisol-Plus 2025 FRM",
        "O artigo informa uso exclusivo de dados colocalizados",
        "24 h",
        "227 pares em NC; 214 pares em IA/IL",
        "NC: modelo logarítmico R²=0,96. IA/IL: modelo com temperatura R²=0,86; modelo simples R²=0,69",
        "Temperatura, região e temperatura de operação do TEOM (50 °C/30 °C)",
        "A correção necessária variou por região; a inclusão da temperatura melhorou substancialmente o ajuste em IA/IL.",
    ),
    "RSL-027": d(
        "Estados Unidos — Ewing, New Jersey",
        "Setembro de 2004 e dezembro de 2004–fevereiro de 2005",
        "Campanhas de verão e inverno em ar ambiente",
        "PM2,5",
        "TEOM-FDMS; TEOM 50 °C; Met One BAM; Andersen BAM",
        "Partisol FRM",
        "Colocalizado",
        "24 h",
        "Verão: FDMS 27, TEOM 20, Met One 16. Inverno: FDMS 9, TEOM 20, Met One 15, Andersen 19",
        "Verão — FDMS: inclinação 1,28, intercepto -0,90, R²=0,96; TEOM: 0,95/2,26/0,94; Met One: 1,15/0,32/0,87. Inverno — FDMS: 1,17/-1,57/0,91; TEOM: 0,54/4,75/0,81; Met One: 0,89/0,50/0,95; Andersen: 0,86/0,40/0,94",
        "Estação, temperatura, material semivolátil e tecnologia",
        "O TEOM convencional subestimou especialmente no inverno; FDMS e BAM conservaram melhor a massa, embora o FDMS tenha ficado acima do FRM no verão.",
        restricoes="Preservar resultados por tecnologia e estação como estimativas dependentes.",
    ),
    "RSL-029": d(
        "Estados Unidos — EPA Region 5; validação adicional em New York",
        "Séries majoritariamente de pelo menos um ano",
        "Dez monitores/sítios em Indiana, Michigan, Minnesota e outros; teste externo em seis TEOM de New York",
        "PM2,5",
        "TEOM",
        "FRM colocalizado",
        "Colocalizado por sítio",
        "24 h",
        "Mínimo de 63 observações por ajuste; número total a confirmar",
        "Modelos segmentados com nós de temperatura entre 12,9 e 20,6 °C; validação em NY geralmente R²>0,85",
        "Temperatura, sítio, concentração e composição",
        "Modelos específicos por sítio corrigiram melhor o TEOM; o efeito da temperatura foi não linear e variou espacialmente.",
        restricoes="Várias estimativas por sítio; não tratar como estudos independentes.",
    ),
    "RSL-044": d(
        "Kuwait — Kuwait City",
        "Outubro de 2017–outubro de 2019",
        "Sítio de amostragem e monitor BAM da Embaixada dos EUA em locais distintos da cidade",
        "PM2,5",
        "BAM da Embaixada dos EUA",
        "Impactador Harvard gravimétrico",
        "Não colocalizado; pareamento diário entre locais urbanos distintos",
        "24 h",
        "607 pares",
        "BAM 53,1±36,8 µg/m³; gravimétrico 41,6±29,0 µg/m³; diferença média 11,5 µg/m³; r=0,91",
        "Meses de poeira (junho/julho), fontes, variabilidade espacial e concentração",
        "O BAM apresentou valores maiores; a alta correlação não elimina o possível componente espacial entre os dois locais.",
        alerta="Reconsiderar elegibilidade: os instrumentos não foram colocalizados e a comparação pode refletir variabilidade espacial.",
    ),
    "RSL-045": d(
        "Estados Unidos — cidades do leste dos EUA",
        "Campanhas multissítio; datas exatas a confirmar",
        "Comparações urbanas em diferentes cidades",
        "PM2,5",
        "CAMM; RAMS; TEOM com secador Nafion",
        "Amostradores integrados/FRM",
        "Colocalizado por campanha",
        "Contínua agregada à amostra integrada",
        "Não informado na extração preliminar",
        "Diferenças médias entre contínuos de 10–30%; TEOM seco com R²>0,90 e inclinações próximas de 1; CAMM/RAMS R² aproximadamente 0,6–0,9 e inclinações 0,7–1,0",
        "Sítio, tempo, material semivolátil e condicionamento da amostra",
        "O TEOM com secagem apresentou a relação mais estável; CAMM subestimou em todos os sítios e o desempenho variou espacial e temporalmente.",
    ),
    "RSL-049": d(
        "Canadá — Toronto, estação Evans",
        "Desde julho de 1995; período final a confirmar",
        "Programa canadense de monitoramento de partículas finas",
        "PM2,5",
        "TEOM",
        "Amostrador dicotômico Graseby-Andersen, gravimétrico",
        "Colocalizado",
        "24 h, aproximadamente a cada seis dias",
        "Não informado na extração preliminar",
        "Razão TEOM/dicotômico=0,88 no período quente e 0,77 no frio; subestimação chegou a aproximadamente 50% em casos frios",
        "Temperatura, estação e material semivolátil",
        "A perda do TEOM foi maior no frio, indicando que uma correção constante não representa a sazonalidade.",
    ),
    "RSL-057": d(
        "Reino Unido — Sunderland",
        "Novembro de 2000–agosto de 2001",
        "Sítio de meio-fio no nordeste da Inglaterra",
        "PM10",
        "TEOM 50 °C; TEOM com Sample Equilibration System a 30 °C",
        "Partisol Plus 2025 conforme EN 12341",
        "Colocalizado",
        "24 h",
        "Não informado na extração preliminar",
        "O TEOM com SES mediu concentrações maiores e apresentou melhor relação com o Partisol; correlação sazonal mais forte no verão",
        "Estação, umidade relativa, água ligada às partículas e condicionamento térmico",
        "O SES reduziu perdas, mas no inverno o Partisol ainda mediu valores muito maiores; um fator único de escala foi inadequado.",
    ),
    "RSL-061": d(
        "Reino Unido — rede de Londres/UK",
        "Período de desenvolvimento e validação multianual; datas a confirmar",
        "Rede regional de monitoramento",
        "PM10",
        "TEOM; sinal de purga de FDMS usado na correção",
        "Método gravimétrico de referência europeu",
        "Validação por sítio; FDMS regional nem sempre no mesmo ponto do TEOM corrigido",
        "24 h",
        "Não informado na extração preliminar",
        "Modelo de correção volátil baseado no sinal de purga do FDMS; atendeu aos critérios de equivalência declarados",
        "Componente volátil regional, temperatura e localização",
        "A homogeneidade regional do material volátil permitiu corrigir vários TEOM com um FDMS regional, com desempenho melhor que fatores fixos.",
        alerta="Distinguir a validação colocalizada da aplicação regional não colocalizada do modelo.",
    ),
    "RSL-064": d(
        "México — sítio T1 da campanha MILAGRO, região da Cidade do México",
        "Campanha MILAGRO; 2006",
        "Sítio de campo influenciado por aerossol urbano/regional",
        "PM2,5",
        "TEOM-GIT com SES/secador a 30 °C; TEOM-DF a 35 °C",
        "Partisol gravimétrico",
        "Colocalizado",
        "Contínua e integrada; correspondência temporal a confirmar",
        "Não informado na extração preliminar",
        "Comparabilidade variou conforme sulfato ou nitrato de amônio predominante; sem estimativa única apropriada",
        "Composição química, nitrato de amônio volátil, sulfato, umidade relativa e água",
        "Os artefatos foram dependentes da química: perdas aumentaram quando o nitrato volátil predominou, e o próprio gravimétrico também apresentou artefatos.",
    ),
    "RSL-066": d(
        "Reino Unido — London, Marylebone Road",
        "Junho de 1997–janeiro de 2000",
        "Sítio urbano de tráfego",
        "PM10",
        "TEOM",
        "Partisol gravimétrico",
        "Colocalizado",
        "24 h",
        "Não informado na extração preliminar",
        "O fator britânico 1,3 superestimou dias de excedência em 50%; superestimou média anual em 13% (1998) e 8% (1999)",
        "Ano, estação, concentração e composição urbana",
        "O fator fixo 1,3 não foi apropriado para o sítio; ajustes curvilíneos não resolveram completamente a variação.",
    ),
    "RSL-069": d(
        "Grécia — Atenas, sítio suburbano",
        "2009–2012",
        "Monitoramento suburbano durante quatro anos",
        "PM2,5 e PM10",
        "Thermo ESM Andersen FH62I-R por atenuação beta",
        "Método gravimétrico de referência",
        "Colocalizado",
        "24 h; algumas amostras de até 72 h",
        "Não informado na extração preliminar",
        "Beta cerca de 30% maior para PM2,5 e 10% para PM10; r total=0,79 e 0,85; frio=0,84/0,95; quente=0,72/0,90",
        "Estação, vapor de água, material do filtro e semivoláteis",
        "O viés e a correlação diferiram por fração e estação; a água retida contribuiu para valores maiores do beta.",
    ),
    "RSL-073": d(
        "Finlândia — sítio de fundo",
        "Período a confirmar",
        "Ar de fundo com baixas concentrações",
        "PM10",
        "Monitor por atenuação beta",
        "Amostrador gravimétrico de baixo volume",
        "Colocalizado",
        "24 h",
        "42 pares",
        "Razão monitor/referência=1,06±0,12; diferença média=0,2 µg/m³; faixa de 1,5–18 µg/m³, média 5,1",
        "Umidade relativa >85%, temperatura <0 °C e baixa concentração",
        "Os métodos foram comparáveis em níveis baixos, com pequeno aumento do beta sob alta umidade e temperatura negativa.",
    ),
    "RSL-076": d(
        "África do Sul — Qalabotjha",
        "Inverno de 1997; campanha de 30 dias",
        "Área residencial durante experimento de combustível de baixa emissão",
        "PM2,5 e PM10",
        "TEOM a 50 °C",
        "Filtros integrados de Teflon e quartzo",
        "Colocalizado",
        "Integrada; aproximadamente diária",
        "30 dias; número exato de pares válidos a confirmar",
        "TEOM PM10 aproximadamente 15% menor; quartzo 5–10% maior que Teflon",
        "Aquecimento, fumaça de carvão, componentes voláteis, substrato do filtro e meteorologia",
        "O TEOM perdeu massa volátil e os próprios filtros diferiram entre si, demonstrando dependência do comparador.",
    ),
    "RSL-082": d(
        "Estados Unidos — Maryland, sítio suburbano",
        "Janeiro e julho de 2002",
        "Campanhas de inverno e verão",
        "PM2,5",
        "TEOM",
        "STN RAAS/SASS e amostrador sequencial DRI, todos por filtro",
        "Colocalizado",
        "24 h",
        "Não informado na extração preliminar",
        "DRI/Teflon e STN/SASS versus TEOM: r=0,95; inclinações dentro de 11% da unidade; viés positivo no STN/SASS e leve negativo no DRI",
        "Protocolo do amostrador/laboratório, velocidade de face, perdas voláteis e estação",
        "Mesmo entre métodos de filtro ocorreram diferenças sistemáticas; o protocolo do comparador condicionou a avaliação do TEOM.",
    ),
    "RSL-085": d(
        "Taiwan — cinco estações",
        "Diferentes estações do ano; período completo a confirmar",
        "Rede multissítio",
        "PM2,5",
        "BAM-1020; TEOM-FDMS",
        "FRM gravimétrico",
        "Colocalizado em cada estação",
        "24 h",
        "265 pares diários",
        "BAM: viés 1,67±12,43%, reduzido a 0,63±8,75% após correção. TEOM-FDMS: 13,86±14,50%, reduzido a -0,85±9,00%",
        "Concentração, temperatura, umidade relativa, água e perda por evaporação",
        "Correções por fatores ambientais reduziram o viés de ambos os FEM; a magnitude e o sinal diferiram entre tecnologias.",
        restricoes="Conservar resultados antes e depois da correção como estimativas vinculadas.",
    ),
    "RSL-086": d(
        "Estados Unidos — Pittsburgh, Lawrenceville",
        "1999–2008",
        "Sítio central do estudo PARIES",
        "PM2,5",
        "TEOM e outros amostradores de especiação/integrados",
        "Três FRM gravimétricos",
        "Sete amostradores colocalizados no mesmo sítio",
        "24 h",
        "7.865 observações diárias",
        "Modelagem por equações estruturais de viés, imprecisão e efeito sigmoide da temperatura; estimativas por instrumento",
        "Temperatura, tipo de amostrador, viés e imprecisão",
        "FRM apresentou maior precisão; o viés e a imprecisão do TEOM diminuíram com o aumento da temperatura.",
        restricoes="Não contar como estudo independente do RSL-107; representa análise aprofundada de um subconjunto/sítio.",
        familia="PARIES/Pittsburgh — mesma família de RSL-107",
    ),
    "RSL-089": d(
        "Estados Unidos — Sul da Califórnia/Los Angeles",
        "06/12/2002–19/02/2003",
        "Supersite urbano; ensaio de desempenho em ar ambiente externo",
        "PM2,5",
        "Três pDR-1200 de fluxo ativo; BAM como comparação adicional",
        "Partisol 2025 FRM e filtros de retaguarda dos pDR",
        "Colocalizado",
        "24 h e contínua",
        "20 execuções simultâneas de 24 h com FRM",
        "Precisão entre pDR=2,1%; filtro de retaguarda/FRM=1,027; R²=0,93; inclinação=0,91",
        "Umidade relativa, tamanho das partículas e correção gravimétrica",
        "Os instrumentos tiveram boa precisão; o filtro de retaguarda aproximou a massa do FRM, enquanto a resposta óptica exigiu atenção à umidade e ao tamanho.",
    ),
    "RSL-090": d(
        "Reino Unido — Harwell, Oxfordshire",
        "Período a confirmar",
        "Sítio rural",
        "PM10 e PM2,5",
        "TEOM",
        "Partisol gravimétrico",
        "Colocalizado e simultâneo",
        "24 h",
        "Não informado na extração preliminar",
        "TEOM menor que Partisol, com divergência maior em concentrações elevadas; resultados químicos por fração",
        "Nitrato de amônio, material semivolátil, temperatura, umidade relativa e água",
        "A divergência foi dominada pelo material semivolátil, principalmente na fração fina, e não por uma diferença constante entre instrumentos.",
    ),
    "RSL-091": d(
        "Estados Unidos — Albany, New York",
        "06/06–25/09; ano a confirmar no artigo",
        "Desenvolvimento e teste de campo do Sample Equilibration System",
        "PM2,5",
        "TEOM com SES; TEOM convencional",
        "FRM gravimétrico",
        "Colocalizado no ensaio de campo",
        "24 h",
        "115 pontos diários",
        "TEOM 30 °C com SES: y=1,0283x-1,6469, R²=0,9352. TEOM 50 °C sem SES: y=0,8613x-0,5048, R²=0,6309; diferença média de aproximadamente 14%",
        "Temperatura de condicionamento, material semivolátil e umidade",
        "Reduzir a temperatura e equilibrar a amostra diminuiu perdas do TEOM sem abandonar a medição contínua.",
        status="Extração preliminar concluída; coeficientes conferidos diretamente na Figura 5",
    ),
    "RSL-095": d(
        "América do Norte — dez áreas urbanas, incluindo Rubidoux, Tlalnepantla e Merced",
        "Campanhas multissítio; período a confirmar",
        "Áreas urbanas com diferentes climas e composições",
        "PM10 e PM2,5",
        "TEOM",
        "Métodos manuais gravimétricos de referência",
        "Colocalizado por campanha",
        "24 h",
        "Não informado na extração preliminar",
        "Correlações menores no inverno e subestimação mais intensa em sítios de alta concentração; métricas específicas por sítio a transcrever",
        "Temperatura, estação, concentração, nitrato e água",
        "O desempenho do TEOM variou fortemente entre cidades e estações; a perda de nitrato semivolátil foi importante nos sítios mais carregados.",
        restricoes="Resultados multissítio devem permanecer dependentes dentro da publicação.",
    ),
    "RSL-101": d(
        "Estados Unidos — Rubidoux, Califórnia",
        "15/08–07/09/2001",
        "Sítio urbano com aerossol rico em nitrato",
        "PM2,5",
        "TEOM diferencial; CAMM; RAMS",
        "FRM gravimétrico",
        "Colocalizado",
        "Contínua agregada à amostra de 24 h",
        "Horárias: CAMM 533, RAMS 366, TEOM diferencial 313; 15 diferenças pareadas para massa/nitrato",
        "TEOM diferencial vs FRM: R²=0,52, inclinação=0,91, intercepto=11,3 µg/m³; médias de 24 h=36,4 vs 26,8 µg/m³, diferença=9,6. CAMM/FRM R²=0,03; RAMS/FRM R²=0,00",
        "Nitrato de amônio, temperatura, composição e princípio instrumental",
        "A diferença entre TEOM diferencial e FRM foi compatível com perdas de nitrato no próprio filtro, evidenciando artefatos em ambos os lados da comparação.",
        status="Extração preliminar concluída; conferir a quantidade exata de pares TEOM–FRM antes da síntese final",
    ),
    "RSL-103": d(
        "Estados Unidos — New Jersey",
        "TEOM: julho de 1997–junho de 1998; filtros de desvio: fevereiro de 1998–fevereiro de 1999",
        "Áreas urbanas/suburbanas",
        "PM2,5",
        "TEOM",
        "Filtros gravimétricos instalados em desvio",
        "Colocalizado no sistema",
        "24 h",
        "104 pares",
        "R²=0,95; nenhuma diferença sazonal estatisticamente significativa ao nível de 95%",
        "Estação e tipo de área",
        "O TEOM forneceu dados temporais compatíveis com os filtros de desvio e não mostrou alteração sazonal clara neste conjunto.",
    ),
    "RSL-105": d(
        "Estados Unidos — New York: Queens e Pinnacle",
        "Janeiro de 2003–dezembro de 2004",
        "Um sítio urbano e um rural",
        "PM2,5",
        "FDMS-TEOM; TEOM convencional; BAM",
        "FRM gravimétrico",
        "Colocalizado em cada sítio",
        "24 h",
        "Queens: 244 pares BAM–FDMS, 283 FDMS–FRM e 320 BAM–FRM. Addison: 349 pares FDMS–FRM em 22 meses",
        "Queens — BAM/FDMS: y=1,02x+1,72, R²=0,93; FDMS/FRM: y=1,25x-0,63, R²=0,95; BAM/FRM: y=1,28x+1,27, R²=0,88. Addison — FDMS/FRM: y=1,088x-0,004, R²=0,945",
        "Sítio urbano/rural, estação, semivoláteis e tecnologia",
        "FDMS e BAM representaram melhor a massa do FRM que o TEOM convencional, mas o desempenho não foi idêntico nos dois ambientes.",
        status="Extração preliminar concluída; coeficientes conferidos diretamente nas Figuras 1–3",
    ),
    "RSL-106": d(
        "Estados Unidos — Kansas, dois confinamentos bovinos",
        "KS1: maio de 2006–fevereiro de 2008; KS2: fevereiro de 2007–fevereiro de 2008",
        "Ambiente externo próximo a fontes agropecuárias",
        "PM10",
        "TEOM",
        "Amostradores FRM de alto e baixo volume",
        "Colocalizado por sítio",
        "Integrada; durações conforme campanha",
        "TEOM–alto volume: 208 pares em KS1 e 98 em KS2; baixo–alto volume: 190 e 63",
        "TEOM/HV: KS1 inclinação=1,07, R²=0,95; KS2=1,04, R²=0,85; combinado=1,06, R²=0,93. Verão=1,01/R² 0,93; inverno=0,94/R² 0,96. LV/HV combinado=0,53/R² 0,93",
        "Sítio, duração de amostragem, estação, meteorologia e carga de poeira",
        "As diferenças dependeram do equipamento e das condições de campo; a ordem dos métodos foi consistente, mas não intercambiável sem ajuste.",
        status="Extração preliminar concluída; preservar estratos de sítio, posição e estação como dependentes",
    ),
    "RSL-107": d(
        "Estados Unidos — região de Pittsburgh, 35 condados",
        "1999–2008",
        "47 sítios do estudo PARIES",
        "PM2,5",
        "TEOM; FDMS; BAM; amostradores de especiação e dicotômicos",
        "FRM gravimétrico",
        "Comparações colocalizadas por sítio",
        "24 h",
        "75.927 observações válidas; 97 amostradores de 15 tipos em 47 sítios",
        "Equações de calibração por equações estruturais; efeito sigmoide da temperatura no TEOM a 50 °C; estimativas próprias por tipo",
        "Temperatura, tipo de amostrador, sítio, viés e imprecisão",
        "FRM foi o mais preciso; TEOM a 50 °C mostrou viés negativo dependente da temperatura, enquanto integrados tiveram vieses menores e menos térmicos.",
        restricoes="Publicação mais ampla da mesma família de RSL-086; usar como relatório principal da família e evitar dupla contagem.",
        familia="PARIES/Pittsburgh — mesma família de RSL-086",
    ),
    "RSL-111": d(
        "Grécia — Xanthi, áreas urbana e suburbana",
        "Urbana: setembro de 2013 e novembro de 2014; suburbana: 2019",
        "Ambiente externo urbano/suburbano; campanha indoor excluída",
        "PM2,5",
        "Nefelômetro",
        "Impactador/amostrador gravimétrico",
        "Colocalizado nas campanhas externas",
        "Integrada e contínua",
        "Número de dias pareados não informado no texto principal",
        "R² de cada ajuste Bsp–massa >0,70; PM2,5=0,55×Bsp+1,13 no urbano (RH ambiente) e PM2,5=0,42×Bsp+2,47 no suburbano (RH≤40%); Bsp–RH urbano R²=0,887",
        "Composição, tamanho, umidade e ambiente urbano/suburbano",
        "A sensibilidade do nefelômetro não foi constante entre campanhas; calibrações locais são necessárias.",
        restricoes="Excluir a campanha indoor.",
        status="Extração preliminar concluída; número de pares deve ser confirmado no material suplementar",
    ),
    "RSL-112": d(
        "Irlanda — Dublin",
        "01/01/1996–30/06/1996",
        "Sítios urbanos de Dublin",
        "PM10",
        "TEOM",
        "Partisol 2000 gravimétrico",
        "TEOM e Partisol colocalizados em College Green; comparação de 11/04 a 19/06/1996",
        "24 h",
        "Comparação diária entre 11/04 e 19/06; número de pares válidos não explicitado",
        "TEOM=0,93×Partisol; r=0,73. O Partisol apresentou valores menores que o TEOM abaixo de aproximadamente 30 µg/m³",
        "Sítio, sazonalidade e método histórico de black smoke",
        "Na campanha colocalizada de College Green houve concordância moderada, com inclinação próxima de 1, mas dispersão relevante e viés dependente da concentração.",
        status="Extração preliminar concluída; valores conferidos diretamente na Figura 4 e no texto digitalizado",
    ),
    "RSL-113": d(
        "Polônia — Gdańsk, estação AM8",
        "Janeiro–dezembro de 2010",
        "Estação urbana da rede ARMAAG",
        "PM10",
        "Eberline FH 62-1 por absorção beta",
        "Digitel de alto volume, gravimétrico",
        "Colocalizado; 24 h",
        "24 h",
        "Campanha anual; número de pares válidos a confirmar",
        "Equivalência obtida somente após correção; discrepâncias maiores no inverno e acima de 30 µg/m³; fatores geralmente entre 1,0 e 1,3",
        "Estação, concentração, composição e fator de correção",
        "Foram necessários fatores sazonais; a relação se deteriorou em concentrações maiores.",
        familia="ARMAAG — campanha de Gdańsk distinta de RSL-001",
    ),
}


def excel_column(number):
    letters = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters


def xml_cell(value, row, column, style=1):
    coordinate = f"{excel_column(column)}{row}"
    text_value = "" if value is None else str(value)
    preserve = ' xml:space="preserve"' if text_value[:1].isspace() or text_value[-1:].isspace() else ""
    return (
        f'<c r="{coordinate}" t="inlineStr" s="{style}">'
        f'<is><t{preserve}>{escape(text_value)}</t></is></c>'
    )


def worksheet_xml(table, widths):
    values = [list(table.columns)] + table.fillna("").astype(str).values.tolist()
    rows = []
    for row_number, values_row in enumerate(values, start=1):
        style = 2 if row_number == 1 else 1
        cells = "".join(
            xml_cell(value, row_number, column_number, style)
            for column_number, value in enumerate(values_row, start=1)
        )
        height = ' ht="38" customHeight="1"' if row_number == 1 else ""
        rows.append(f'<row r="{row_number}"{height}>{cells}</row>')

    columns = "".join(
        f'<col min="{index}" max="{index}" width="{width}" customWidth="1"/>'
        for index, width in enumerate(widths, start=1)
    )
    last_column = excel_column(len(table.columns))
    last_row = len(table) + 1
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>
  <sheetFormatPr defaultRowHeight="15"/>
  <cols>{columns}</cols>
  <sheetData>{''.join(rows)}</sheetData>
  <autoFilter ref="A1:{last_column}{last_row}"/>
</worksheet>'''


def write_xlsx(path, sheets):
    workbook_sheets = "".join(
        f'<sheet name="{escape(name)}" sheetId="{index}" r:id="rId{index}"/>'
        for index, (name, _, _) in enumerate(sheets, start=1)
    )
    workbook_relationships = "".join(
        f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{index}.xml"/>'
        for index in range(1, len(sheets) + 1)
    )
    content_overrides = "".join(
        f'<Override PartName="/xl/worksheets/sheet{index}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        for index in range(1, len(sheets) + 1)
    )
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "[Content_Types].xml",
            f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  {content_overrides}
</Types>''',
        )
        archive.writestr(
            "_rels/.rels",
            '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>''',
        )
        archive.writestr(
            "xl/workbook.xml",
            f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>{workbook_sheets}</sheets>
</workbook>''',
        )
        archive.writestr(
            "xl/_rels/workbook.xml.rels",
            f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {workbook_relationships}
  <Relationship Id="rId{len(sheets) + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>''',
        )
        archive.writestr(
            "xl/styles.xml",
            '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="10"/><name val="Calibri"/></font>
    <font><b/><color rgb="FFFFFFFF"/><sz val="10"/><name val="Calibri"/></font>
  </fonts>
  <fills count="3">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill>
  </fills>
  <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="3">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="center"/></xf>
  </cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>''',
        )
        for index, (_, table, widths) in enumerate(sheets, start=1):
            archive.writestr(f"xl/worksheets/sheet{index}.xml", worksheet_xml(table, widths))


def load_included():
    with (TRIAGEM / "triagem_texto_completo.csv").open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    included = [r for r in rows if r["Decisão texto completo"] == "Incluir"]
    ids = {r["ID"] for r in included}
    missing = ids - DATA.keys()
    extra = DATA.keys() - ids
    if missing or extra:
        raise RuntimeError(f"IDs divergentes. Ausentes={sorted(missing)}; extras={sorted(extra)}")
    return included


def main():
    rows = []
    for source in load_included():
        extracted = DATA[source["ID"]]
        row = {
            "ID": source["ID"],
            "Título": source["Título"],
            "Ano da publicação": source["Ano"],
            "Autores": source["Autores"],
            "Periódico/Fonte": source["Periódico/Fonte"],
            "DOI": source["DOI"],
            **extracted,
            "Arquivo-fonte": source["Arquivo analisado"],
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    SAIDA.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAIDA / "extracao_dados.csv", index=False, encoding="utf-8-sig")

    criteria = pd.DataFrame(
        [
            ["Unidade da matriz", "Uma linha por publicação/documento; resultados múltiplos permanecem descritos na mesma linha nesta etapa."],
            ["Dependência", "Estimativas por sítio, estação, instrumento ou correção não devem ser tratadas como independentes."],
            ["Sobreposição", "RSL-086 e RSL-107 pertencem à mesma família PARIES/Pittsburgh; RSL-107 é o relatório mais amplo."],
            ["Subconjuntos", "RSL-020, RSL-021 e RSL-111: usar somente resultados externos. RSL-013: separar aerossol ambiente de concentrado."],
            ["Casos limítrofes", "RSL-002 e RSL-044 requerem decisão explícita sobre a representação da mesma massa de ar; RSL-061 separa validação local e aplicação regional."],
            ["Não informado", "Campos marcados como não informados exigem conferência dirigida antes da síntese quantitativa."],
        ],
        columns=["Regra", "Aplicação"],
    )

    extraction_widths = [
        12, 50, 12, 34, 32, 28, 24, 28, 23, 34, 26, 30, 34, 28, 24, 26, 58,
        38, 58, 40, 42, 38, 40, 50,
    ]
    if len(extraction_widths) != len(df.columns):
        extraction_widths = [24] * len(df.columns)
        extraction_widths[0] = 12
        extraction_widths[1] = 50
    write_xlsx(
        SAIDA / "extracao_dados.xlsx",
        [
            ("Extração", df, extraction_widths),
            ("Regras", criteria, [24, 110]),
        ],
    )

    print(
        f"Geradas {len(df)} linhas em "
        "dados/extracao/extracao_dados.csv e extracao_dados.xlsx"
    )


if __name__ == "__main__":
    main()