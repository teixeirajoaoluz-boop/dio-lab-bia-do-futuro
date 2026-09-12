# Agências de Viagem e Operadoras de Turismo — Base sobre Comissão, não sobre o Pacote

## 1. Fundamento legal

LC 214/2025, art. 288 — texto oficial consolidado (norma atualizada, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
Dentro do Capítulo VII do Título V, a **Seção IV — "Das Agências de Turismo"** começa no
**art. 288** e vai até o **art. 291**, confirmado linha a linha no texto oficial:

- Art. 288: regime específico de IBS/CBS para agências de turismo.
- Art. 289: na intermediação de serviços turísticos, a **base de cálculo é o valor da operação,
  deduzidos os repasses aos fornecedores intermediados** com base no documento que subsidia o
  agenciamento (inciso I); a alíquota é a mesma aplicável a hotelaria/parques de diversão/parques
  temáticos (inciso II — ou seja, também com a redução de 40% do art. 281); § 2º integra à base
  demais valores, comissões e incentivos pagos por terceiros.
- Art. 290: permite ao **adquirente** (ex.: empresa que contrata viagens corporativas) apropriar
  crédito do IBS/CBS relativo ao **serviço de intermediação da agência** (não ao pacote inteiro).
- Art. 291: permite a apropriação e utilização de créditos de IBS/CBS nas aquisições de bens e
  serviços pelas próprias agências de turismo, vedado o crédito sobre os valores deduzidos da base
  nos termos do art. 289, I.

Link do PDF fonte (texto oficial consolidado):
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

## 2. Regra específica — em que difere do regime geral

Uma agência de viagem tipicamente vende um pacote que inclui passagem aérea, hospedagem e
passeios — serviços prestados por terceiros (companhias aéreas, hotéis, operadoras locais), não
pela própria agência. Se o regime geral fosse aplicado sobre o valor bruto do pacote, a agência
seria tributada sobre receita que na verdade pertence aos fornecedores intermediados — problema
estrutural semelhante ao de uma comissária/representante comercial.

A LC 214/2025 resolve isso com uma base de cálculo **líquida de repasses**:

```
Base de cálculo = Valor cobrado do cliente pelo pacote − Repasses aos fornecedores intermediados
                 (companhias aéreas, hotéis, operadoras terceirizadas etc.)
```

Isso é estruturalmente parecido com a técnica usada em serviços financeiros e planos de saúde
(base sobre receita/margem própria, não sobre o giro bruto), mas com uma peculiaridade adicional:
o art. 290 permite ao **adquirente do serviço de intermediação** (não ao consumidor final típico,
mas a uma empresa que contrata viagens, por exemplo) creditar-se do IBS **apenas sobre a parcela
de intermediação** da agência — não sobre o valor das passagens/hospedagem que a agência apenas
repassou (esses, presumivelmente, já geram crédito diretamente do fornecedor original, se
aplicável).

## 3. Exemplo de cálculo numérico

**Cenário**: agência de viagens corporativas vende um pacote de R$ 50.000 (passagens +
hospedagem + traslados) para uma empresa cliente. Do valor total, R$ 44.000 são repassados às
companhias aéreas e ao hotel; a agência retém R$ 6.000 de comissão/taxa de serviço.

```
Base de cálculo = 50.000 − 44.000 = 6.000
```

Aplicando a alíquota específica confirmada no art. 289, II (mesma de hotelaria/parques —
redução de 40% do art. 281 — sobre a soma referencial ilustrativa de ~17,7%, ainda não fixada por
resolução do Senado, ver Lacunas):

```
Alíquota efetiva = 17,7% × (1 − 40%) = 10,62%
IBS + CBS ≈ 6.000 × 10,62% ≈ R$ 637
```

**Crédito do adquirente (art. 290)**: a empresa cliente, se contribuinte do regime regular, credita
apenas o IBS relativo aos R$ 637 de intermediação — não os R$ 44.000 repassados (que seguem seu
próprio fluxo de tributação/crédito diretamente na relação entre a empresa cliente e os
fornecedores originais, ou entre a agência e esses fornecedores, dependendo de como a operação é
estruturada documentalmente — mecânica exata não detalhada nesta pesquisa). Pelo art. 291, a
própria agência mantém crédito sobre suas aquisições de bens e serviços, vedado apenas o crédito
sobre os valores já deduzidos da base (os repasses do art. 289, I).

Contraste com tributação sobre o valor bruto e sem a redução setorial (o que a lei não manda
fazer): `50.000 × 17,7% ≈ R$ 8.850` — mais de 13× o valor correto de R$ 637, evidenciando por que a
base líquida de repasses é uma mecânica de cálculo distinta, não um mero desconto de alíquota.

## 4. Fontes consultadas

- LC 214/2025 (texto oficial consolidado, norma atualizada, Câmara dos Deputados) — arts. 288 a
  291, lidos literalmente.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — tema não coberto nos 17
  mapeados anteriormente.

## 5. Lacunas conhecidas

- **Valor numérico da alíquota de referência** de cada esfera federativa ainda não foi fixado por
  resolução do Senado — o exemplo usa ~17,7% apenas como ordem de grandeza; a alíquota específica
  do setor (mesma de hotelaria, com redução de 40%) já está confirmada no art. 289, II c/c art. 281.
- **Mecânica de crédito dos fornecedores intermediados** (companhia aérea, hotel) quando o
  pagamento passa pela agência — não detalhada; risco de dupla tributação ou de vácuo de crédito se
  a documentação fiscal não for bem estruturada entre os três elos (cliente, agência, fornecedor).
- **Interação com o regime de hotelaria** (segmento 08) quando o pacote inclui hospedagem — mesma
  observação de sobreposição já registrada no segmento 08.
