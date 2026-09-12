# Regimes Específicos — Bloco 2

Setores com **sistemática própria** de apuração, base de cálculo ou crédito de IBS/CBS — diferente
da regra geral (arts. 12-15 base de cálculo, arts. 28-47 não cumulatividade plena). Não são apenas
alíquotas reduzidas: cada um destes 13 segmentos altera a **mecânica de cálculo** em algum ponto
(base líquida, monofasia, crédito presumido, redução com crédito assimétrico etc.).

Distinto dos "Regimes Diferenciados" (bloco 1, reduções de alíquota sem mudança de mecânica) e dos
"Regimes Aduaneiros Especiais" (bloco 3, específico de importação).

Todas as citações abaixo foram confirmadas contra o **texto oficial consolidado da LC 214/2025**
("norma atualizada", já com as alterações da LC 227/2025), publicado pelo Centro de Documentação e
Informação da Câmara dos Deputados:
`https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf`

| # | Pasta | Resumo (1 linha) | Mecânica diferenciadora | Artigo confirmado | Status |
|---|---|---|---|---|---|
| 01 | `01-combustiveis-biocombustiveis` | Tributação monofásica de combustíveis | Cobrança concentrada em 1 elo; veda crédito na revenda; base por unidade de medida | art. 172-180 | Confirmado — faixa legal do diferencial biocombustível (40%-90% da alíquota do fóssil) achada no art. 175 §1º |
| 02 | `02-servicos-financeiros` | Bancos, seguros, fundos — base sobre receitas/margem | Base = receitas/spread/tarifas, não valor bruto movimentado | art. 181-233 | Confirmado — cronograma de alíquotas real no art. 233 (10,85% em 2027-28 até 12,50% em 2033) |
| 03 | `03-planos-assistencia-saude` | Operadoras de saúde — base sobre prêmio líquido de sinistro | Base = prêmios + receita financeira de reservas − indenizações pagas | art. 234-243 | Confirmado — redução de 60% no art. 237 |
| 04 | `04-concursos-prognosticos-apostas` | Loterias e bets — base sobre receita própria | Base = arrecadação − premiações − destinações obrigatórias | art. 244-250 | Confirmado — percentual exato de alíquota no art. 246 continua sem previsão numérica na lei (lacuna real, não de pesquisa) |
| 05 | `05-bens-imoveis` | Incorporação/locação — redutores de base e tributação por fluxo | Redutor de Ajuste (arts. 257-258) + Redutor Social (arts. 259-260); redução geral de 50% (art. 261 caput) e de 70% para locação (art. 261 parágrafo único) | art. 251-265 | Confirmado |
| 06 | `06-agropecuaria-pesca-florestas-extrativismo` | Produtor rural — crédito presumido ao adquirente + redução de 60% | Crédito presumido via fórmula `CP=(VO×C)/(1+C)` (coeficiente `C` de ato anual) | art. 164-168 | Confirmado — coeficiente `C` continua dependendo de ato infralegal anual não publicado |
| 07 | `07-sociedades-cooperativas` | Ato cooperativo com alíquota zero (regime opcional) | Alíquota zero associado↔cooperativa; operações com terceiros seguem regime geral | art. 271-272 | Confirmado |
| 08 | `08-hotelaria-parques-diversao-tematicos` | Hotéis/parques — redução de alíquota com crédito assimétrico | Crédito pleno ao prestador, débito a 40% da alíquota (art. 281) | art. 277-283 | Confirmado |
| 09 | `09-bares-restaurantes` | Alimentação preparada — redução de alíquota | Mesma lógica de crédito-cheio/débito a 40% (art. 275) de hotelaria | art. 273-276 | Confirmado |
| 10 | `10-agencias-viagem-operadoras-turismo` | Agências — base sobre comissão líquida de repasses | Base = valor cobrado − repasses a fornecedores intermediados; mesma alíquota de hotelaria (art. 289, II) | art. 288-291 | Confirmado |
| 11 | `11-zona-franca-manaus-alc` | ZFM/ALC — alíquota zero + crédito presumido industrial | Alíquota zero em operações específicas; crédito presumido não espelha débito do fornecedor | art. 439 (ZFM) / art. 458 (ALC) | Confirmado — percentual de crédito presumido depende de ato infralegal |
| 12 | `12-simples-nacional` | Aponta para base já existente (`simples-nacional/`) | Creditamento restrito do tomador: adquirente no regime regular credita-se em montante equivalente ao devido pelo fornecedor no DAS | **art. 47, § 9º, inciso II** | Corrigido — art. 127 (citado antes) não tem relação com SN, é a Redução de 30% para 18 profissões regulamentadas |
| 13 | `13-transporte-coletivo-intermunicipal-interestadual` | Transporte rodoviário/ferroviário/hidroviário/aéreo entre municípios/estados | Art. 285 (urbano dentro da seção): 100% redução + vedação total de crédito; arts. 286-287 (intermunicipal/interestadual/aéreo regional): 40% de redução cada | art. 284-287 | Confirmado — achado nesta rodada, distinto do transporte urbano do bloco 1 (art. 157, isenção) |

## Achado metodológico (resolvido em 2026-08-27)

Na primeira rodada (pesquisa via RAG local), 3 dos 12 segmentos originais (financeiros, imóveis,
agropecuária) tinham numeração de artigo divergente do mapa pré-existente
(`fontes-legais/mapa-lc214-artigos.json`), sem confirmação possível porque o fetch direto ao
Planalto falhava. Numa segunda rodada, o texto oficial consolidado foi obtido via Câmara dos
Deputados (URL acima) e usado para confirmar, artigo por artigo, todos os 13 segmentos deste bloco
— inclusive um quarto erro que só apareceu nesta correção: a citação do art. 127 para o
creditamento restrito do Simples Nacional (segmento 12) estava errada; o artigo correto é o art.
47, § 9º, inciso II. `fontes-legais/mapa-lc214-artigos.json` foi corrigido nos 3+1 pontos.

## Fontes usadas neste bloco

- Texto oficial consolidado da LC 214/2025 (Câmara dos Deputados, URL acima) — fonte primária desta rodada de correção.
- MCP `mcp-rag-reforma` (`buscar_reforma`, `aprofundar_documento`) — usado na rodada de pesquisa original, antes da fonte oficial estar disponível.
- Projeto irmão `C:\Projetos Tecnologicos\01_Projeto BUFON & FRASSON RTC\PROJETO TECNOLOGICO\` — motor de cálculo real do crédito presumido de produtor rural (segmento 06).
- `simples-nacional/` e `aliquotas-transicao/` (raiz de `GUERRA_MENTORIA_REGRAS RTC`) — referenciados no segmento 12 e usados como base de alíquotas do regime geral nos exemplos numéricos.

## Lacunas conhecidas do bloco (residuais, estruturais — não de pesquisa)

1. Coeficiente `C` do crédito presumido de produtor rural (segmento 06) e percentual de crédito presumido da ZFM (segmento 11) dependem de atos infralegais anuais ainda não publicados.
2. Percentual de alíquota do art. 246 (concursos de prognósticos) não está definido na própria lei — depende de regulamento.
3. Nenhum MCP de jurisprudência foi consultado — lei recente demais para haver litígio consolidado.
4. Anexos citados por remissão (não transcritos integralmente) em vários segmentos.
