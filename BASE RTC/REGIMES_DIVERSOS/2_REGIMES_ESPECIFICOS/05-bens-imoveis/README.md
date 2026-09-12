# Bens Imóveis e Construção Civil — Redutor de Ajuste e Tributação por Fluxo de Pagamento

## 1. Fundamento legal

LC 214/2025, Título V "Dos Regimes Específicos do IBS e da CBS", Capítulo V "Dos Bens Imóveis" —
**arts. 251 a 263+** — texto oficial consolidado (norma atualizada, com as alterações da LC
227/2025, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
O mapa antigo (`fontes-legais/mapa-lc214-artigos.json`, arts. 183-198) usava numeração
**incorreta/desatualizada e não deve mais ser usado** para este tema — a numeração confirmada por
leitura direta do texto oficial é a que segue.

Estrutura interna confirmada do Capítulo V:

- **Seção I — Disposições Gerais (arts. 251-253)**: art. 251 sujeita ao regime específico as
  operações com bens imóveis de contribuintes do regime regular (e define quando pessoa física se
  torna contribuinte); art. 252 lista as operações alcançadas (alienação, direitos reais, locação,
  administração/intermediação, construção civil); art. 253 trata de locação residencial de curta
  duração (≤ 90 dias), equiparada a hotelaria.
- **Seção II — Do Momento da Ocorrência do Fato Gerador (art. 254)**.
- **Seção III — Da Base de Cálculo**: Subseção I "Disposições Gerais" — **art. 255** (base = valor
  da operação/locação/direitos reais/administração/construção) e art. 256 (valor de referência);
  Subseção II "Do Redutor de Ajuste" — **art. 257** (institui o redutor de ajuste vinculado a cada
  imóvel, usado para abater da base o valor de aquisição do imóvel) e **art. 258** (valor inicial do
  redutor de ajuste e regras de rateio em divisão/fusão de imóveis); Subseção III "Do Redutor
  Social" — **art. 259** (redutor social de R$ 100.000 por imóvel residencial novo ou R$ 30.000 por
  lote residencial, na **alienação**, aplicado após o redutor de ajuste) e **art. 260** (redutor
  social de R$ 600/mês por imóvel, na **locação residencial**).
- **Seção IV — Da Alíquota (art. 261)**: o *caput* reduz em **50%** as alíquotas do IBS/CBS sobre
  **todas** as operações deste Capítulo; o **parágrafo único** reduz especificamente em **70%** as
  alíquotas sobre locação, cessão onerosa e arrendamento de bens imóveis (correção relevante: a
  redução de 70% não é a regra geral do Capítulo, é uma exceção mais favorável só para locação —
  o restante das operações tem redução de 50%).
- **Seção V — Da Incorporação Imobiliária e do Parcelamento de Solo (art. 262)**: o IBS/CBS
  incidente na alienação de unidades imobiliárias é devido **"em cada pagamento"** — tributação por
  fluxo de recebimento, não no fechamento do contrato de compra e venda.
- Seção VI — Da Sujeição Passiva (art. 263 e seguintes).

## 2. Regra específica — em que difere do regime geral

1. **Redutor de ajuste (arts. 257-258)**: no regime geral, a base é o valor integral da operação.
   Na venda de imóvel, o valor de aquisição do imóvel (equivalente, em geral, ao custo do terreno
   mais construção anterior) é vinculado ao imóvel como redutor de ajuste (art. 257) e abatido da
   base de cálculo na alienação — evitando tributar como valor agregado pela atividade econômica do
   incorporador aquilo que já correspondia a um valor de aquisição anterior.
2. **Redutor Social (arts. 259-260)**: dedução fixa adicional para habitação — R$ 100.000 por
   imóvel residencial novo ou R$ 30.000 por lote residencial na **alienação** (art. 259), aplicada
   **depois** do redutor de ajuste, e R$ 600/mês por imóvel na **locação residencial** (art. 260) —
   descontos que não existem no regime geral.
3. **Alíquota reduzida para todo o Capítulo, com redução adicional para locação (art. 261)**: as
   alíquotas de IBS/CBS sobre as operações deste Capítulo já nascem reduzidas em **50%** frente à
   alíquota padrão do regime geral (*caput*); para locação, cessão onerosa e arrendamento
   especificamente, a redução sobe para **70%** (parágrafo único) — tratando o setor de locação
   imobiliária como estruturalmente diferente do restante da economia (sem o mesmo grau de
   aproveitamento de crédito que uma atividade industrial teria).
4. **Tributação por fluxo de pagamento na incorporação (art. 262)**: em vez de reconhecer o fato
   gerador no fechamento do contrato de venda de uma unidade (como seria a regra geral — regime de
   competência, fato gerador na emissão do documento fiscal), a incorporação reconhece o IBS/CBS
   **a cada parcela efetivamente paga** pelo comprador — regime de caixa parcelado, específico do
   setor, com o redutor de ajuste e o redutor social deduzidos proporcionalmente em cada parcela
   (art. 262, § 4º).

## 3. Exemplo de cálculo numérico

**Cenário**: incorporadora vende unidade residencial nova por R$ 500.000, sendo R$ 150.000
correspondentes ao valor de aquisição do imóvel/redutor de ajuste (art. 257-258) e o imóvel se
qualifica para o Redutor Social de alienação (art. 259, R$ 100.000, imóvel residencial novo).

```
Base antes dos redutores               = 500.000
(–) Redutor de ajuste (art. 257-258)   = 150.000
(–) Redutor Social (art. 259)          = 100.000
Base de cálculo final                   = 250.000
```

Sobre essa base incide a alíquota do IBS/CBS **já reduzida em 50%** por força do art. 261, *caput*
(redução geral do Capítulo). Aplicando a alíquota de referência ilustrativa de ~17,7% do regime
geral, com a redução de 50%:

```
Alíquota efetiva da incorporação = 17,7% × (1 − 50%) = 8,85%
IBS + CBS ≈ 250.000 × 8,85% ≈ R$ 22.125
```

Contraste sem os redutores de base nem a redução de alíquota: `500.000 × 17,7% ≈ R$ 88.500` — cerca
de 4× o valor apurado com a mecânica do regime específico. Além disso, pelo art. 262, esse valor
não é recolhido de uma vez no fechamento do contrato: se a venda for financiada em 100 parcelas
mensais de R$ 5.000, o IBS/CBS de cada parcela é apurado proporcionalmente **no momento do
recebimento**, com o redutor de ajuste e o redutor social também rateados por parcela (art. 262,
§ 4º).

**Locação (art. 261, parágrafo único)**: para um aluguel residencial de R$ 10.000/mês, a redução
de alíquota é de **70%** (maior que a redução geral de 50% do Capítulo), e ainda incide o redutor
social de locação de R$ 600/mês (art. 260):

```
Base = 10.000 − 600 (redutor social, art. 260) = 9.400
Alíquota efetiva = 17,7% × (1 − 70%) = 5,31%
IBS + CBS do mês ≈ 9.400 × 5,31% ≈ R$ 499
```

## 4. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada com a LC 227/2025, Câmara dos
  Deputados) — leitura direta dos arts. 251 a 263, confirmando *caput*, seções/subseções e
  parágrafos relevantes (inclusive a distinção entre a redução geral de 50% do art. 261, *caput*, e
  a redução de 70% do parágrafo único, específica para locação).
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — mapa antigo (arts.
  183-198) identificado como desatualizado para este tema; não usar mais essa numeração.
- Decreto 12.955/2026 (arts. 370-374) e Resolução CGIBS nº 6/2026, citados em pesquisa anterior
  como fonte regulamentar complementar do redutor de ajuste — não lidos diretamente nesta rodada.

## 5. Lacunas conhecidas

- **Alíquota de referência numérica do regime geral** (usada no exemplo como ~17,7% ilustrativo)
  ainda depende de ato do Comitê Gestor/Poder Executivo para cada ano-calendário — o exemplo usa um
  valor de referência apenas para dimensionar, não é a alíquota oficialmente publicada.
- **Fórmula exata de apuração do redutor de ajuste quando não há segregação contratual clara entre
  terreno e construção** — o art. 257/258 tratam do valor de aquisição em geral, mas casos-limite de
  segregação não foram aprofundados nesta leitura.
- **Créditos sobre materiais de construção** citados no mapa antigo (183-198) — não localizados
  como dispositivo específico dentro do Capítulo V lido nesta rodada; pode estar no regime geral de
  créditos (Título I) em vez de uma regra própria deste Capítulo — não confirmado.
- Regulamentação infralegal (Decreto 12.955/2026, Resolução CGIBS nº 6/2026) sobre a operacionalização
  do redutor de ajuste — referenciada mas não lida diretamente nesta rodada.
