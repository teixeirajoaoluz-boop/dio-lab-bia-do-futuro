# Transporte Coletivo de Passageiros Rodoviário Intermunicipal e Interestadual — Redução de 40%

## 1. Fundamento legal

LC 214/2025, Título V, Capítulo VII ("Dos Bares, Restaurantes, Hotelaria, Parques de Diversão e
Parques Temáticos, Transporte Coletivo de Passageiros e Agências de Turismo"), **Seção III — "Do
Transporte Coletivo de Passageiros Rodoviário Intermunicipal e Interestadual, Ferroviário,
Hidroviário e Aéreo Regional e Do Transporte de Carga Aéreo Regional"**, **arts. 284 a 287**
(confirmado por leitura direta do texto oficial, 2026-08-27). A Seção IV seguinte ("Das Agências
de Turismo") começa no art. 288 — o intervalo 284-287 é a Seção III completa, sem sobra.

**IMPORTANTE — não confundir com outro regime**: este regime (arts. 284-287) trata do transporte
**intermunicipal e interestadual** (entre municípios/estados). É **diferente** do transporte
público **urbano, semiurbano e metropolitano** do **art. 157** (isenção/imunidade tratada à parte),
cujo README próprio é
`C:\GUERRA_MENTORIA_REGRAS RTC\REGIMES_DIVERSOS\1_REGIMES_DIFERENCIADOS\08-transporte-publico-coletivo`
— pasta sendo corrigida por outro agente em paralelo, não tocada aqui.

Fonte: LC 214/2025, arts. 284 a 287 — texto oficial consolidado (norma atualizada, Câmara dos
Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).

## 2. Regra específica — em que difere do regime geral

O art. 284 define o regime específico e delimita 4 modalidades de transporte coletivo de
passageiros sujeitas a ele: (I) rodoviário intermunicipal e interestadual; (II) ferroviário e
hidroviário intermunicipal e interestadual; (III) ferroviário e hidroviário de caráter urbano,
semiurbano e metropolitano; (IV) aéreo regional. O § 4º do art. 284 restringe os incisos I a III
ao **transporte público** (sob autorização, permissão ou concessão pública) — não abrange
transporte fretado/privado fora desse enquadramento.

Dentro da Seção III há **duas mecânicas distintas**, e o regime não é uniforme:

1. **Art. 285 — ferroviário/hidroviário urbano, semiurbano e metropolitano (inciso III)**: alíquota
   **reduzida em 100%** (isenção efetiva) e **vedação total de crédito** — tanto para o próprio
   fornecedor do serviço de transporte (inciso II) quanto para o adquirente (inciso III do art.
   285). É um regime à parte, mais restritivo, dentro da mesma Seção.
2. **Art. 286 — rodoviário, ferroviário e hidroviário intermunicipais e interestaduais (incisos I
   e II do art. 284)**: alíquotas do regime específico **reduzidas em 40%** (quarenta por cento).
   O parágrafo único do art. 286 **permite a apropriação e utilização de créditos de IBS/CBS** nas
   aquisições de bens e serviços pelos fornecedores desse transporte sujeitos ao regime regular,
   observado o disposto nos arts. 47 a 56 (regime geral de créditos) — ou seja, crédito pleno do
   prestador sobre seus insumos, com débito recolhido à alíquota reduzida (mesmo padrão assimétrico
   observado em bares/restaurantes e hotelaria).
3. **Art. 287 — transporte aéreo regional de passageiros ou de carga (inciso IV do art. 284)**:
   alíquotas **também reduzidas em 40%**, mas em artigo próprio, específico para o modal aéreo
   regional — não compartilha o mesmo parágrafo de regras de crédito do art. 286 (o art. 287 não
   tem parágrafo próprio tratando de crédito na leitura feita; o § 2º do art. 284, que permite
   crédito ao adquirente do serviço de transporte em geral, aplica-se de forma transversal a toda
   a Seção III, "observado o disposto nos arts. 47 a 56").

Em resumo: a redução de 40% mencionada no request do usuário está confirmada, mas **não é um único
percentual genérico do art. 287** — está fracionada em dois artigos (art. 286 para
rodo/ferro/hidroviário intermunicipal/interestadual; art. 287 para aéreo regional), ambos com 40%,
e coexiste com um regime totalmente diferente (100% de redução + vedação de crédito) no art. 285
para ferroviário/hidroviário urbano dentro da mesma Seção III.

## 3. Exemplo de cálculo numérico

**Cenário**: empresa de ônibus presta serviço de transporte rodoviário interestadual (art. 284, I),
faturando R$ 300.000 no mês, com R$ 100.000 em compras de insumos (combustível, peças,
manutenção) tributados à alíquota cheia.

Usando a alíquota de referência ilustrativa de ~17,7% (IBS+CBS, `fontes-legais/mapa-lc214-artigos.json`)
e a redução de 40% confirmada no art. 286:

```
Alíquota efetiva = 17,7% × (1 − 40%) = 10,62%
Débito sobre o serviço prestado ≈ 300.000 × 10,62% ≈ R$ 31.860
Crédito sobre as compras (alíquota cheia, arts. 47-56) ≈ 100.000 × 17,7% ≈ R$ 17.700
Saldo a recolher ≈ 31.860 − 17.700 = R$ 14.160
```

Isso ilustra o art. 286 (rodoviário intermunicipal/interestadual, crédito pleno ao prestador). Caso
o mesmo serviço fosse ferroviário/hidroviário de caráter **urbano/semiurbano/metropolitano** (art.
285), o resultado seria diferente por natureza: débito = zero (redução de 100%) e nenhum crédito
apropriável — não há saldo a recolher, mas também não há aproveitamento de crédito das compras.

## 4. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (com alterações da LC 227/2025), Câmara dos Deputados —
  leitura direta dos arts. 273 a 288 (Capítulo VII completo) para confirmar o intervalo exato da
  Seção III e a mecânica de cada artigo.
- `C:\GUERRA_MENTORIA_REGRAS RTC\REGIMES_DIVERSOS\2_REGIMES_ESPECIFICOS\09-bares-restaurantes\README.md`
  — modelo de estrutura replicado para este README.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — alíquota de referência
  ilustrativa (~17,7%) usada no exemplo numérico; tema Seção III do Capítulo VII não estava
  mapeado anteriormente neste arquivo.

## 5. Lacunas conhecidas

- **Alíquota de referência total (~17,7%)** usada no exemplo é ilustrativa/premissa, não valor
  legal fixado na LC 214/2025 (depende de resolução do Comitê Gestor do IBS e de lei ordinária da
  CBS).
- **Regras de crédito do art. 287 (aéreo regional)** — não há parágrafo próprio no art. 287
  tratando de crédito explicitamente; a leitura de que o crédito segue o regime geral (arts. 47-56)
  apoia-se no § 2º do art. 284 (regra geral da Seção), não em dispositivo específico do art. 287 —
  tratar como interpretação razoável, não como texto literal expresso no próprio artigo.
- **Definição de "transporte aéreo regional"** (art. 284, § 1º, VIII) depende de ato conjunto do
  Comitê Gestor do IBS e do Ministro da Fazenda com base em classificação da ANAC — rotas exatas
  não fazem parte do texto da lei e não foram pesquisadas aqui.
- **Cronograma de transição/vigência específico** deste regime (percentuais de implementação
  2026-2033) não foi pesquisado nesta rodada — apenas a mecânica final (2033 em diante) foi
  confirmada.
