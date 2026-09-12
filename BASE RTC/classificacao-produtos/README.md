# Classificação Fiscal de Produtos — Guerra RTC

Base de conhecimento canônica sobre como a plataforma Guerra RTC classifica produtos
para fins de IBS/CBS (Reforma Tributária, LC 214/2025). Cobre o modelo geral
(NCM → CST → cClassTrib) e o módulo especializado de classificação farmacêutica.

## 1. O papel do NCM, CST e cClassTrib na plataforma

A plataforma trata a classificação tributária de um produto como uma cadeia de três
campos, armazenados por NCM na tabela `ncm_tributacao_rtc` (ver
`ncm-tributacao-rtc.md` para a estrutura completa):

- **NCM/NBS** — identifica o produto (Nomenclatura Comum do Mercosul) ou o serviço
  (Nomenclatura Brasileira de Serviços). É a chave de busca: dado um NCM, a
  plataforma resolve o tratamento tributário do IBS/CBS.
- **CST** (Código de Situação Tributária) — indica o *regime* aplicável ao item
  (tributação integral, redução, alíquota zero, etc.) no novo modelo do IBS/CBS.
- **cClassTrib** (Código de Classificação Tributária) — é o código mais granular:
  aponta para a hipótese específica de tratamento diferenciado (qual anexo da
  LC 214/2025, qual redução, qual regra) associada àquele NCM/CST. É o campo que a
  nota fiscal eletrônica efetivamente carrega para o Fisco identificar o benefício
  aplicado.

A relação é hierárquica: o NCM identifica o produto, o CST classifica o regime
geral, e o cClassTrib desambigua a regra específica dentro daquele regime (ex.: "CST
200 aplicado por conta do Anexo XIV" vs. "CST 200 aplicado por conta do Anexo IV").
Além desses três campos, a tabela guarda `reducao_ibs` e `reducao_cbs` (percentual
de redução da alíquota, já numérico) e `anexo` (qual anexo da LC 214/2025 fundamenta
o tratamento — ex.: Anexo 14 para medicamentos). Fonte: estrutura da tabela em
`c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\07_criar_tabela_ncm_tributacao_rtc.sql`.

### Como a base é alimentada

A tabela é populada a partir de um CSV mestre (`CAD_NCM_CST_CCLASSTRIB.csv`), que
contém a associação NCM ↔ CST ↔ cClassTrib ↔ reduções ↔ anexo ↔ legislação, curada
manualmente fora do repositório. O script de carga (script 13) apenas lê, normaliza
e insere esse CSV nos schemas `rtc_poc` e `rtc_prod` — **não define nenhuma regra de
classificação por si mesmo**, apenas mecânica de ETL (batches de 500, tratamento de
encoding, conversão de vírgula decimal). Fonte:
`c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\13_popular_ncm_tributacao_rtc.py`.

O script `consultar_anexo14_ncm.py` mostra o único ponto onde uma regra de negócio
aparece explicitamente no código: ele filtra a tabela por `anexo = '14'` e resume
as combinações de `reducao_ibs`/`reducao_cbs` encontradas, com a nota de que o
**Anexo 14 (Fornecimento de medicamentos) tem fundamento no art. 146 da LC 214/2025**.
Fonte: `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\consultar_anexo14_ncm.py`.

O script `verificar_ncm_populado.py` é só uma checagem de saúde (contagem de
registros e de NCMs distintos por schema, esperando ~3.487 registros) — não contém
regra de classificação. Fonte:
`c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\verificar_ncm_populado.py`.

**Lacuna identificada**: nenhum dos scripts SQL/Python do Guerra RTC contém, embutida
no código, a tabela de mapeamento NCM → CST/cClassTrib — ela vive inteiramente no
CSV externo `01_api_participantes/DADOS BASE/CAD_NCM_CST_CCLASSTRIB.csv`, que não
foi lido nesta tarefa (é dado tabular externo, não regra de código) e cujo conteúdo
completo não está documentado aqui. Qualquer regra de negócio sobre *qual* NCM cai em
qual CST/cClassTrib/anexo está nesse CSV, não no código-fonte.

## 2. Classificação farmacêutica (módulo FARMA)

Fonte: `C:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\farma.py`.

Esse módulo é um motor separado, mais rico que a tabela genérica de NCM: ele resolve
o problema de que uma farmácia vende um **mix de produtos** (medicamentos,
dispositivos médicos, perfumaria/conveniência) e cada categoria tem tratamento
tributário diferente no IBS/CBS. O motor classifica cada item em um de 4 "baldes"
e depois calcula a alíquota efetiva **mesclada** (blended) desse mix, ano a ano, ao
longo da transição 2027-2033.

### 2.1 Os 4 baldes tributários

| Balde | Rótulo | Redução | Base legal |
|---|---|---|---|
| `medicamento_zero` | Medicamento — alíquota zero (Anexo XIV) | 100% (zero) | LC 214/2025, medicamentos do Anexo XIV |
| `medicamento_60` | Medicamento ANVISA / manipulado | 60% | LC 214/2025, medicamentos registrados na ANVISA ou manipulados |
| `dispositivo_60` | Dispositivo médico (Anexo IV) | 60% | LC 214/2025, dispositivos médicos do Anexo IV |
| `cheio` | Não-medicamento (HPC/perfumaria/conveniência) | 0% (alíquota padrão) | LC 214/2025, regra geral |

Os valores exatos (incluindo os placeholders de cClassTrib marcados no próprio
código como "confirmar na tabela oficial") estão em `regras-farma.json`.

### 2.2 Regra de decisão (ordem de precedência)

Ao classificar um item (dado seu NCM e/ou descrição), o motor testa, nesta ordem,
até a primeira regra que casar:

1. **Anexo XIV por nome de princípio ativo** — se algum token da lista oficial de
   382 princípios ativos do Anexo XIV (ou seu "nome-núcleo" sem prefixo de sal, ex.:
   "cloridrato de X" → compara só "X"; ou um componente de uma combinação, ex.:
   "rifampicina + isoniazida" → compara "rifampicina" e "isoniazida"
   separadamente) aparecer na descrição do produto → **medicamento_zero**,
   confiança "regra".
2. **Vacina/soro por NCM** — se o NCM começar com 3002.2, 3002.41 ou 3002.42
   (vacinas/soros de uso humano) → **medicamento_zero**, confiança "regra", mesmo
   sem bater por texto.
3. **Medicamento por NCM** — se o NCM começar com 3003 ou 3004 (capítulo 30,
   medicamentos em geral) → **medicamento_60** (presunção de registro ANVISA),
   confiança "regra".
4. **Manipulado por texto** — se a descrição contiver "manipul", "fórmula"/"formula"
   ou "magistral" → **medicamento_60** (farmácia de manipulação), confiança "regra".
5. **Dispositivo médico por NCM** — se o NCM começar com 3005, 3006, 9018, 9019,
   9021 ou 9022 → **dispositivo_60**, mas com confiança **"heuristica"** (o próprio
   motor sinaliza que esses NCMs não garantem enquadramento no Anexo IV — precisa de
   revisão manual, ao contrário de todas as outras regras que retornam confiança
   "regra").
6. **Default** — nada bateu → **cheio** (não-medicamento: HPC, perfumaria,
   conveniência), alíquota padrão, confiança "regra".

A distinção "regra" vs. "heurística" no campo `confianca` é o sinalizador que a
plataforma usa para indicar quais classificações devem ser revisadas manualmente
antes de compor um dossiê ou parecer.

### 2.3 Cálculo do comportamento tributário (alíquota efetiva mesclada)

Depois de classificar cada item de uma lista de produtos (ponderando por
faturamento), o motor consolida um **mix** (participação de cada balde no
faturamento total) e projeta o comportamento ano a ano na janela de transição
2027-2033 (tabela de alíquotas CBS/IBS herdada do motor geral `engine.py`):

- `aliquota_referencia(ano)` = CBS(ano) + IBS(ano), a alíquota-padrão cheia do ano,
  sem nenhuma redução.
- `efetiva_balde(ano)` = `aliquota_referencia(ano) × (1 − redução_do_balde)`.
- `blended(ano)` = soma, para cada balde presente no mix, de
  `share_do_balde × efetiva_balde(ano)`.

A série anual também calcula receita projetada (com crescimento anual composto),
débito de IBS/CBS, crédito (proporcional a um parâmetro `razao_credito` informado
pelo usuário — tipicamente <1, já que uma farmácia é estruturalmente devedora) e a
posição líquida a pagar. A tabela de alíquotas de transição usada está reproduzida
em `regras-farma.json`.

### 2.4 Mudanças de regime que o motor documenta (notas operacionais)

O módulo carrega quatro notas operacionais fixas, reaplicadas em dossiês e
revisões, que resumem o que muda estruturalmente para uma farmácia no IBS/CBS:

1. **Fim do ICMS-ST do medicamento** — hoje o ICMS é retido por substituição
   tributária no distribuidor; no IBS/CBS não há ST: cada etapa da cadeia debita e
   credita separadamente, mudando precificação e fluxo de caixa do imposto.
2. **Fim do PIS/COFINS monofásico** — hoje a indústria concentra o PIS/COFINS e a
   drogaria revende com alíquota zero; no IBS/CBS a farmácia passa a ter débito em
   cada venda (compensado pelo crédito da compra).
3. **Não-cumulatividade plena** — a farmácia passa a poder creditar IBS/CBS de
   mercadorias, energia, aluguel, ERP, maquininha e fretes; o imposto recai apenas
   sobre o valor agregado.
4. **Benefício de 60%/zero é condicionado** — só vale enquanto a indústria/importador
   cumprir a regulação de preços da CMED ou o compromisso firmado com a União e o
   CGIBS. Isto é, a redução não é uma característica fixa do NCM: depende de
   conformidade regulatória de terceiros na cadeia.

### 2.5 O que NÃO está no repositório (lacunas explícitas)

- Os códigos `cClassTrib` definitivos para os baldes `medicamento_zero`,
  `medicamento_60` e `dispositivo_60` **não estão definidos** — o próprio
  código-fonte os marca como placeholder ("confirmar na tabela oficial"). Só o
  balde `cheio` tem cClassTrib fechado (`000001`).
- Não há, no módulo FARMA nem nos scripts do Guerra RTC lidos, nenhuma menção a
  **substituição tributária remanescente** para farma no IBS/CBS — pelo contrário,
  a nota operacional nº 1 afirma explicitamente que a ST acaba.
- Não há menção a regime de **cesta básica** no módulo farma.py — o regime
  documentado para farma é especificamente o do Anexo XIV/Anexo IV (saúde), distinto
  do regime de cesta básica nacional (que é tratado, se existir, em outro módulo não
  lido nesta tarefa).
  - Se a plataforma tiver uma tabela de cesta básica separada, ela não faz parte do
    escopo desta pesquisa (não foi apontada como fonte pela tarefa).
- O conteúdo completo do CSV `CAD_NCM_CST_CCLASSTRIB.csv` (a fonte real de
  NCM→CST/cClassTrib para todo o resto da plataforma, fora do farma) não foi lido
  nem extraído — é dado externo, não está versionado como regra de código nos
  scripts analisados.
