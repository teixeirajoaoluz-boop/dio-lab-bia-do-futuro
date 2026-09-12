# Insumos Agropecuários e Aquícolas — Redução de 60%

## 1. Fundamento legal

**Confirmado por leitura literal do texto oficial consolidado** — LC 214/2025, art. 138 (Capítulo
"Da Redução em 60%", Seção X — Dos Insumos Agropecuários e Aquícolas), texto oficial consolidado
(norma atualizada, já incorpora as alterações da LC 227/2025), Centro de Documentação e Informação
da Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

> "Seção X Dos Insumos Agropecuários e Aquícolas
> Art. 138. Ficam reduzidas em 60% (sessenta por cento) as alíquotas do IBS e da CBS incidentes
> sobre o fornecimento dos insumos agropecuários e aquícolas relacionados no Anexo IX desta Lei
> Complementar, com a especificação das respectivas classificações da NCM/SH e da NBS.
> § 1º A redução de alíquotas prevista no caput deste artigo somente se aplica aos produtos de
> que trata o Anexo IX desta Complementar que, quando exigido, estejam registrados como insumos
> agropecuários ou aquícolas no órgão competente do Ministério da Agricultura e Pecuária.
> § 2º Fica diferido o recolhimento do IBS e da CBS incidentes nas seguintes operações com
> insumos agropecuários e aquícolas de que trata o caput:
> I - fornecimento realizado por contribuinte sujeito ao regime regular do IBS e da CBS para:
> a) contribuinte sujeito ao regime regular do IBS e da CBS; e
> b) produtor rural não contribuinte do IBS e da CBS que utilize os insumos na produção de bem
> vendido para adquirentes que têm direito à apropriação dos créditos presumidos estabelecidos
> pelo art. 168 desta Lei Complementar; e
> II - importação realizada por: a) contribuinte sujeito ao regime regular do IBS e da CBS; e
> b) produtor rural não contribuinte do IBS e da CBS nas mesmas condições da alínea 'b' do inciso
> I.
> § 3º O diferimento de que tratam a alínea 'b' do inciso I e a alínea 'b' do inciso II, ambos do
> § 2º, somente será aplicado sobre a parcela de insumos utilizada pelo produtor rural não
> contribuinte na produção de bem vendido para adquirentes que têm direito à apropriação dos
> créditos presumidos estabelecidos pelo art. 168."

O texto completo do § 2º (antes cortado na fonte do RAG local) confirma que o diferimento cobre
duas hipóteses de fornecimento (B2B regular e venda a produtor rural não contribuinte vinculado a
créditos presumidos do art. 168) mais a importação nas mesmas condições — resolvendo a lacuna da
rodada anterior sobre o teor completo do dispositivo.

**Importante — não confundir com o art. 137** (Seção anterior, "Dos Produtos Agropecuários,
Aquícolas, Pesqueiros, Florestais e Extrativistas Vegetais In Natura"), que trata do PRODUTO
agropecuário final in natura (item VIII do rol de 60%), também reduzido em 60%, mas é um
dispositivo diferente do art. 138 (que trata dos INSUMOS usados na produção — sementes, mudas,
fertilizantes, rações, defensivos etc., item IX do rol). Os dois são segmentos juridicamente
distintos ainda que vizinhos e com o mesmo percentual.

**Nota sobre a base já existente**: o mapa estático pré-existente desta base
(`fontes-legais/mapa-lc214-artigos.json`) cita um tema "Produtor Rural e Agronegócio" com artigos
"128 a 137" — essa faixa **não corresponde** ao que a pesquisa desta rodada confirmou (arts. 128 a
142 são, na verdade, o Capítulo "Da Redução em 60%" cobrindo educação/saúde/dispositivos/
medicamentos/agro/cultura/desporto/segurança — não um capítulo específico de "Produtor Rural").
Isso é uma **divergência confirmada** entre o mapa estático já existente (gerado por uma rodada
anterior via `fonte_lc214_mapa_temas`, sem fetch de confirmação literal) e o texto oficial
consolidado da lei, lido nesta rodada — os números confirmados nesta pasta (137, 138) são os
corretos; recomenda-se corrigir o mapa estático em manutenção futura.

## 2. Regra

- **Percentual de redução**: 60% sobre IBS e CBS.
- **Aplica-se a**: bens — insumos agropecuários e aquícolas listados no Anexo IX (sementes, mudas,
  fertilizantes, defensivos, rações etc., por classificação NCM/SH e NBS).
- **Condicionante**: quando exigido, o produto precisa estar registrado como insumo agropecuário
  ou aquícola no órgão competente do Ministério da Agricultura e Pecuária.
- **Regra adicional de diferimento (§ 2º e § 3º)**: em duas hipóteses B2B — (i) fornecimento entre
  contribuintes do regime regular, e (ii) fornecimento/importação para produtor rural não
  contribuinte que use o insumo na produção de bem vendido a adquirente com direito a crédito
  presumido do art. 168 — o recolhimento do IBS/CBS é DIFERIDO, limitado, na segunda hipótese, à
  parcela efetivamente usada nessa produção. Além do desconto de 60% na alíquota, há uma regra de
  postergação do momento do pagamento do tributo devido.

## 3. Como funciona na prática

Sistemática geral de apuração (débito-crédito, mensal, Split Payment), com duas camadas extras:
(1) a alíquota nominal já sai com 60% de desconto para os itens do Anexo IX; (2) para operações
específicas do § 2º, o recolhimento não ocorre no mês do fato gerador, mas é diferido para uma
etapa posterior da cadeia — isso é uma regra de MOMENTO de recolhimento, distinta da regra de
alíquota, e precisa ser modelada separadamente se a plataforma Guerra RTC vier a implementar este
segmento.

## 4. Exemplo de cálculo numérico

Operação hipotética: R$ 100.000,00 em vendas de insumos agropecuários do Anexo IX (sem considerar
o diferimento do § 2º, referencial CBS 8,50% / IBS 5,00%):

| Ano | Regime GERAL | Redução de 60% (insumo agropecuário/aquícola) |
|---|---|---|
| 2027 | 8,50% → **R$ 8.500,00** | 3,40% → **R$ 3.400,00** |
| 2033 | 13,50% → **R$ 13.500,00** | 5,40% → **R$ 5.400,00** |

## 5. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, Câmara dos Deputados) — leitura
  literal do art. 138, incluindo o texto completo dos §§ 2º e 3º (diferimento).
- MCP `mcp-rag-reforma` — `Material Base\Lcp 214_ATUALIZADA.pdf`,
  `Mentoria_Consultoria_Reforma Tributária\Thompson - Dominio Sistemas\ANTES\Produtor Rural e
  Agro (1).docx`, `Material Base\Reforma Tributária - LCP 214-2025.docx`.
- MCP `mcp-compliance` — mapa estático (`fontes-legais/mapa-lc214-artigos.json`) — divergência
  identificada e registrada acima (faixa "128-137" do mapa antigo não bate com a confirmação
  direta desta rodada).
- `aliquotas-transicao/cronograma-aliquotas.json`.
- Google Drive: encontrado material do cliente Thompson Reuters sobre "Produtor Rural e
  Agronegócio" já indexado no RAG (`Mentoria_Consultoria_Reforma Tributária\Thompson - Dominio
  Sistemas\ANTES\`), incluindo uma ata de posicionamentos técnicos em reunião de 26/06/2025 sobre
  tributação do produtor rural — **não foi lida integralmente** nesta rodada, é uma fonte real de
  cliente sobre o tema correlato (produtor rural), embora não seja especificamente sobre insumos.
- Projeto BUFON & FRASSON RTC: nenhum classificador específico de insumos agropecuários
  encontrado.
- MindMeister: nenhum mapa relevante.

## 6. Lacunas conhecidas

1. **Anexo IX completo** não foi extraído.
2. **Divergência com o mapa estático pré-existente** ("Produtor Rural e Agronegócio, arts.
   128-137") confirmada acima — recomenda-se corrigir essa imprecisão no arquivo
   `fontes-legais/mapa-lc214-artigos.json` da base raiz em uma próxima rodada de manutenção.
3. **Ata de reunião Thompson Reuters** sobre produtor rural não foi lida integralmente.
4. **Nenhuma jurisprudência** pesquisada nesta rodada.
