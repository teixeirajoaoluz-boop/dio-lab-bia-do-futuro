# Concursos de Prognósticos e Apostas (Loterias e Bets) — Base sobre Receita Própria

## 1. Fundamento legal

LC 214/2025, art. 244 — texto oficial consolidado (norma atualizada, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
Capítulo IV do Título V ("Dos Concursos de Prognósticos") começa no art. 244 e vai até o
**art. 250** (não 247 — correção de numeração: o Capítulo tem 3 Seções: Seção I "Disposições
Gerais" arts. 244-248, Seção II "Da Importação" art. 249, Seção III "Da Exportação" art. 250),
confirmado linha a linha no texto oficial:

- Art. 244: regime específico do IBS/CBS para todas as modalidades lotéricas, apostas de quota
  fixa ("bets"), *sweepstakes*, turfe e *fantasy sport* (e, por parágrafo único, *fantasy sport*
  propriamente dito).
- Art. 245: base de cálculo = **receita própria** (arrecadação total menos premiações pagas e
  destinações obrigatórias por lei a órgão/fundo público e demais beneficiários); parágrafo único
  afasta a incidência sobre as premiações pagas.
- Art. 246: alíquota do IBS/CBS **nacionalmente uniforme**, correspondente à **soma das alíquotas
  de referência das esferas federativas** — sem variação por Estado/Município (o texto não prevê
  redução percentual sobre essa soma, diferente do que ocorre em saúde/hotelaria/bares).
- Art. 247: veda o creditamento ao apostador (consumidor final da aposta não é contribuinte e não
  se credita, o que é a regra geral para consumidor final, mas o artigo reforça isso
  explicitamente para o setor).
- Art. 248: obrigação acessória da operadora (local da aposta, valores apostados e premiados;
  identificação do apostador quando a aposta é virtual).
- Art. 249 (Seção II): importação de serviços de concursos de prognósticos, com fator de redução
  de base previsto em regulamento.
- Art. 250 (Seção III): exportação — serviços prestados por meio virtual a residente/domiciliado
  no exterior são imunes.

Link do PDF fonte (texto oficial consolidado):
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

## 2. Regra específica — em que difere do regime geral

No regime geral, a base de cálculo é o valor bruto da operação (o preço cobrado). Nas apostas, o
"preço" não é um conceito aplicável da mesma forma: o apostador paga um valor pela aposta, mas a
operadora só fica com uma fração dele — o restante retorna como premiação ou é destinado
obrigatoriamente a terceiros por lei (fundos, entidades esportivas, arrecadação social). Por isso a
LC 214/2025 usa uma base sobre a **receita própria da operadora**, não sobre o valor total apostado:

```
Base de cálculo = Total arrecadado em apostas
                   − Premiações pagas aos apostadores
                   − Destinações obrigatórias por lei
```

Diferenças estruturais frente ao regime geral:

1. **Base líquida de premiação**, análoga (mas não idêntica) à técnica usada para seguros e planos
   de saúde — o tributo incide sobre a "margem" econômica da operadora, não sobre o giro bruto.
2. **Alíquota nacionalmente uniforme** (art. 246) — rompe com a lógica do IBS de alíquota
   fracionada por ente federativo de destino, tratando o setor como caso de uniformização nacional
   (semelhante à monofasia de combustíveis nesse aspecto de uniformidade, embora a mecânica de
   base seja diferente).
3. **Vedação expressa ao crédito do apostador** (art. 247) — reforça que o consumidor final não
   pode compensar nada, o que evita disputas sobre eventual "prêmio líquido de tributo".

## 3. Exemplo de cálculo numérico

**Cenário hipotético**: plataforma de apostas de quota fixa recebe, em um mês, R$ 50.000.000 em
apostas; paga R$ 42.000.000 em premiações aos apostadores vencedores; e tem R$ 500.000 de
destinação obrigatória por lei (ex.: repasse a entidades desportivas).

```
Base de cálculo = 50.000.000 − 42.000.000 − 500.000 = 7.500.000
```

Aplicando a alíquota uniforme nacional (art. 246) — o valor numérico exato dessa alíquota **não
foi confirmado nesta pesquisa** (ver Lacunas); usando a soma referencial ilustrativa de ~17,7%
(a mesma referência do regime geral, citada apenas para dar ordem de grandeza, não como dado legal
confirmado para o setor):

```
IBS + CBS ≈ 7.500.000 × 17,7% ≈ R$ 1.327.500
```

Contraste: se a base fosse (erroneamente) o valor bruto apostado, o tributo seria
`50.000.000 × 17,7% ≈ R$ 8.850.000` — mais de 6× o valor correto. Isso demonstra por que a
mecânica de "receita própria" não é um detalhe cosmético: é uma base de cálculo qualitativamente
diferente do valor da operação usado no regime geral.

## 4. Fontes consultadas

- LC 214/2025 (texto oficial consolidado, norma atualizada, Câmara dos Deputados) — arts. 244 a
  250, lidos literalmente.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — tema não coberto nos 17
  mapeados anteriormente.

## 5. Lacunas conhecidas

- **Valor numérico da alíquota de referência de cada esfera federativa** (que compõe a soma
  uniforme do art. 246) ainda não foi fixado por resolução do Senado — o exemplo usa ~17,7% apenas
  como ordem de grandeza ilustrativa; já está confirmado, porém, que o art. 246 **não prevê
  redução percentual** sobre essa soma (diferente de saúde/hotelaria/bares).
- **Lista taxativa de "destinações obrigatórias por lei"** dedutíveis da base — não detalhada nesta
  pesquisa; pode remeter à Lei 13.756/2018 (loterias) e à Lei 14.790/2023 (apostas de quota fixa),
  que não foram consultadas.
- Regulamentação da retenção na fonte/split payment para apostas online (fluxo financeiro passa por
  meios de pagamento eletrônico) — não pesquisado.
- Jurisprudência: tema novo, setor "bets" ainda em consolidação regulatória mesmo fora do âmbito
  tributário (regulação SPA/Ministério da Fazenda) — sem precedentes aplicáveis ao IBS/CBS.
