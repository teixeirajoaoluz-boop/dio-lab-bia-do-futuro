# Combustíveis e Biocombustíveis — Monofasia de IBS/CBS

## 1. Fundamento legal

LC 214/2025, Título V "Dos Regimes Específicos do IBS e da CBS", Capítulo I "Dos Combustíveis" —
**arts. 172 a 180** — texto oficial consolidado (norma atualizada, com as alterações da LC
227/2025, Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).
Estrutura interna confirmada por leitura direta do texto:

- **Seção I — Disposições Gerais (art. 172)**: incidência única (monofásica) do IBS e da CBS sobre
  combustíveis — gasolina e suas correntes, etanol anidro combustível (EAC), óleo diesel e suas
  correntes, biodiesel (B100), GLP, etanol hidratado combustível (EHC), querosene de aviação, óleo
  combustível, gás natural processado, biometano, GNV, entre outros listados no *caput*.
- **Seção II — Da Base de Cálculo (art. 173)**: a base é a **quantidade** de combustível objeto da
  operação (aferida pela unidade de medida própria de cada produto), e o tributo devido é a
  multiplicação dessa quantidade pela **alíquota específica** aplicável.
- **Seção III — Das Alíquotas (arts. 174 e 175)**: art. 174 fixa as alíquotas específicas por
  unidade de medida, uniformes em todo o território nacional; art. 175 assegura aos biocombustíveis
  e ao hidrogênio de baixa emissão de carbono carga tributária **inferior** à dos combustíveis
  fósseis equivalentes — o diferencial é limitado por lei a **não menos de 40% nem mais de 90%** das
  alíquotas incidentes sobre o fóssil comparado (art. 175, § 1º).
- **Seção IV — Da Sujeição Passiva (art. 176)**: define os contribuintes do regime monofásico —
  produtor nacional de biocombustíveis, refinaria de petróleo e suas bases, Central de Matéria-Prima
  Petroquímica (CPQ), Unidade de Processamento de Gás Natural (UPGN), formulador de combustíveis,
  importador e demais agentes produtores autorizados.
- Seção V (arts. 178-179) trata das operações com EAC; **Seção VI (art. 180)** veda o creditamento
  na aquisição de combustíveis monofásicos destinados a distribuição/comercialização/revenda (o
  distribuidor/revendedor não se credita do IBS/CBS pago na aquisição).

O Capítulo II "Dos Serviços Financeiros" começa logo em seguida, no art. 181 — ver README do tema
02.

## 2. Regra específica — em que difere do regime geral

O regime geral do IBS/CBS é **plurifásico e ad valorem**: cada elo da cadeia apura débito sobre o
valor da operação e se credita do imposto pago na etapa anterior (não cumulatividade plena, arts.
28-47 da LC 214/2025). Combustíveis fósseis e biocombustíveis rompem com essa lógica em dois
pontos:

1. **Concentração em um único elo (monofasia)**: o tributo é cobrado uma única vez, na saída do
   produtor/refinaria/CPQ/UPGN (art. 176), e as etapas seguintes da cadeia (distribuição, revenda,
   posto de combustível) **não apuram débito nem crédito** sobre o produto monofásico — o art. 180
   veda expressamente o crédito na aquisição para revenda.
2. **Base específica por unidade de medida (quantidade), não pelo valor da operação** (art. 173): a
   alíquota é específica por unidade de medida (art. 174), igual em todo o território nacional, e
   não em percentual sobre o preço de venda — diferente de todo o resto do regime geral, onde a
   alíquota é sempre ad valorem.

Isso significa que **o preço de venda ao consumidor final não altera o valor do tributo
recolhido por litro** — ao contrário do regime ad valorem, em que um aumento de preço aumenta
proporcionalmente o IBS/CBS devido.

## 3. Exemplo de cálculo numérico

**Cenário**: refinaria vende 100.000 litros de diesel à distribuidora; a distribuidora revende à
rede de postos; o posto vende ao consumidor final.

### Regime geral (ad valorem) — para contraste, valores hipotéticos do cronograma de transição

Se diesel fosse tributado pelo regime geral (não é — está aqui só para contraste didático), usando
o cronograma real (`aliquotas-transicao/cronograma-aliquotas.json`): em 2027, CBS fixo 8,40% + IBS
fixo 0,10% sobre o valor de cada venda, com direito a crédito em cada etapa. O tributo cresceria
com o preço.

### Regime monofásico real (arts. 172, 173, 174, 176 e 180)

1. Refinaria vende 100.000 litros. Suponha alíquota específica **X R$/litro** fixada por lei/ato do
   Comitê Gestor (o valor numérico da alíquota específica por litro **não foi confirmado nesta
   pesquisa** — ver Lacunas). O tributo total devido pela refinaria é `100.000 × X`, recolhido uma
   única vez.
2. Distribuidora compra os 100.000 litros: **não há débito nem crédito de IBS/CBS nessa etapa**
   (art. 180) — o preço de compra já embute o tributo pago pela refinaria, mas ele não circula mais
   como crédito na cadeia.
3. Posto de combustível compra da distribuidora e revende ao consumidor: mesma lógica — sem
   débito/crédito adicional de IBS/CBS sobre o combustível monofásico.
4. **Resultado**: o valor total de IBS/CBS embutido no preço final ao consumidor é fixo em
   `100.000 × X`, independentemente de quantas margens de revenda existirem entre a refinaria e o
   posto — diferente do regime ad valorem, em que cada margem geraria débito e crédito adicionais
   (mas com efeito neutro na cadeia, já que o não cumulativo pleno anula o efeito cascata; a
   diferença real do monofásico é que ele **elimina a necessidade de apuração em cada etapa**, não
   que ele mude o valor total arrecadado).

**Biocombustíveis (art. 175)**: se o mesmo volume fosse de biodiesel puro, a alíquota específica
seria **inferior** à do diesel fóssil equivalente, dentro da faixa legal de **40% a 90%** da
alíquota do fóssil comparado (art. 175, § 1º) — o valor exato dentro dessa faixa, para cada
combustível/ano, depende de ato do Comitê Gestor e não foi confirmado nesta pesquisa (ver
Lacunas).

## 4. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada com a LC 227/2025, Câmara dos
  Deputados) — leitura direta dos arts. 172 a 180, confirmando *caput* e parágrafos.
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — confirmado que este tema
  **não está** nos 17 temas já mapeados (é expansão nova desta rodada).
- `C:\GUERRA_MENTORIA_REGRAS RTC\aliquotas-transicao\cronograma-aliquotas.json` — usado apenas como
  contraste do regime geral ad valorem.

## 5. Lacunas conhecidas

- **Valor numérico da alíquota específica por unidade de medida** (art. 174) para cada
  combustível — não localizado nesta pesquisa; depende de ato do Comitê Gestor do IBS/Poder
  Executivo que fixa os valores específicos, ainda não publicado ou não indexado nas fontes
  consultadas.
- **Percentual exato do diferencial competitivo dentro da faixa legal 40%-90%** (art. 175, § 1º)
  para cada biocombustível/ano — a faixa está confirmada no texto da lei, mas o percentual
  específico definido pelo regulamento/Comitê Gestor não foi localizado.
- Regulamentação infralegal (Decreto/Resolução CGIBS) sobre split payment em monofasia — não
  pesquisado; hipótese de trabalho é que, como a cobrança se concentra no produtor/refinaria e não
  há mais elos com débito/crédito, o mecanismo de split payment (arts. 31 a 35, pensado para o
  regime geral B2B) tem aplicação distinta ou reduzida nesta cadeia — não confirmado (o art. 177,
  § 1º, I, apenas menciona a hipótese de liquidação via split como excludente de responsabilidade
  solidária, sem detalhar a mecânica completa).
