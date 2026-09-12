# Planos de Assistência à Saúde — Base de Cálculo Específica

## 1. Fundamento legal

LC 214/2025, art. 234 — texto oficial consolidado (norma atualizada, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
Capítulo III do Título V ("Dos Planos de Assistência à Saúde") abrange os **arts. 234 a 243**,
confirmados linha a linha no texto oficial:

- Art. 234: regime específico de IBS/CBS para seguradoras de saúde, administradoras de benefícios,
  cooperativas operadoras e cooperativas de seguro saúde, e demais operadoras de planos de
  assistência à saúde.
- Art. 235: define a **base de cálculo** = prêmios/contraprestações recebidos **+** receitas
  financeiras das reservas técnicas, **deduzidas** as indenizações relativas a eventos já
  ocorridos.
- Art. 236: estende o regime aos **planos de assistência funerária** (remissão aos arts. 234 a 242).
- Art. 237: fixa a **alíquota nacionalmente uniforme**, reduzida em **60%** sobre a soma das
  alíquotas de referência de cada esfera federativa.
- Art. 238: veda o crédito ao adquirente do plano, ressalvada a hipótese do parágrafo único
  (crédito proporcional ao contratante pessoa jurídica do regime regular, redação dada pela
  LC 227/2025).
- Art. 239: obrigação acessória de identificação dos beneficiários titulares e valores de prêmios.
- Art. 240: intermediação de planos de saúde tributada pela mesma alíquota do plano.
- Art. 241 e 242: importação e exportação de serviços de plano de saúde.
- Art. 243: estende o regime aos planos de assistência à saúde de **animais domésticos**, exceto
  quanto à alíquota (que segue regra própria de uniformização nacional sem a redução de 60%).

Link do PDF fonte (texto oficial consolidado):
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

## 2. Regra específica — em que difere do regime geral

No regime geral, a base de cálculo é o **valor da operação** (art. 12-15 da LC 214/2025) — o preço
cobrado pelo bem/serviço. No setor de saúde suplementar não há uma "venda" de bem por preço fixo:
a operadora recebe mensalidades (prêmios) de um conjunto de beneficiários e paga sinistros
(indenizações/reembolsos) que variam. A LC 214/2025 resolve isso com uma **base de cálculo
líquida setorial**, análoga à técnica usada para seguros:

```
Base de cálculo = (Prêmios/contraprestações recebidos + Receitas financeiras das reservas técnicas)
                   − Indenizações de eventos ocorridos
```

Isso é estruturalmente diferente do regime geral porque:

1. A base **não é o valor bruto cobrado do beneficiário** — é líquida das indenizações pagas,
   funcionando de forma parecida com uma "margem financeira" do segurador, não com um preço de
   venda.
2. Entram na base **receitas financeiras das reservas técnicas** (rendimento da aplicação
   financeira dos recursos que a operadora é obrigada a manter reservados) — um componente que não
   existe no cálculo do regime geral para a maioria dos setores.
3. Consequência prática: o tributo não é simplesmente "alíquota × mensalidade" — é
   "alíquota × (receita de prêmios + receita financeira das reservas − sinistros pagos no
   período)", o que pode gerar base tributável menor (ou até negativa em períodos de sinistralidade
   alta) do que a simples soma das mensalidades cobradas.

## 3. Exemplo de cálculo numérico

**Cenário hipotético**: operadora de plano de saúde, em um mês, recebe R$ 10.000.000 em
mensalidades de beneficiários, tem R$ 200.000 de rendimento financeiro sobre reservas técnicas, e
paga R$ 7.500.000 em indenizações (reembolsos/pagamentos a prestadores) referentes a eventos
ocorridos no período.

```
Base de cálculo = 10.000.000 + 200.000 − 7.500.000 = 2.700.000
```

Aplicando a alíquota específica do setor confirmada no art. 237 (soma das alíquotas de referência
de cada esfera federativa, **reduzida em 60%**): tomando ~17,7% como a soma referencial ilustrativa
das alíquotas de referência (`fontes-legais/mapa-lc214-artigos.json`, tema "Alíquotas do IBS e
CBS" — o valor definitivo da alíquota de referência só será fixado por resolução do Senado, ver
Lacunas), a alíquota efetiva do setor seria:

```
Alíquota efetiva = 17,7% × (1 − 60%) = 7,08%
IBS + CBS ≈ 2.700.000 × 7,08% ≈ R$ 191.160
```

Contraste com o regime geral aplicado ingenuamente sobre o valor bruto das mensalidades (o que a
lei **não** manda fazer, mas serve para evidenciar a diferença de mecânica):

```
Se fosse sobre o valor bruto, sem a base líquida: 10.000.000 × 7,08% = R$ 708.000
```

A diferença (R$ 708.000 vs R$ 191.160) mostra o efeito da dedução de sinistros e da base
líquida — não é uma questão de "alíquota menor", é uma **base de cálculo estruturalmente distinta**.

## 4. Fontes consultadas

- LC 214/2025 (texto oficial consolidado, norma atualizada, Câmara dos Deputados) — arts. 234 a
  243, lidos literalmente.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — confirmado que este tema
  não estava nos 17 temas já mapeados.

## 5. Lacunas conhecidas

- **Valor numérico da alíquota de referência** de cada esfera federativa ainda não foi fixado (só
  será definido por resolução do Senado, conforme cronograma da Reforma) — o exemplo usa ~17,7%
  apenas como referência ilustrativa de ordem de grandeza; a redução de 60% sobre essa base, essa
  sim, já está confirmada no art. 237.
- Tratamento de planos coletivos empresariais vs. individuais/familiares — não pesquisado.
- Jurisprudência: tema novo, sem precedentes judiciais aplicáveis (tributo inexistente antes da
  Reforma).
