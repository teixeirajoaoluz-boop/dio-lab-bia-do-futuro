# Fórmulas de apuração — motor de cálculo RTC

**Fonte:** `C:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\engine.py`
(fiel ao "documento-PADRÃO 06" da Plataforma Bufon & Frasson; base legal: LC 214/2025 arts. 10, 12, 28, 92, 347-350; EC 132/2023 / CF art. 156-A).

Este motor é a camada de **simulação/projeção** (calcula a NF-e representativa de um ano e o
saldo credor anual da empresa). Ele é independente das regras de crédito por aquisição descritas
em `regras-credito-aquisicoes.json` — trabalha em cima de premissas agregadas por empresa/ano,
não linha a linha por fornecedor.

## 1. Tabela de transição de alíquotas (2027-2033)

Para cada ano da janela de transição existe um conjunto fixo de parâmetros:

- **Alíquota CBS** do ano
- **Alíquota IBS** do ano
- **IPI**: sempre 0 a partir de 2027 (salvo Zona Franca de Manaus, fora do escopo deste motor)
- **Fator ICMS**: começa em 100% (2027-2028) e reduz 10 pontos percentuais por ano até
  zerar em 2033 — reflete a extinção gradual do ICMS na transição.

## 2. Montagem da nota fiscal representativa do ano (`montarNotaFiscal`)

Passo a passo, para um valor bruto de venda/aquisição em determinado ano:

1. **Valor bruto**: preço atual, com os tributos antigos embutidos "por dentro".
2. **Base líquida** = valor bruto × (1 − percentual de extração dos tributos antigos).
   A extração-padrão (quando a empresa não fornece a própria) é 14,6728% — proporção histórica
   de PIS + COFINS + ICMS + ISS sobre a receita, extraída do exemplo de referência (ECF 2024
   "Full Comex").
3. **CBS do ano** = base líquida × alíquota CBS do ano (tributo "por fora").
4. **IBS do ano** = base líquida × alíquota IBS do ano (tributo "por fora").
5. **IPI** = 0.
6. **Valor total da NF** = base líquida + CBS + IBS + IPI. Esse valor total é a base sobre a
   qual incide o ICMS residual, em efeito cascata durante a transição.
7. **ICMS residual** = valor total da NF × alíquota efetiva de ICMS da empresa × fator ICMS do
   ano (o fator zera o ICMS residual gradualmente até 2033). A alíquota efetiva-padrão, quando
   não informada, é 6,2162% (ICMS líquido de incentivo INVEST-CE sobre o mercado interno).
8. **Crédito de CBS** = base líquida × percentual de crédito de CBS informado para a operação
   (crédito financeiro pleno, art. 28 da LC 214/2025 — depende de a aquisição gerar direito a
   crédito, conforme as regras de `regras-credito-aquisicoes.json`).
9. **Crédito de IBS** = base líquida × percentual de crédito de IBS informado.

### Dois cenários de leitura do resultado

- **Cenário 1 — Carga bruta (só débito, sem compensar crédito)**:
  `carga_bruta = CBS do ano + IBS do ano + ICMS residual`
  Mostra o total do "destaque fiscal" na nota, sem abater o que a empresa tem direito a
  recuperar como crédito.

- **Cenário 2 — Posição líquida (débito menos crédito)**:
  `posicao_liquida = ICMS residual + (CBS do ano − crédito de CBS) + (IBS do ano − crédito de IBS)`
  Se o resultado for negativo, a empresa está em posição credora (mais crédito do que débito)
  naquela operação.

## 3. Saldo credor anual da empresa (`saldoCredorAnual`)

Sobe o cálculo do nível "uma operação" para o nível "empresa no ano", a partir de uma receita
tributada agregada e dos créditos acumulados de CBS/IBS:

1. **Débito de CBS do ano** = receita tributada × alíquota CBS do ano.
2. **Débito de IBS do ano** = receita tributada × alíquota IBS do ano.
3. **Saldo credor de CBS** = máximo entre 0 e (crédito de CBS acumulado − débito de CBS do ano).
   Ou seja: só existe saldo credor de CBS se o crédito acumulado superar o débito do ano;
   caso contrário, o saldo credor é zero (não vira número negativo/dívida aqui).
4. **Saldo credor de IBS** = máximo entre 0 e (crédito de IBS acumulado − débito de IBS do ano).
5. **Saldo credor total** = saldo credor de CBS + saldo credor de IBS.
6. **Posição líquida da empresa no ano** =
   (receita tributada × fator ICMS do ano × alíquota efetiva de ICMS) − saldo credor total.

Em linguagem de negócio:

- **Valor a recolher** de IBS/CBS surge quando o débito do ano é maior que o crédito
  acumulado — a diferença positiva é o valor a pagar (o "saldo credor" fica em zero, pois não
  há excedente de crédito).
- **Valor a recuperar/crédito acumulado (saldo credor)** surge quando o crédito acumulado é
  maior que o débito do ano — a diferença positiva vira saldo credor a compensar ou recuperar
  em períodos futuros.

## 4. Observação importante — dependência não documentada nas fontes lidas

O comentário do próprio `engine.py` indica que, **em produção**, os débitos/créditos/saldo do
Cenário 2 (posição líquida) e do saldo credor anual normalmente **não são recalculados por esta
fórmula de referência**: eles vêm diretamente de uma "memória 08" — uma série anual de premissas
(`premissas.serie_anual`) mantida em outro componente da plataforma. A fórmula documentada acima
é usada como **cálculo de validação/fallback**, para conferir a memória 08 ou substituí-la quando
ela não estiver disponível.

Essa tabela/estrutura de `premissas.serie_anual` **não foi encontrada** nos arquivos SQL lidos
para este levantamento (`34a_regras_negocio_projecoes_aquisicoes.sql`, `34_criar_tabela_projecoes_acquisitions.sql`,
`37_criar_tabela_projecoes_acquisitions_contabil.sql`, `27_criar_tabela_consolidated_acquisitions.sql`,
`22_criar_tabela_consolidated_revenues.sql`). Fica registrada aqui como **dependência externa
não documentada** — não foi inventada nenhuma estrutura para ela.
