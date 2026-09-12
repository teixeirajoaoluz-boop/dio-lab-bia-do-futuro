# Zona Franca de Manaus e Áreas de Livre Comércio — Alíquota Zero e Crédito Presumido

## 1. Fundamento legal

**Correção de localização (confirmado por leitura direta do texto oficial, 2026-08-27)**: o bloco
ZFM/ALC não está no Título V — está no **Livro III ("Das Demais Disposições"), Título I** ("Da
Zona Franca de Manaus, das Áreas de Livre Comércio, da Devolução do IBS e da CBS ao Turista
Estrangeiro, do Programa Nacional de Conformidade Tributária e das Penalidades Administrativas
Não Tributárias Relativas ao Recolhimento dos Tributos na Liquidação Financeira — título com
redação dada pela LC 227/2025).

- **Capítulo I — Da Zona Franca de Manaus**: abre no **art. 439** ("Os benefícios relativos à
  Zona Franca de Manaus estabelecidos neste Capítulo aplicam-se até a data estabelecida pelo
  art. 92-A do ADCT"). Definições no art. 440 (indústria incentivada, bem intermediário etc.).
  Arts. 448/449 (dentro deste mesmo capítulo): **crédito presumido de IBS** à indústria
  incentivada na ZFM na aquisição de bem intermediário produzido dentro da própria área.
- **Capítulo II — Das Áreas de Livre Comércio**: abre no **art. 458** ("Os benefícios relativos
  às Áreas de Livre Comércio estabelecidos neste Capítulo aplicam-se até a data estabelecida
  pelo art. 92-A do ADCT"). Art. 459 (mesmo capítulo): relação das ALC com regime favorecido —
  Tabatinga, Guajará-Mirim, Boa Vista e Bonfim, Macapá e Santana, entre outras.
- Arts. 445 e 463, citados na versão anterior deste README, não foram relidos linha a linha nesta
  rodada de confirmação — manter como não confirmados até nova checagem (ver Lacunas).

Fonte: LC 214/2025, arts. 439 e 458 (artigos-âncora dos Capítulos I e II do Título I do Livro
III) — texto oficial consolidado (norma atualizada, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).

## 2. Regra específica — em que difere do regime geral

O regime geral tributa toda operação com bens/serviços à alíquota padrão, com crédito pleno na
cadeia (arts. 28-47). Para a ZFM/ALC, a LC 214/2025 substitui isso por uma combinação de:

1. **Alíquota zero em operações específicas** (art. 445 para ZFM; art. 463 para bem industrializado
   nacional destinado a contribuinte habilitado em ALC) — diferente de uma "redução percentual",
   é ausência total de débito na operação alcançada.
2. **Crédito presumido do IBS à indústria incentivada** (arts. 448/449) na compra de bem
   intermediário produzido dentro da própria ZFM — mecanismo que **substitui o crédito ordinário**
   (que normalmente exigiria débito na etapa anterior) por um crédito fixado independentemente do
   valor de IBS efetivamente cobrado do fornecedor, preservando o incentivo fiscal regional mesmo
   dentro da lógica não cumulativa do IBS/CBS. Isso é estruturalmente diferente do crédito comum:
   no regime geral, o crédito do adquirente espelha o débito do fornecedor; no crédito presumido
   da ZFM, o valor é definido por regra própria, não pelo débito efetivo da operação anterior.

Este regime é historicamente sensível: a manutenção dos incentivos da ZFM tem base constitucional
(art. 40 do ADCT, com vigência assegurada até 2073 pela EC 132/2023) e é tema recorrente de disputa
em tribunais superiores mesmo antes da Reforma — motivo pelo qual jurisprudência do STF é relevante
como pano de fundo (ver Lacunas).

## 3. Exemplo de cálculo numérico

**Cenário**: indústria incentivada na ZFM compra R$ 500.000 em bem intermediário produzido por
outra empresa dentro da própria ZFM, e depois vende o produto industrializado por R$ 1.200.000 a
um contribuinte fora da ZFM (regime geral, sem alíquota zero).

1. **Compra do bem intermediário (dentro da ZFM)**: em vez de creditar o IBS efetivamente cobrado
   pelo fornecedor (que pode ser reduzido/zero pelo próprio regime da zona), a indústria apropria
   um **crédito presumido de IBS**, calculado por regra própria dos arts. 448/449 — o percentual
   exato não foi confirmado nesta pesquisa (ver Lacunas). Hipoteticamente, se o crédito presumido
   fosse de 15% do valor da aquisição: `500.000 × 15% = R$ 75.000` de crédito presumido de IBS.
2. **Venda para fora da ZFM**: segue o regime geral. Usando a alíquota de referência ilustrativa de
   ~17,7% (IBS+CBS, `fontes-legais/mapa-lc214-artigos.json`): débito de
   `1.200.000 × 17,7% ≈ R$ 212.400`.
3. **Apuração**: a indústria abate do débito de R$ 212.400 o crédito presumido de R$ 75.000
   (mais eventuais créditos ordinários de outros insumos), reduzindo o valor líquido a recolher —
   um resultado que **não dependeu do IBS efetivamente pago pelo fornecedor dentro da ZFM**, ao
   contrário do crédito ordinário do regime geral.

## 4. Fontes consultadas

- MCP `mcp-rag-reforma` (`buscar_reforma`, tier="chunk") — arts. 445, 448, 449, 458, 459, 463 da
  LC 214/2025.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — tema não coberto nos 17
  mapeados anteriormente; nem EC 132/2023 (art. 40 ADCT) foi lido diretamente nesta rodada.

## 5. Lacunas conhecidas

- **Percentual exato do crédito presumido** (arts. 448/449) — não confirmado; o exemplo usa valor
  hipotético apenas para ilustrar a mecânica.
- **Arts. 445 e 463** (alíquota zero) — citados na versão original deste README a partir de
  paráfrase do RAG; não foram relidos linha a linha do texto oficial nesta rodada de confirmação
  (que focou em achar os artigos-âncora dos capítulos, arts. 439 e 458). Tratar como pendente de
  reconfirmação.
- **Artigo de abertura do capítulo ZFM/ALC**: RESOLVIDO nesta rodada — é o **art. 439** (Capítulo
  I, ZFM) e o **art. 458** (Capítulo II, ALC), ambos dentro do Título I do Livro III ("Das Demais
  Disposições").
- **Jurisprudência STF/STJ sobre ZFM** não foi consultada nesta pesquisa (o request do usuário
  aponta os MCPs `guerra-stf`/`guerra-stj` como relevantes para este tema histórico de disputa,
  mas não foram acionados nesta rodada por foco em fundamentação legal primária) — pendente para
  aprofundamento futuro.
- Relação entre o novo regime de IBS/CBS na ZFM e o **IPI mantido/zerado** para produtos ZFM
  (regra de transição do IPI na Reforma) — não pesquisada.
- Texto integral literal dos 6 artigos não foi obtido via fetch direto do Planalto — vieram de
  paráfrase/trecho do RAG.
