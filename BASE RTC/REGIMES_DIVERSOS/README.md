# REGIMES_DIVERSOS — Regimes Diferenciados, Específicos e Aduaneiros (LC 214/2025)

Base canônica dos tratamentos tributários fora da sistemática padrão do IBS/CBS, organizada em
3 blocos conforme a natureza do tratamento — não confundir um com o outro:

| Bloco | Natureza | O que muda | Pasta |
|---|---|---|---|
| 1 | **Regimes Diferenciados** | Só a **alíquota** (60% ou zero/isenção) — apuração, base e crédito seguem a regra geral | `1_REGIMES_DIFERENCIADOS/` |
| 2 | **Regimes Específicos** | A **mecânica de cálculo** (base, crédito, forma de apuração) é própria do setor | `2_REGIMES_ESPECIFICOS/` |
| 3 | **Regimes Aduaneiros Especiais** | Suspensão/diferimento de IBS/CBS na importação (drawback, admissão temporária, entreposto) | `3_REGIMES_ADUANEIROS_ESPECIAIS/` |

26 segmentos ao todo (25 originalmente pedidos + 1 achado durante a pesquisa — transporte coletivo
intermunicipal/interestadual, ver abaixo). Cada subpasta tem `README.md` com: fundamento legal
(artigo da LC 214/2025 confirmado por citação literal), regra/mecânica, exemplo de cálculo numérico
2027 vs. 2033 (cronograma real de `aliquotas-transicao/cronograma-aliquotas.json`), fontes
consultadas e lacunas conhecidas.

- [`1_REGIMES_DIFERENCIADOS/README.md`](1_REGIMES_DIFERENCIADOS/README.md) — 12 segmentos
- [`2_REGIMES_ESPECIFICOS/README.md`](2_REGIMES_ESPECIFICOS/README.md) — 13 segmentos (12 pedidos + transporte intermunicipal/interestadual)
- [`3_REGIMES_ADUANEIROS_ESPECIAIS/README.md`](3_REGIMES_ADUANEIROS_ESPECIAIS/README.md) — 1 segmento

## Numeração de artigos: reconciliada com fonte oficial (resolvido em 2026-08-27)

A primeira rodada desta base (pesquisa via RAG local) encontrou divergências entre o mapa legal
pré-existente (`fontes-legais/mapa-lc214-artigos.json`) e a numeração real da lei, mas não pôde
confirmar qual estava certo — o fetch direto a `planalto.gov.br` falhou (rede bloqueada nesta
máquina). Numa segunda rodada, foi localizado e baixado o **texto oficial consolidado da LC
214/2025** ("norma atualizada", já incorporando as alterações da LC 227/2025), publicado pelo
Centro de Documentação e Informação da Câmara dos Deputados:

`https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf`
(298 páginas — texto extraído e usado para confirmar, artigo por artigo, cada citação desta base).

**Todos os 26 segmentos foram reconciliados contra esse texto oficial.** Correções mais relevantes
em relação à primeira rodada e ao mapa antigo:

| Segmento | Estava (errado) | Confirmado (oficial) |
|---|---|---|
| Cesta Básica Nacional | arts. 63-66 | **art. 125** (capítulo próprio, Título III) |
| Produtor Rural (crédito presumido) | arts. 128-137 | **art. 164** (Título IV, Cap. VII) — 128-142 é na verdade o capítulo "Redução em 60%" (12 setores diferentes) |
| Serviços Financeiros | arts. 167-182 | **art. 181-233** |
| Bens Imóveis | arts. 183-198 | **art. 251-265** |
| Simples Nacional (creditamento restrito do tomador) | art. 127 | **art. 47, § 9º, inciso II** — art. 127 é, na verdade, a Redução de 30% para 18 profissões regulamentadas, sem nenhuma relação com SN |
| Transporte público coletivo urbano | classificação em dúvida (Regime Diferenciado ou Específico?) | **Regime Diferenciado confirmado — art. 157, isenção** (não uma fração de redução) |

O arquivo `fontes-legais/mapa-lc214-artigos.json` (base pré-existente, fora desta pasta) também foi
corrigido nestes 5 pontos, com nota de revisão registrando a fonte e o motivo.

### Achado extra: dois regimes de transporte coletivo diferentes

A dúvida sobre onde classificar "transporte público coletivo" revelou que a lei trata **dois
regimes distintos**, ambos reais e ambos agora documentados:

- **Urbano/semiurbano/metropolitano** (art. 157) — **isenção total**, Regime Diferenciado, bloco 1, pasta `08-transporte-publico-coletivo`.
- **Intermunicipal/interestadual** (arts. 284-287) — Regime Específico, bloco 2, pasta nova `13-transporte-coletivo-intermunicipal-interestadual`. Dentro dele, o art. 285 (ferroviário/hidroviário urbano) tem 100% de redução com vedação total de crédito — regime ainda mais restritivo que os 40% do art. 286/287 (rodoviário/aéreo).

## Lacunas remanescentes (estruturais, não de pesquisa)

Estas não são falhas da pesquisa — são dados que só existem quando o Comitê Gestor do IBS/RFB
publicar os atos correspondentes, hoje inexistentes:

- Coeficientes de crédito presumido (produtor rural, Zona Franca de Manaus) dependem de ato anual do Comitê Gestor/Ministério da Fazenda — ainda não publicado.
- Listas completas de Anexos (II, III, IV, V, VI, IX, X, XI, XII, XIII, XV — dispositivos médicos, medicamentos, insumos agropecuários etc.) não foram transcritas integralmente; os READMEs citam o artigo que remete ao Anexo, não o Anexo em si.
- Nenhuma jurisprudência (CARF/STJ/STF/CJF) foi pesquisada — a transição só começa em 2027, não há litígio consolidado esperável ainda.
- Regulamentação infralegal (decretos, resoluções CGIBS) não foi lida sistematicamente — apenas o que já havia sido localizado nas rodadas anteriores (Decreto 12.955/2026, Resolução CGIBS nº 6/2026).

## Próximos passos recomendados

1. Avaliar se `cadeia-negocios-creditos/` (base pré-existente) precisa de alguma correção adicional relacionada ao achado do art. 47 §9º — verificado nesta rodada que o JSON de regras de negócio não cita artigo de lei diretamente, então não há erro a corrigir lá, mas a anotação cruzada em `fontes-legais/mapa-lc214-artigos.json` já foi corrigida.
2. Transcrever os Anexos citados (II, III, IV, V, VI, IX-XV) quando o objetivo for uso em parecer que dependa da lista exata de produtos/serviços.
3. Retomar pesquisa de jurisprudência a partir de 2027, quando a transição gerar litígio concreto.
