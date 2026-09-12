# 1_REGIMES_DIFERENCIADOS — Setores com Redução de Alíquota (60%, Zero ou Isenção) na Sistemática Geral

Esta pasta reúne 12 segmentos da LC 214/2025 que recebem **redução de alíquota** (60%, 100%/
alíquota zero, ou isenção — pasta 08) mas seguem a **sistemática geral de apuração** do IBS/CBS
(débito menos crédito, não cumulatividade plena, Split Payment, período mensal) — sem regra de
cálculo própria. Isso os distingue dos "Regimes Específicos" (outra pasta deste bloco
`REGIMES_DIVERSOS`, com fórmulas e regras de crédito próprias).

Todos os valores de exemplo usam o cronograma REAL de transição já extraído do código de produção
da plataforma Guerra RTC (`aliquotas-transicao/cronograma-aliquotas.json`, referencial de exemplo
CBS 8,50% / IBS 5,00%): em 2027, CBS fixo 8,40% + IBS fixo 0,10% = 8,50% total; em 2033 (regime
pleno), CBS 8,50% + IBS 5,00% (100% do referencial) = 13,50% total. A redução setorial (60% ou
100%) incide apenas sobre a soma CBS+IBS — o ICMS/ISS residual da transição segue seu próprio
cronograma de extinção, sem desconto adicional pela redução setorial.

## Fonte desta rodada de correção

Esta rodada corrigiu a numeração de artigo dos 12 READMEs a partir do **texto integral oficial
consolidado da LC 214/2025** — "norma atualizada" (já incorpora as alterações da LC 227/2025),
publicado pelo Centro de Documentação e Informação da Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

Essa é uma fonte de maior autoridade que o RAG local usado na rodada anterior (que continha uma
numeração desatualizada, provavelmente de uma versão anterior do projeto de lei). Todos os artigos
listados na tabela abaixo foram confirmados por leitura literal deste texto oficial.

## Tabela-resumo

| Pasta | Resumo (1 linha) | Artigo(s) | % Redução | Status |
|---|---|---|---|---|
| `01-servicos-educacao` | Serviços de educação do Anexo II (creche a ensino superior) | art. 129 | 60% | Confirmado por fonte oficial |
| `02-servicos-saude` | Serviços de saúde do Anexo III (planos, hospitalar), exclui glosas médicas da base | art. 130 | 60% | Confirmado por fonte oficial |
| `03-dispositivos-medicos-acessibilidade` | Regime DUPLO: lista ampla (Anexo IV/V) a 60% + lista restrita (Anexo XII/XIII) a zero | arts. 131, 132 (60%) e 144, 145 (zero) | 60% e 100% | Confirmado por fonte oficial |
| `04-medicamentos` | Regime DUPLO: medicamentos Anvisa/manipulação (Anexo VI) a 60% + lista de doenças/programas específicos a zero | arts. 133/134 (60%) e 146 (zero) | 60% e 100% | Confirmado por fonte oficial |
| `05-produtos-saude-menstrual` | Tampões, absorventes e coletores menstruais (NCM 9619.00.00), condicionado a norma Anvisa | art. 147 | 100% | Confirmado por fonte oficial |
| `06-cesta-basica-nacional` | Alimentos essenciais da Cesta Básica Nacional (Anexo I) — capítulo próprio, distinto do art. 135 (alimentos em geral, 60%) | art. 125 | 100% | Confirmado por fonte oficial (corrige numeração antiga "arts. 63-66") |
| `07-producoes-artisticas-culturais-jornalisticas-audiovisuais` | Cessão de direitos de obras nacionais (autor/intérprete brasileiro) | art. 139 | 60% | Confirmado por fonte oficial |
| `08-transporte-publico-coletivo` | Transporte público coletivo rodoviário e metroviário urbano/semiurbano/metropolitano — ISENÇÃO (não redução percentual) | art. 157 | Isenção (100%) | Confirmado por fonte oficial (corrige hipótese antiga de enquadramento como Regime Específico) |
| `09-insumos-agropecuarios-aquicolas` | Sementes, mudas, fertilizantes, defensivos do Anexo IX, com diferimento em cadeia B2B (§§ 2º-3º) | art. 138 | 60% | Confirmado por fonte oficial |
| `10-produtos-horticolas-frutas-ovos` | Produtos hortícolas, frutas e ovos do Anexo XV — IBS e CBS ambos confirmados a zero | art. 148 | 100% | Confirmado por fonte oficial |
| `11-atividades-desportivas` | Educação desportiva e clubes filiados (SAF/futebol profissional é regime específico à parte, fora de escopo) | art. 141 | 60% | Confirmado por fonte oficial |
| `12-seguranca-soberania-nacional` | Bens/serviços de segurança nacional/cibernética — dois gatilhos distintos (comprador público OU sócio brasileiro ≥20%) | art. 142 | 60% | Confirmado por fonte oficial |

## Achados desta rodada de correção

1. **Dois segmentos tinham a numeração de artigo errada e foram corrigidos com base na fonte
   oficial**:
   - `06-cesta-basica-nacional`: o fundamento correto é o **art. 125** (Título III, Capítulo II
     "Da Cesta Básica Nacional de Alimentos"), não o intervalo "arts. 63-66" herdado de uma rodada
     anterior. Existe também o art. 135 ("Alimentos Destinados ao Consumo Humano", redução de
     60%), que é uma categoria distinta e mais ampla — não a cesta básica em si.
   - `08-transporte-publico-coletivo`: o fundamento correto é o **art. 157** (Título IV, Capítulo
     V — mesmo Título dos Regimes Diferenciados), uma **isenção** de IBS e CBS para transporte
     rodoviário e metroviário urbano/semiurbano/metropolitano sob autorização, permissão ou
     concessão pública. O segmento está corretamente classificado neste bloco (Regimes
     Diferenciados) — a hipótese anterior de que fosse um Regime Específico estava equivocada.
     Existe um regime **diferente e separado** para transporte coletivo intermunicipal/
     interestadual (arts. 284-287, Regime Específico, redução de 40%), mapeado por outro processo
     no bloco `2_REGIMES_ESPECIFICOS`.
2. **Todos os demais 10 segmentos já tinham a numeração correta** (confirmada anteriormente por
   RAG local ou inferida por sequência), e foram agora **confirmados por citação literal direta**
   do texto oficial consolidado, eliminando as ressalvas de "não confirmado" / "inferido por
   sequência" que constavam nas versões anteriores dos READMEs — notavelmente a pasta 07
   (produções artísticas/culturais, antes só inferida como art. 139, agora confirmada), a pasta 03
   (arts. 131/132 antes inferidos, agora confirmados), a pasta 10 (confirmado que o art. 148 zera
   tanto IBS quanto CBS, não só IBS) e a pasta 12 (confirmado que o art. 142 reduz tanto IBS
   quanto CBS, não só CBS).
3. **O mapa estático pré-existente da base (`fontes-legais/mapa-lc214-artigos.json`) continua com
   uma imprecisão de faixa de artigo** identificada na pasta 09 ("Produtor Rural e Agronegócio:
   arts. 128-137", que não corresponde ao texto oficial — arts. 128-142 são o Capítulo "Da Redução
   em 60%" cobrindo os 13 setores deste bloco). Recomenda-se corrigir esse mapa estático numa
   próxima manutenção.
4. **Nenhuma jurisprudência (CARF/STJ/STF/CJF)** foi pesquisada para nenhum dos 12 segmentos nesta
   rodada — a lei é de 2025 e o regime de transição só começa em 2027, então não há jurisprudência
   consolidada esperável ainda sobre a aplicação concreta desses artigos.
5. **Exemplos reais de mercado**: seguem pendentes de leitura integral um estudo de caso de
   distribuidora de medicamentos (pasta 04) e uma planilha de contribuições do próprio escritório
   sobre a regulamentação do transporte rodoviário (pasta 08), ambos já localizados em rodada
   anterior no Google Drive do escritório. Para os demais 10 segmentos, nenhum material específico
   de cliente real foi localizado.
6. **Lacunas estruturais remanescentes** (não resolvidas por leitura do texto legal, pois dependem
   de atos infralegais ainda não publicados ou de Anexos não extraídos integralmente): listas
   completas de Anexos (II, III, IV, V, VI, IX, X, XI, XII, XIII, XV e o Anexo I da cesta básica),
   e definição de normas técnicas complementares (ex.: norma da Anvisa referida no art. 147). Essas
   não são lacunas de pesquisa desta rodada — são listas publicadas em Anexo da própria lei, cuja
   extração integral fica para uma rodada dedicada a mapear cada Anexo por completo.
