# Serviços de Saúde — Redução de 60%

## 1. Fundamento legal

**LC 214/2025, art. 130** (mesmo Capítulo do art. 129, Seção III — Dos Serviços de Saúde):

> "Art. 130. Ficam reduzidas em 60% (sessenta por cento) as alíquotas do IBS e da CBS incidentes
> sobre o fornecimento dos serviços de saúde relacionados no Anexo III desta Lei Complementar, com
> a especificação das respectivas classificações da NBS.
>
> Parágrafo único. Não integram a base de cálculo do IBS e da CBS dos serviços de saúde de que
> trata o caput deste artigo os valores glosados pela auditoria médica dos planos de assistência
> à saúde e não pagos."

**Confirmado por leitura literal do texto oficial consolidado** — LC 214/2025, art. 130, texto
oficial consolidado (norma atualizada, já incorpora as alterações da LC 227/2025), Centro de
Documentação e Informação da Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

Esta é a fonte de maior autoridade disponível para este README — substitui a confirmação da rodada
anterior, que se apoiava no RAG local (`Material Base\Lcp 214_ATUALIZADA.pdf`,
`Mentoria_Consultoria_Reforma Tributária\00_Modelos\REGULAMENTO DA CBS.pdf` e `REGUMANTO DO IBS E
OUTRAS PROVIDÊNCIAS - MAR 26 - 09 (1).docx`).

O **Anexo III** lista os serviços de saúde por código NBS. Um rascunho anterior (PLP 68/2024, que
antecedeu a LC 214/2025 e teve renumeração de artigos) já dava a régua do tipo de item coberto:
serviços cirúrgicos, ginecológicos e obstétricos, psiquiátricos, de UTI, de urgência, hospitalares
em geral, clínica médica, entre outros (fonte: `PLP 68-2024 [EM DISCUSSÃO].pdf` — **atenção**: essa
é a minuta do projeto de lei, não o texto final sancionado; a numeração de itens do Anexo III pode
ter mudado entre o PLP e a LC 214/2025 sancionada — usar apenas como indicativo do TIPO de serviço
coberto, não como lista definitiva).

## 2. Regra

- **Percentual de redução**: 60% sobre IBS e CBS.
- **Aplica-se a**: serviços de saúde listados no Anexo III (planos de assistência à saúde,
  procedimentos médicos/hospitalares listados).
- **Regra de base de cálculo específica**: valores glosados pela auditoria médica dos planos de
  saúde e não pagos **não entram na base de cálculo** — ou seja, o IBS/CBS não incide sobre o
  valor que a operadora de saúde glosou e não efetivamente pagou ao prestador. Essa é uma regra de
  BASE DE CÁLCULO, distinta da alíquota reduzida, e é exclusiva deste artigo.

## 3. Como funciona na prática

Sistemática geral: apuração mensal, não cumulatividade plena, Split Payment. A única
particularidade adicional (além da alíquota 60% menor) é a exclusão da base de cálculo dos valores
glosados — o que exige controle contábil de glosas para não recolher IBS/CBS sobre receita que a
operadora de saúde nunca efetivamente recebeu.

## 4. Exemplo de cálculo numérico

Operação hipotética: R$ 100.000,00 de faturamento de serviços de saúde do Anexo III (sem glosas
para simplificar), usando o mesmo referencial de exemplo da base canônica (CBS 8,50% / IBS 5,00%):

| Ano | CBS+IBS regime GERAL | CBS+IBS com redução de 60% (serviço de saúde) |
|---|---|---|
| 2027 | 8,50% → **R$ 8.500,00** | 3,40% → **R$ 3.400,00** |
| 2033 | 13,50% → **R$ 13.500,00** | 5,40% → **R$ 5.400,00** |

(Mesma observação da pasta 01: a redução de 60% incide só sobre CBS/IBS; ICMS/ISS residual da
transição segue seu próprio cronograma de extinção, sem desconto adicional por o serviço estar no
Anexo III.)

## 5. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, Câmara dos Deputados) — leitura
  literal do art. 130, confirmando o caput e o parágrafo único citados na Seção 1.
- MCP `mcp-rag-reforma` (`buscar_reforma`, tier `chunk`) — arquivos `Material Base\Lcp
  214_ATUALIZADA.pdf`, `Mentoria_Consultoria_Reforma Tributária\00_Modelos\REGULAMENTO DA
  CBS.pdf`, `REGUMANTO DO IBS E OUTRAS PROVIDÊNCIAS - MAR 26 - 09 (1).docx` e, apenas como
  indicativo de conteúdo do Anexo III (não como fonte de numeração final), `PLP 68-2024 [EM
  DISCUSSÃO].pdf`.
- MCP `mcp-compliance` (`fonte_lc214_mapa_temas`) — mapa estático já existente não desce a este
  nível de artigo (mesma observação da pasta 01).
- `aliquotas-transicao/cronograma-aliquotas.json` — valores reais do cronograma CBS/IBS.
- Google Drive: varredura por nome de arquivo (`saude`) nas duas pastas-raiz não encontrou
  material específico dedicado a serviços de saúde/planos de saúde na Reforma (o único arquivo
  com "saúde" no nome encontrado foi sobre medicamentos, tratado na pasta 04).
- Projeto BUFON & FRASSON RTC: nenhum classificador específico de serviços de saúde encontrado
  no grep do código-fonte.
- MindMeister: nenhum mapa relevante (mesma observação da pasta 01).

## 6. Lacunas conhecidas

1. **Anexo III completo** não foi extraído integralmente; a lista de itens vista tem origem no
   PLP 68/2024 (minuta pré-sanção), não no texto final da LC 214/2025 — os NÚMEROS de item podem
   ter mudado, embora o TIPO de serviço (cirúrgico, UTI, urgência, clínica médica etc.) seja
   presumivelmente estável entre a minuta e o texto final.
2. **Nenhuma jurisprudência** pesquisada nesta rodada (lei recente, regime começa em 2027).
3. **Nenhum exemplo real de mercado** (ex.: um cliente do escritório que seja plano de saúde ou
   hospital) foi localizado nas pastas do Drive varridas.
4. **Regra de glosas médicas**: não há, na base canônica já existente (`cadeia-negocios-creditos/`
   ou `formulas-glossario/`), nenhuma fórmula ou campo que já opere essa exclusão de base de
   cálculo — se a plataforma Guerra RTC vier a implementar essa regra, ela precisará ser
   construída do zero; não é uma regra herdada do sistema de ICMS/ISS anterior.
