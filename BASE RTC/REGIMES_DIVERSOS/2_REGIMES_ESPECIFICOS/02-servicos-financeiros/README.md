# Serviços Financeiros — Base sobre Receitas, não sobre Valor da Operação

## 1. Fundamento legal

LC 214/2025, Título V "Dos Regimes Específicos do IBS e da CBS", Capítulo II "Dos Serviços
Financeiros" — **arts. 181 a 233** — texto oficial consolidado (norma atualizada, com as
alterações da LC 227/2025, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
O mapa antigo (`fontes-legais/mapa-lc214-artigos.json`, arts. 167-182) usava numeração
**incorreta/desatualizada e não deve mais ser usado** para este tema — a numeração confirmada por
leitura direta do texto oficial é a que segue.

Estrutura interna confirmada do Capítulo II:

- **Seção I — Disposições Gerais (arts. 181-184)**: art. 181 sujeita serviços financeiros a regime
  específico; **art. 182** define o rol de "serviços financeiros" (operações de crédito, câmbio,
  TVM, securitização, faturização, seguros, previdência complementar, capitalização, consórcio,
  arranjos de pagamento, ativos virtuais, etc. — 17 incisos); art. 183 define quem se sujeita ao
  regime (instituições supervisionadas pelo SFN e demais fornecedores equiparados); art. 184 remete
  ao regime geral os serviços bancários tarifados (conta corrente, cheque, saque, TED etc.).
- **Seção II — Disposições Comuns aos Serviços Financeiros (arts. 185-191)**: **art. 185** — a base
  de cálculo é composta das **receitas** das operações, com as deduções previstas no Capítulo; art.
  186 — receitas de reversão de provisão/recuperação de crédito baixado compõem a base; art. 187 —
  restrição das deduções; art. 188 — regra para cooperativas; **art. 189** — alíquota (remete ao
  cronograma do art. 233); art. 190 — apropriação de créditos; art. 191 — obrigação acessória.
- **Seção III — Das Operações de Crédito, Câmbio, TVM, Securitização e Faturização (a partir do
  art. 192)**: **art. 192** — base de cálculo específica dessas operações = receitas menos despesas
  financeiras de captação, despesas de câmbio, perdas com TVM etc.
- Demais seções do Capítulo (IV a XIII) tratam de consórcio, fundos de investimento, FGTS, arranjos
  de pagamento, mercados organizados, seguros, previdência, capitalização, ativos virtuais,
  importação (art. 231) e exportação (art. 232) de serviços financeiros.
- **Seção XIV — Disposições Transitórias (art. 233)**: fecha o Capítulo II — fixa o cronograma da
  soma das alíquotas de IBS+CBS sobre serviços financeiros (ver item 3). O Capítulo III "Dos Planos
  de Assistência à Saúde" começa em seguida, no art. 234.

## 2. Regra específica — em que difere do regime geral

No regime geral, a base é o valor bruto da operação (preço cobrado do cliente). Em serviços
financeiros, não há um "preço de venda" no sentido tradicional — um banco cobra juros sobre um
empréstimo, tem spread cambial, tarifas e comissões; uma seguradora recebe prêmios e paga
sinistros. A LC 214/2025 resolve isso tributando a **receita própria/margem** do prestador, não o
volume financeiro movimentado:

1. **Base sobre receitas específicas** (juros, spread, tarifas, comissões), com deduções por tipo
   de serviço (art. 185) — não sobre o valor principal do empréstimo, do câmbio ou do título
   negociado.
2. **Regra de margem/diferencial para crédito, câmbio e TVM** (art. 192) — dedução de despesas
   financeiras de captação, despesas de câmbio e perdas com TVM da receita bruta dessas operações;
   mecânica análoga, em espírito, à usada para planos de saúde (base = receita − indenizações, art.
   235) e para apostas (base = receita própria), mas com fórmula própria do setor financeiro.
3. **Alíquota específica, diferente da padrão** (art. 189 c/c art. 233): a soma das alíquotas de
   IBS+CBS sobre serviços financeiros é fixada por cronograma legal próprio — **confirmada** nesta
   pesquisa (ver item 3, Exemplo de cálculo).
4. **Split payment com aplicação distinta**: o mecanismo de retenção automática na liquidação
   financeira (arts. 31 a 35 do regime geral) pressupõe um preço de venda identificável no momento
   do pagamento. O texto lido não trouxe, dentro do Capítulo II, um dispositivo que excepcione
   expressamente o split payment para serviços financeiros — permanece como lacuna (ver Lacunas).

## 3. Exemplo de cálculo numérico

**Cenário hipotético**: banco concede empréstimo de R$ 1.000.000 no mês, cobra R$ 15.000 de juros
e tarifas no período, e tem R$ 3.000 de despesas dedutíveis específicas do regime (art. 192).

```
Base de cálculo (art. 185/192) = Receitas do serviço financeiro (juros + tarifas) − deduções
                                 = 15.000 − 3.000 = 12.000
```

**Não** é `1.000.000 × alíquota` (isso seria tributar o principal do empréstimo, o que a mecânica
de "base sobre receitas" evita).

**Alíquota (art. 233, confirmada)**: a soma das alíquotas de IBS+CBS sobre serviços financeiros é
fixada por cronograma legal: **10,85%** em 2027-2028, **11,00%** em 2029, **11,15%** em 2030,
**11,30%** em 2031, **11,50%** em 2032 e **12,50%** a partir de 2033 (art. 233, incisos I a VI,
com redação da LC 227/2025). Aplicando a alíquota de 2027 (10,85%) sobre a base do exemplo:

```
IBS + CBS = 12.000 × 10,85% ≈ R$ 1.302
```

**Contraste didático com o regime geral** (não aplicável ao setor, só para evidenciar a diferença
de mecânica): se o banco fosse tributado sobre o valor bruto do empréstimo pela mesma alíquota de
10,85%, o tributo seria `1.000.000 × 10,85% = R$ 108.500` — mais de 80× o valor real
(R$ 1.302). Isso demonstra por que "base sobre receita/margem" não é apenas uma alíquota mais
baixa, é uma base de cálculo qualitativamente diferente.

## 4. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada com a LC 227/2025, Câmara dos
  Deputados) — leitura direta dos arts. 181 a 233, confirmando *caput*, incisos e parágrafos
  relevantes (inclusive o cronograma de alíquotas do art. 233).
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — mapa antigo (arts.
  167-182) identificado como desatualizado para este tema; não usar mais essa numeração.
- Decreto 12.955/2026 (Regulamento) — citado em pesquisa anterior como fonte regulamentar
  complementar dos arts. 185/186 da LC; não lido diretamente nesta rodada, mantém-se como
  referência secundária.

## 5. Lacunas conhecidas

- **Regra de crédito ao tomador** de serviço financeiro em detalhe operacional (o art. 190 remete
  a informações prestadas pelos fornecedores ao Comitê Gestor/RFB e aos arts. 47 a 56, mas o
  mecanismo prático de apropriação não foi aprofundado nesta pesquisa).
- **Dispositivo que excepciona split payment** para serviços financeiros de forma expressa — não
  localizado dentro do Capítulo II lido; permanece em aberto se há regra específica em outro trecho
  da lei ou em regulamento.
- **Regulamentação infralegal** (Decreto 12.955/2026, arts. 273-274) sobre a mecânica de deduções
  dos arts. 185/186/192 — referenciada mas não lida diretamente nesta rodada.
