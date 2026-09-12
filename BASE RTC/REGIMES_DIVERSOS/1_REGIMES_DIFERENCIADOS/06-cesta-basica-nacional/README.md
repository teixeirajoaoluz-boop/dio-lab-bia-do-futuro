# Cesta Básica Nacional de Alimentos — Alíquota Zero

## 1. Fundamento legal

**Achado desta rodada — corrige a base herdada de rodada anterior**: o artigo correto **não é o
intervalo 63-66**, como constava anteriormente. A Cesta Básica Nacional de Alimentos tem um
capítulo próprio, com um único artigo dedicado, na parte inicial do Título III da LC 214/2025
(antes do Título IV "Dos Regimes Diferenciados", onde estão os demais 11 segmentos deste bloco).

**Confirmado por leitura literal do texto oficial consolidado** — LC 214/2025, art. 125 (Título
III, Capítulo II "Da Cesta Básica Nacional de Alimentos"), texto oficial consolidado (norma
atualizada, já incorpora as alterações da LC 227/2025), Centro de Documentação e Informação da
Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

> "CAPÍTULO II
> DA CESTA BÁSICA NACIONAL DE ALIMENTOS
> Art. 125. Ficam reduzidas a zero as alíquotas do IBS e da CBS incidentes sobre as vendas de
> produtos destinados à alimentação humana relacionados no Anexo I desta Lei Complementar, com a
> especificação das respectivas classificações da NCM/SH, que compõem a Cesta Básica Nacional de
> Alimentos, criada nos termos do art. 8º da Emenda Constitucional nº 132, de 20 de dezembro de
> 2023.
> Parágrafo único. Aplica-se o disposto nos §§ 1º e 2º do art. 126 desta Lei Complementar às
> reduções de alíquotas de que trata o caput deste artigo."

**Não confundir com o art. 135** ("Dos Alimentos Destinados ao Consumo Humano", Seção VII do
Capítulo "Da Redução em 60%", Título IV — mesmo capítulo dos demais 11 segmentos deste bloco):

> "Art. 135. Ficam reduzidas em 60% (sessenta por cento) as alíquotas do IBS e da CBS incidentes
> sobre o fornecimento dos alimentos destinados ao consumo humano relacionados no Anexo VII desta
> Lei Complementar, com a especificação das respectivas classificações da NCM/SH."

São duas categorias distintas e não sobrepostas por desenho:
- **Cesta Básica Nacional (art. 125, Anexo I)** — alíquota **zero**, lista fechada e mais estreita
  de itens essenciais (a cesta básica em si).
- **Alimentos destinados ao consumo humano (art. 135, Anexo VII)** — redução de **60%**, categoria
  mais ampla, cobrindo alimentos em geral que não estejam na lista fechada do Anexo I.
Um mesmo produto alimentício não deveria, por desenho da lei, estar simultaneamente nos dois
Anexos — mas a existência e a extensão exata de eventual sobreposição entre Anexo I e Anexo VII
não foi verificada nesta rodada (ver Lacunas).

## 2. Regra

- **Percentual de redução**: 100% — alíquota ZERO de IBS e CBS.
- **Aplica-se a**: vendas de produtos destinados à alimentação humana relacionados no **Anexo I**
  da LC 214/2025, que compõem a Cesta Básica Nacional de Alimentos criada pelo art. 8º da EC
  132/2023.
- **Regra de estabilidade de alíquota (parágrafo único)**: aplicam-se a este artigo os §§ 1º e 2º
  do art. 126 — ou seja, mudanças na lista de produtos beneficiados (acréscimo, exclusão ou
  substituição) só entram em vigor após cumpridos os requisitos constitucionais de revisão de
  alíquota de referência (art. 156-A, §§ 9º e 11, da Constituição Federal), e o regime se estende,
  no que couber, à importação dos produtos listados.

## 3. Como funciona na prática

Sistemática geral (débito-crédito, apuração mensal, Split Payment) — alíquota zero na saída para
os itens do Anexo I, mantendo direito a crédito das entradas (não cumulatividade plena).

## 4. Exemplo de cálculo numérico

Operação hipotética: R$ 100.000,00 em vendas de itens da Cesta Básica Nacional (Anexo I),
referencial CBS 8,50% / IBS 5,00% (fonte: `aliquotas-transicao/cronograma-aliquotas.json`):

| Ano | Regime GERAL (produto qualquer, sem benefício) | Alíquota zero (cesta básica, art. 125) |
|---|---|---|
| 2027 | 8,50% → **R$ 8.500,00** | 0% → **R$ 0,00** |
| 2033 | 13,50% → **R$ 13.500,00** | 0% → **R$ 0,00** |

Para comparação, o mesmo produto se enquadrado como "alimento destinado ao consumo humano" do
art. 135 (60%, categoria mais ampla, não a cesta básica em si) recolheria:

| Ano | Redução de 60% (art. 135, alimentos em geral) |
|---|---|
| 2027 | 3,40% → **R$ 3.400,00** |
| 2033 | 5,40% → **R$ 5.400,00** |

## 5. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, Câmara dos Deputados) — leitura
  literal dos arts. 125 (Cesta Básica Nacional) e 135 (Alimentos Destinados ao Consumo Humano),
  para confirmar tanto o artigo correto quanto a distinção entre as duas categorias.
- `aliquotas-transicao/cronograma-aliquotas.json` — valores reais do cronograma CBS/IBS.

## 6. Lacunas conhecidas

1. **Lista completa do Anexo I** (itens da Cesta Básica Nacional de Alimentos) não foi extraída
   nesta rodada — apenas confirmado o fundamento legal (art. 125) e a remissão ao Anexo I.
2. **Extensão de eventual sobreposição entre Anexo I (cesta básica, zero) e Anexo VII (alimentos
   em geral, 60%, art. 135)** não foi investigada — não se sabe se algum item aparece nos dois
   Anexos por erro de redação, o que geraria conflito de alíquota a resolver.
3. **Nenhum exemplo real de mercado ou jurisprudência** foi pesquisado especificamente para esta
   pasta nesta rodada.

## Correção desta rodada

A rodada anterior citava "LC 214/2025, arts. 63 a 66" para este segmento, herdado do mapa estático
pré-existente da base (`fontes-legais/mapa-lc214-artigos.json`, tema "Cesta Básica Nacional e
Alíquota Zero") sem confirmação por fetch direto. A leitura do texto oficial consolidado nesta
rodada mostrou que essa numeração estava **incorreta** — o fundamento correto é o **art. 125**,
em capítulo próprio e específico da Cesta Básica Nacional de Alimentos (Título III, Capítulo II),
não no intervalo 63-66. Este README foi reescrito integralmente com a base correta.
