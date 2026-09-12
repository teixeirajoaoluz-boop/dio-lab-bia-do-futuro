# Glossário de Fórmulas — Sistema Guerra RTC

## Propósito

Este glossário é o dicionário canônico de **todos os campos calculados e mapeamentos de
colunas** usados na plataforma Guerra RTC (planejamento da Reforma Tributária — IBS/CBS).
Cada entrada documenta, para uma coluna de uma tabela do banco, sua **sigla curta** (usada
internamente em fórmulas e telas) e, quando aplicável, a **expressão/regra de cálculo**
(`expressao_texto`) que gera aquele valor — débito, crédito, saldo, alíquota aplicada,
percentual de redução, projeção de receita/aquisição, etc.

- **Fonte original**: `00_banco_AWS/GLOSSARIO FORMULAS.csv` (planilha mantida manualmente).
- **Schema de referência**: `backend/base_sql/01_create_table_formulas_glossario.sql`
  (tabela `formulas_glossario`: `tabela`, `coluna`, `sigla`, `expressao_texto`, `descricao`,
  `entradas`, `autor`, `versao`).
- **Transcrição**: `glossario-formulas.json` é uma cópia fiel, linha a linha, do CSV. O CSV
  atual só preenche 4 das 8 colunas do schema (`tabela`, `coluna`, `sigla`,
  `expressao_texto` — mapeada da coluna "FÓRMULA" do CSV); `descricao`, `entradas`, `autor`
  e `versao` não existem hoje no CSV e aparecem como `null` no JSON.

Este arquivo não interpreta nem completa fórmulas ausentes — muitas siglas existem apenas
como *mapeamento de nome de coluna* (sem lógica de cálculo), o que é normal para campos de
entrada (dados brutos importados) em vez de campos derivados.

## Estrutura do JSON

Cada objeto em `glossario-formulas.json` tem exatamente estes campos:

```json
{
  "tabela": "receita_projecao",
  "coluna": "valor_ibs_2027",
  "sigla": "vl_ibs_27",
  "expressao_texto": "vl_opr_27 * pct_ibs_27",
  "descricao": null,
  "entradas": null,
  "autor": null,
  "versao": null
}
```

## Domínios (tabelas) cobertos

| Tabela | Nº de campos | Descrição |
|---|---|---|
| `aliquotas_transicao` | 8 | Alíquotas referenciais e aplicadas de CBS, IBS, ICMS e ISS ao longo da transição da reforma (por sigla: `*_ref` = referencial, `*_apl` = aplicada). |
| `premissas_taxa de crescimento` | 2 | Premissas de taxa de crescimento por ano (`ptc_ano`, `ptc_tx_crescimento`) — insumo usado nas projeções de receita/aquisição. |
| `products` | 11 | Cadastro de produtos/itens: código, descrição, unidade, NCM, alíquota ICMS, CST, classificação tributária, percentuais de redução de IBS/CBS, anexo do Simples. |
| `consolidated_revenues` | 3 | Receita consolidada por data/item (`vl_opr` = valor da operação) — base histórica antes da projeção. |
| `receita_projecao` | 39 | Projeção de receita ano a ano (2027 em diante): valor da operação projetado, percentuais e valores de IBS/CBS aplicados, com fórmulas de recorrência (ex.: `vl_opr_27 = vl_opr + (vl_opr * ptc_tx_crescimento[2027])`; `vl_ibs_27 = vl_opr_27 * pct_ibs_27`). Maior domínio do glossário — concentra a lógica de projeção de débito tributário sobre receitas. |
| `aquisicoes_origem_fiscal` | 13 | Aquisições de fornecedores com sua origem fiscal (data, participante, fornecedor, regime Simples Nacional, etc.) — insumo para cálculo de crédito. |
| `projecoes-acquisitions` | 57 | Projeção de aquisições (créditos) ano a ano, espelhando a lógica de `receita_projecao` mas para o lado de crédito/fornecedores (nome, CNPJ/CPF, Simples Nacional, valores e percentuais projetados de IBS/CBS por aquisição). |
| `suppliers` | 19 | Cadastro de fornecedores (nome, CNPJ/CPF, opção pelo Simples Nacional, demais atributos usados nas projeções de crédito). |
| `plano_contas` | 7 | Plano de contas contábil (natureza, indicador de conta, nível, código da conta) — base para o cruzamento fiscal-contábil. |
| `balancete_contas_resultado` | 4 | Balancete de contas de resultado (data, conta contábil, valor, indicador débito/crédito) — dado contábil bruto usado nas projeções contábeis. |
| `projecoes-acquisitions-contabil` | 36 | Versão contábil da projeção de aquisições: valores e percentuais de IBS/CBS por conta contábil, condicionados a "geração de crédito/débito = SIM" na tabela de origem. |

## Convenções de sigla observadas

- Sufixo `_ref` / `_apl`: alíquota referencial vs. aplicada (transição da reforma).
- Sufixo `_27`, `_28`, ...: ano de projeção (2027, 2028, ...).
- Prefixo `pct_`: percentual; `vl_`: valor monetário; `dsc_`: descrição; `cod_`/`cod_itm`: código de item.
- Expressões do tipo "Igual a X" ou "igual a X_outra_tabela" indicam **campo copiado/lookup**
  de outra tabela (ex.: `receita_projecao.pct_red_ibs` é o `red_ibs` de `products`,
  localizado pelo `cod_itm_srv`), não um cálculo novo.
- Expressões com colchetes (`ibs_apl[2027]`) indicam que o valor é buscado na tabela
  `aliquotas_transicao` para o ano específico entre colchetes.

## Limitações conhecidas da fonte

- Nenhuma linha do CSV preenche `descricao`, `entradas`, `autor` ou `versao` — o schema SQL
  suporta esses campos, mas eles não foram populados na planilha até o momento da
  transcrição.
- 61 das 199 linhas têm `expressao_texto` vazio (campos de entrada/importação direta, sem
  fórmula de cálculo associada).
