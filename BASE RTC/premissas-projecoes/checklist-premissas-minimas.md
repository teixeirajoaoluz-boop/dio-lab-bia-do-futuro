# Checklist — Premissas Mínimas Antes de Rodar uma Projeção

> Extraído das regras de validação reais em `premissas.py` (mcp-planejamento-RTC)
> e da estrutura das tabelas SQL do Guerra RTC. Onde não há regra de validação
> em código para algo pedido na tarefa original (sazonalidade, cronograma de
> transição como campo explícito), isso é marcado como "sem validação
> automática encontrada" — não foi inventada uma regra para preencher o vazio.

## A) Obrigatório e validado em código (`premissas.py`, função `validar()`)

- [ ] **`ecf.mercado_interno` preenchido e diferente de zero.**
      Se zero, `calcular_derivados()` lança `ValueError` — bloqueia qualquer
      cálculo de derivados. (linhas 23-24)
- [ ] **`ecf.exportacao + ecf.mercado_interno` ≈ `ecf.receita_bruta`** (tolerância
      de até 5% de divergência). Acima disso, entra como problema de validação.
      (linhas 57-63)
- [ ] **Se `derivados.extracao_art12` e/ou `derivados.icms_efetivo` vierem
      preenchidos no JSON**, eles precisam bater com o recálculo a partir da
      `ecf` (tolerância `1e-4`). Nunca aceitar valor "herdado" de outra empresa
      ou período. (linhas 64-71)
- [ ] **`serie_anual` cobre todos os anos de 2027 a 2033**, sem nenhum ano
      faltando. (linhas 73-77)
- [ ] **Schema estrutural**: `premissas.json` valida contra o JSON Schema em
      `premissas.schema.json` (caminho padrão no Drive:
      `G:\Meu Drive\Projetos de Execução\MCP\mcp-planejamento-RTC\premissas.schema.json`).
      Se o arquivo de schema não existir no caminho configurado, ou se a
      biblioteca `jsonschema` não estiver instalada, essa etapa é pulada e
      reportada como aviso — **não bloqueia**, mas deveria ser corrigido antes
      de considerar a validação completa. (linhas 39-52)

> Todas as violações acima entram na lista `_validacao` (nunca uma exceção
> fatal, exceto o `ValueError` de `mercado_interno == 0`). Uma projeção pode
> tecnicamente rodar com a lista não-vazia — mas isso significa que os dados de
> entrada não passaram no contrato mínimo da plataforma.

## B) Estruturalmente obrigatório pelo banco Guerra RTC (constraints SQL)

- [ ] **Toda linha de `receita_projecao` precisa ter `receita_id` apontando
      para uma `consolidated_revenues` existente** (FK, `NOT NULL`, `UNIQUE`) —
      ou seja, não é possível projetar uma receita que não foi antes
      consolidada/importada. (`25_criar_tabela_receita_projecao.sql`)
- [ ] **Toda premissa livre (`PROJETOBEF.premissas`) precisa de `companyId`
      válido** (FK `NOT NULL` para `companies`). (`26_criar_tabela_premissas.sql`)
- [ ] Campos `NOT NULL` sem default que exigem preenchimento explícito: em
      `premissas`: `id`, `companyId`, `name`; em `receita_projecao`: `id`
      (default automático), `receita_id`.

## C) Presente no exemplo real, mas sem regra de validação em código

Fica registrado porque é claramente usado como premissa de projeção na prática,
mas nenhuma das fontes lidas impõe validação sobre estes campos — quem monta a
consultoria decide manualmente se estão adequados:

- [ ] `crescimento_aa` (taxa de crescimento ao ano) preenchido e coerente com o
      histórico de faturamento mensal, se disponível.
- [ ] `razao_credito` (proporção de crédito tributário aproveitável) preenchido.
- [ ] Bloco `pgdas_historico` (para empresas do Simples Nacional) com
      faturamento mensal recente, RBT12 e composição de receita por anexo —
      relevante para checar enquadramento e sublimite antes de projetar.
- [ ] Bloco `alertas` revisado manualmente (ex.: `rbt12_acima_sublimite_ce`,
      parcelamentos em curso, vencimentos de contrato) — nenhum destes bloqueia
      a projeção no código, mas são sinais de risco que a consultoria deveria
      checar antes de assinar as premissas.
- [ ] `percentual_crescimento`, `reducao_ibs_percentual`,
      `reducao_cbs_percentual` de cada item em `receita_projecao` — têm
      `default = 0` no banco, então uma linha pode ser gravada sem essas
      premissas terem sido de fato decididas. Confirmar manualmente que não
      ficaram no default por omissão.

## D) Pedido pela tarefa original, mas SEM evidência de campo/validação nos arquivos lidos

Registrar como lacuna explícita em vez de inventar uma regra:

- [ ] **Sazonalidade de vendas/compras**: não há campo, tabela ou validação
      correspondente em nenhum dos arquivos lidos.
- [ ] **Cronograma de transição da Reforma como objeto explícito** (ex.: uma
      tabela de percentuais de transição por ano além do que já está embutido
      em `percentual_ibs_AAAA`/`percentual_cbs_AAAA`): o que existe é a alíquota
      efetiva já discriminada ano a ano em `receita_projecao` — não há um
      "cronograma" separado e nomeado como tal no código lido.
- [ ] **Alíquotas referenciais por tributo** como tabela de referência
      independente (ex.: alíquota-padrão nacional de IBS/CBS por ano): não
      localizada nos arquivos lidos — o que existe são percentuais já
      aplicados por item de receita, não uma tabela de referência global.
- [ ] **Ano-base** como campo nomeado explicitamente: o mais próximo é
      `empresa.exercicio_ecf` no `premissas.json` (ano da ECF usada como Fonte
      A) — mas isso é observação do exemplo real, não uma regra imposta por
      `premissas.py`.

## Antes de aprovar premissas para rodar a projeção

1. Rodar `carregar()`/`validar()` do `premissas.py` e conferir se `_validacao`
   veio vazia.
2. Se não vazia, resolver cada item antes de prosseguir — especialmente
   divergências de `receita_bruta` e de derivados recalculados, que indicam
   erro na ECF de origem, não só um "aviso".
3. Confirmar que a série 2027-2033 (seja em `serie_anual` do JSON, seja nas
   colunas por ano de `receita_projecao`) está completa, sem ano faltando.
4. Revisar manualmente os campos da seção C e D acima — não há gate automático
   para eles hoje.
