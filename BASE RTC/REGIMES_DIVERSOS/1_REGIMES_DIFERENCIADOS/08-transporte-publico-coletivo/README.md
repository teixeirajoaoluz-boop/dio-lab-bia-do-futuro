# Transporte Público Coletivo Urbano, Semiurbano e Metropolitano — Isenção

## 1. Fundamento legal — correção de enquadramento desta rodada

A rodada anterior havia levantado a hipótese de que este segmento fosse, na verdade, um Regime
Específico (fora do escopo deste bloco), por não ter localizado o dispositivo exato na LC
214/2025. A leitura do texto oficial consolidado nesta rodada resolve a dúvida: **o segmento está
corretamente classificado neste bloco (Regimes Diferenciados)**, mas não como uma redução de
alíquota de 60%/zero — é uma **isenção**, com Capítulo próprio, logo após o Capítulo IV ("Da
Redução a Zero") do mesmo Título IV.

**Confirmado por leitura literal do texto oficial consolidado** — LC 214/2025, art. 157 (Título
IV "Dos Regimes Diferenciados do IBS e da CBS", Capítulo V "Do Transporte Público Coletivo de
Passageiros Rodoviário e Metroviário de Caráter Urbano, Semiurbano e Metropolitano"), texto
oficial consolidado (norma atualizada, já incorpora as alterações da LC 227/2025), Centro de
Documentação e Informação da Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

> "CAPÍTULO V
> DO TRANSPORTE PÚBLICO COLETIVO DE PASSAGEIROS RODOVIÁRIO E METROVIÁRIO DE CARÁTER URBANO,
> SEMIURBANO E METROPOLITANO
> Art. 157. Fica isento do IBS e da CBS o fornecimento de serviços de transporte público coletivo
> de passageiros rodoviário e metroviário de caráter urbano, semiurbano e metropolitano, sob
> regime de autorização, permissão ou concessão pública.
> Parágrafo único. Para fins do caput deste artigo, consideram-se:
> I - serviço de transporte público coletivo de passageiros o acessível a toda a população
> mediante cobrança individualizada, com itinerários e preços fixados pelo poder público;
> II - transporte rodoviário o serviço de transporte terrestre realizado sobre vias urbanas e
> rurais; [...]"

**Distinção importante — fora do escopo desta pasta**: existe um regime **diferente e separado**
para transporte coletivo **intermunicipal/interestadual**, tratado nos **arts. 284-287** da LC
214/2025 (Regime Específico, redução de 40%) — isso está sendo mapeado por outro agente/processo
no bloco `2_REGIMES_ESPECIFICOS`, não é reaberto aqui. O art. 157 desta pasta cobre apenas o
transporte **urbano, semiurbano e metropolitano** rodoviário e metroviário.

## 2. Regra

- **Natureza do benefício**: **isenção** (não uma redução percentual de alíquota) — o fornecimento
  do serviço listado não sofre incidência de IBS nem de CBS.
- **Aplica-se a**: serviços de transporte público coletivo de passageiros **rodoviário e
  metroviário**, de caráter **urbano, semiurbano e metropolitano**, prestados sob regime de
  autorização, permissão ou concessão pública — ou seja, o serviço precisa ser acessível a toda a
  população, com cobrança individualizada e itinerários/preços fixados pelo poder público (§ único,
  inciso I).
- **Não se aplica** ao transporte intermunicipal/interestadual (regime específico separado, arts.
  284-287, fora de escopo desta pasta) nem a serviços de transporte privado/fretamento sem regime
  de autorização, permissão ou concessão pública.

## 3. Como funciona na prática

Diferente dos demais 11 segmentos deste bloco (redução de 60% ou zero, mas ainda sujeitos a débito
e crédito na sistemática geral), a **isenção do art. 157 significa que a operação não gera débito
de IBS/CBS na saída**. A LC 214/2025 não traz, no próprio art. 157, uma vedação expressa de crédito
das entradas para o fornecedor — ao contrário do que a rodada anterior havia especulado a partir de
um trecho de outro dispositivo (transporte ferroviário/hidroviário ligado a regime específico,
fora do escopo deste artigo). Recomenda-se, antes de aplicar esta regra em um caso concreto,
verificar as regras gerais de vedação/estorno de crédito para operações isentas (arts. 47 e
seguintes, já mapeados na base canônica), pois **isenção**, diferente de **alíquota zero**, tende a
gerar vedação de crédito das entradas pela sistemática geral do IBS/CBS — este ponto não foi
verificado a fundo nesta rodada (ver Lacunas).

## 4. Exemplo de cálculo numérico

Operação hipotética: R$ 100.000,00 em tarifas de transporte público coletivo urbano (ônibus
municipal ou metrô, sob concessão pública), referencial CBS 8,50% / IBS 5,00% (fonte:
`aliquotas-transicao/cronograma-aliquotas.json`):

| Ano | Regime GERAL (sem benefício) | Isenção (art. 157) |
|---|---|---|
| 2027 | 8,50% → **R$ 8.500,00** | isento → **R$ 0,00** |
| 2033 | 13,50% → **R$ 13.500,00** | isento → **R$ 0,00** |

Diferente dos exemplos de alíquota zero das demais pastas deste bloco, aqui a rubrica correta na
nota fiscal é "isento", não "alíquota 0%" — o efeito final em caixa é o mesmo (R$ 0,00 de débito),
mas a classificação fiscal e o eventual tratamento de crédito das entradas podem divergir.

## 5. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, Câmara dos Deputados) — leitura
  literal do art. 157 e do parágrafo único, e confirmação de que o Capítulo V (isenção) sucede o
  Capítulo IV (redução a zero) dentro do mesmo Título IV "Dos Regimes Diferenciados".
- `aliquotas-transicao/cronograma-aliquotas.json` — valores reais do cronograma CBS/IBS.

## 6. Lacunas conhecidas

1. **Tratamento do crédito das entradas** para o fornecedor de transporte público coletivo isento
   (se há vedação/estorno pela sistemática geral de isenções, arts. 47 e seguintes, ou se há regra
   específica de manutenção de crédito) não foi verificado a fundo nesta rodada.
2. **Nenhuma jurisprudência ou exemplo real de mercado** (ex.: concessionária de transporte urbano
   cliente do escritório) foi pesquisado nesta rodada.

## Correção desta rodada

A rodada anterior classificou este segmento como um possível Regime Específico (por não ter
localizado o artigo exato, e por ter encontrado, em outra fonte, uma regra de vedação de crédito
para transporte ferroviário/hidroviário urbano que não pertence a este dispositivo). A leitura do
texto oficial consolidado confirma que o segmento está corretamente classificado neste bloco
(Regimes Diferenciados, art. 157, Capítulo V do Título IV) — mas como **isenção**, categoria
distinta de "redução de 60%" ou "alíquota zero" usada nos demais 11 segmentos. Este README foi
reescrito integralmente com a base correta.
