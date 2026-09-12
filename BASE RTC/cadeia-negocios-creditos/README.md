# Cadeia de negócios — crédito de IBS/CBS nas aquisições (Guerra RTC)

Base de conhecimento canônica sobre como a plataforma Guerra RTC (Bufon & Frasson) decide o
tratamento de crédito de IBS/CBS de cada aquisição ao longo da cadeia — fornecedor por
fornecedor, produto por produto — e como o motor de cálculo transforma isso em débito, crédito,
valor a recolher e valor a recuperar.

## 1. Como a plataforma decide a alíquota/crédito de cada aquisição

A decisão acontece por aquisição individual (linha de compra), na tabela de projeções
`PROJETOBEF.projecoes_acquisitions` (origem fiscal, SPED Fiscal/Contribuições/XML — ver
estrutura em `backend/base_sql/34_criar_tabela_projecoes_acquisitions.sql`). A lógica de decisão
está formalizada como 3 regras de negócio numeradas em
`backend/base_sql/34a_regras_negocio_projecoes_aquisicoes.sql`, persistidas na tabela
`PROJETOBEF.regras_negocio_projecoes_aquisicoes` (estruturadas em JSON em
`regras-credito-aquisicoes.json` neste diretório). Em prosa:

1. **Fornecedor optante do Simples Nacional** (`optanteSimplesNacional_suppl = SIM`):
   a plataforma ignora a alíquota padrão de transição do ano e usa as alíquotas específicas do
   Simples Nacional do próprio fornecedor (vindas de `suppliers` / `aliquota_sn_ibs_cbs`, por
   anexo e por ano — colunas do tipo `cbs_2027_2028`, `ibs_2029`, etc.). Isso reflete que o
   crédito de IBS/CBS gerado por uma compra de fornecedor do Simples segue regra própria
   (recolhimento simplificado), diferente do regime regular.

2. **Fornecedor fora do Simples Nacional, com o produto/serviço cadastrado** (`products`):
   a plataforma usa a alíquota aplicada padrão do ano (`ibs_apl`/`cbs_apl` de
   `aliquotas_transicao`), mas desconta a redução específica cadastrada para aquele
   produto/serviço (`reducao_ibs`, `reducao_cbs`) — ou seja, produtos com benefício fiscal
   próprio (ex.: cesta básica, medicamentos, etc.) reduzem a alíquota-base do ano.

3. **Fornecedor fora do Simples Nacional, produto/serviço não cadastrado**: a plataforma cai no
   **padrão de referência do ano** puro — `ibs_apl`/`cbs_apl` de `aliquotas_transicao`, com
   redução 0. É o comportamento "default" quando não há informação mais específica disponível.

Note a hierarquia de precedência implícita: regime do fornecedor (Simples ou não) decide
primeiro; dentro do regime "fora do Simples", o cadastro do produto decide se há redução
específica ou se cai no padrão do ano.

O resultado de cada regra alimenta as colunas de percentual/valor de IBS e CBS por ano
(2027 a 2033) da tabela `projecoes_acquisitions` — a mesma lógica existe em versão "origem
contábil" na tabela `PROJETOBEF.projecoes_acquisitions_contabil`
(`backend/base_sql/37_criar_tabela_projecoes_acquisitions_contabil.sql`), que parte do
balancete contábil (`vl_aquisicao`, `pct_red_ibs`, `pct_red_cbs`) em vez de nota fiscal/SPED —
ambas convergem, mais adiante, para a mesma tabela de consolidação de aquisições
`PROJETOBEF.consolidated_acquisitions` (`backend/base_sql/27_criar_tabela_consolidated_acquisitions.sql`),
que guarda o valor da operação (`vl_opr`), o CFOP e a origem do dado (SPED Fiscal, SPED
Contribuições, XML ou planilha) — o espelho do lado da receita é
`PROJETOBEF.consolidated_revenues` (`backend/base_sql/22_criar_tabela_consolidated_revenues.sql`).

## 2. Como o motor de cálculo transforma isso em débito, crédito e saldo (engine.py)

Uma vez definida a alíquota/percentual de crédito aplicável a cada aquisição (passo 1), o motor
de cálculo em `C:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\engine.py`
simula o efeito de IBS/CBS numa nota fiscal representativa do ano, e depois no saldo anual da
empresa. Em linguagem de negócio (detalhamento passo a passo em `formulas-apuracao.md`):

- **Débito de IBS/CBS**: o tributo que incide "por fora" sobre a base líquida de uma
  venda/receita, calculado com a alíquota de transição do ano (tabela fixa 2027→2033, definida
  no próprio motor com base na LC 214/2025).
- **Crédito fiscal (financeiro pleno, art. 28 LC 214/2025)**: a parcela da base líquida da
  aquisição sobre a qual a empresa tem direito a se creditar — o percentual de crédito é o
  próprio resultado das 3 regras do item 1 acima (quanto a aquisição "vale" de crédito depende
  de o fornecedor ser do Simples, do produto ter redução cadastrada, ou do padrão do ano).
- **Crédito contábil**: no motor, é a mesma mecânica de crédito financeiro aplicada quando a
  origem do dado é contábil (balancete) em vez de fiscal (SPED/XML) — ver
  `projecoes_acquisitions_contabil` no item 1.
- **Valor a recolher**: quando o débito do ano supera o crédito acumulado, a diferença positiva
  é o que a empresa deve pagar de IBS/CBS.
- **Valor a recuperar (saldo credor)**: quando o crédito acumulado supera o débito do ano, a
  diferença positiva vira saldo credor — a compensar ou recuperar em períodos seguintes.

O motor também simula o **ICMS residual** durante a transição (ele não desaparece de uma vez —
seu peso cai gradualmente, de 100% em 2027-2028 até 0% em 2033), e oferece duas leituras do
resultado: a "carga bruta" (só débito, sem abater crédito) e a "posição líquida" (débito menos
crédito, podendo indicar posição credora).

## 3. Ponto de atenção — dependência não documentada

O próprio `engine.py` deixa registrado que, em produção, o cálculo de débito/crédito/saldo por
ano normalmente vem pronto de uma "memória 08" (`premissas.serie_anual`), e que a fórmula acima é
usada apenas como cálculo de validação/fallback. Essa tabela de premissas **não foi encontrada**
nos scripts SQL lidos para este levantamento — ver detalhes e ressalva completa no fim de
`formulas-apuracao.md`.

## Arquivos deste diretório

- `regras-credito-aquisicoes.json` — as 3 regras de crédito por aquisição, estruturadas.
- `formulas-apuracao.md` — fórmulas do motor de cálculo, passo a passo, em linguagem de negócio.
- `README.md` — este arquivo.

## Fontes lidas

- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\34a_regras_negocio_projecoes_aquisicoes.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\34_criar_tabela_projecoes_acquisitions.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\37_criar_tabela_projecoes_acquisitions_contabil.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\27_criar_tabela_consolidated_acquisitions.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\22_criar_tabela_consolidated_revenues.sql`
- `c:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\engine.py`
