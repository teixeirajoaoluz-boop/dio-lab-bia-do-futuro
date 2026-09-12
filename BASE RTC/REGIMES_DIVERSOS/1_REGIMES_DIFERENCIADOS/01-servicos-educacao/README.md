# Serviços de Educação — Redução de 60%

## 1. Fundamento legal

**LC 214/2025, art. 129** (Capítulo "Da Redução em 60% das Alíquotas do IBS e da CBS", Seção II —
Dos Serviços de Educação):

> "Art. 129. Ficam reduzidas em 60% (sessenta por cento) as alíquotas do IBS e da CBS incidentes
> sobre o fornecimento dos serviços de educação relacionados no Anexo II desta Lei Complementar,
> com a especificação das respectivas classificações da Nomenclatura Brasileira de Serviços,
> Intangíveis e Outras Operações que Produzam Variações no Patrimônio (NBS)."
>
> Parágrafo único. A redução de alíquotas prevista no caput deste artigo:
> I - somente se aplica sobre os valores devidos pela contraprestação dos serviços listados no
> Anexo II da Lei Complementar nº 214, de 2025; e
> II - não se aplica a outras operações eventualmente ocorridas no âmbito das escolas, das
> instituições ou dos estabelecimentos do fornecedor de serviços.

**Confirmado por leitura literal do texto oficial consolidado** — LC 214/2025, art. 129, texto
oficial consolidado (norma atualizada, já incorpora as alterações da LC 227/2025), Centro de
Documentação e Informação da Câmara dos Deputados:
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf

Esta é a fonte de maior autoridade disponível para este README — substitui a confirmação da rodada
anterior, que se apoiava no RAG local (arquivo `Material Base\Lcp 214_ATUALIZADA.pdf`).

O **Anexo II** da LC 214/2025 lista os serviços de educação por código NBS — ex.: "Ensino
Infantil, inclusive creche e pré-escola" (NBS 1.2201.1), "Ensino Fundamental" (1.2201.20.00),
"Ensino Médio" (1.2201.30.00), "Ensino Técnico de Nível Médio" (1.2202.00.00), "Ensino Superior,
compreendidos os cursos e programas de graduação, pós-graduação, de extensão e cursos
sequenciais" (1.2204), entre outros (fonte: `Material Base\Reforma Tributária - LCP 214-2025.pdf`).

**Nota de escopo**: existe ainda um benefício adicional específico — **art. 308 da LC 214/2025**
("Fica reduzida a zero a alíquota da CBS incidente sobre o fornecimento de serviços de educação
de ensino superior por instituição privada de ensino... durante o período de adesão e vinculação
ao Programa Universidade para Todos - Prouni") — que é um **Regime Específico** (alíquota zero
apenas da CBS, só para adesão ao PROUNI, com regra de proporcionalidade própria), não um Regime
Diferenciado geral. Fica fora do escopo desta pasta (é tratado, se aplicável, pelo bloco de
Regimes Específicos) — citado aqui apenas para não confundir o operador que encontrar "educação"
com alíquota zero em vez de 60%.

## 2. Regra

- **Percentual de redução**: 60% sobre as alíquotas do IBS e da CBS (não é alíquota zero).
- **Aplica-se a**: exclusivamente aos **serviços** listados no Anexo II (não a produtos/bens
  vendidos por instituições de ensino, nem a outras receitas da escola fora do Anexo II — ex.:
  venda de uniformes, material didático avulso, cantina).
- **Não se aplica** a "outras operações eventualmente ocorridas no âmbito das escolas" — a lei é
  explícita em vedar a extensão do benefício por analogia a atividades correlatas do mesmo
  estabelecimento.

## 3. Como funciona na prática

Segue a sistemática geral do IBS/CBS: apuração mensal, débito menos crédito (não cumulatividade
plena), Split Payment na liquidação financeira. A única mudança é que a **alíquota nominal usada
no cálculo do débito** já sai reduzida em 60% para as operações do Anexo II — não há fórmula de
cálculo própria, crédito presumido, ou regime de caixa diferenciado.

## 4. Exemplo de cálculo numérico

Operação hipotética: mensalidade de curso listado no Anexo II, valor de **R$ 100.000,00**
(agregado mensal de uma instituição de ensino), usando o cronograma real de transição (referencial
de exemplo do próprio README de origem: CBS 8,50% / IBS 5,00%; fonte:
`aliquotas-transicao/cronograma-aliquotas.json`).

| Ano | CBS+IBS regime GERAL (sem redução) | CBS+IBS com redução de 60% (serviço de educação) |
|---|---|---|
| 2027 | CBS 8,40% + IBS 0,10% = 8,50% → **R$ 8.500,00** | CBS 3,36% + IBS 0,04% = 3,40% → **R$ 3.400,00** |
| 2033 | CBS 8,50% + IBS 5,00% = 13,50% → **R$ 13.500,00** | CBS 3,40% + IBS 2,00% = 5,40% → **R$ 5.400,00** |

Observação metodológica: a redução de 60% incide **apenas sobre CBS e IBS** (é o que a lei diz
literalmente — "alíquotas do IBS e da CBS"). O ICMS/ISS residual da transição (arts. 337-370, já
mapeados na base) segue seu próprio cronograma de extinção **sem qualquer desconto adicional** por
o serviço estar listado no Anexo II — a redução de 60% não é uma dedução sobre a carga tributária
total da empresa, é uma alíquota nominal menor apenas na parcela IBS/CBS.

## 5. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, Câmara dos Deputados) — leitura
  literal do art. 129, confirmando o caput e o parágrafo único citados na Seção 1.
- MCP `mcp-rag-reforma` (`buscar_reforma`, tier `chunk`, múltiplas queries) — arquivo
  `Material Base\Lcp 214_ATUALIZADA.pdf` e `Mentoria_Consultoria_Reforma
  Tributária\00_Modelos\REGULAMENTO DA CBS.pdf` — usados na rodada anterior, agora corroborados
  pela fonte oficial.
- MCP `mcp-compliance` (`fonte_lc214_mapa_temas`, `fonte_artigo_url`) — mapa de 17 temas
  já existente na base (`fontes-legais/mapa-lc214-artigos.json`); **nota**: o mapa estático já
  existente não desce ao nível de artigo específico de cada setor do art. 128 — apenas cita
  genericamente "Imunidades e Isenções (arts. 49-56)" e "Alíquotas (arts. 16-23)".
- `aliquotas-transicao/README.md` e `cronograma-aliquotas.json` (base canônica já existente) —
  valores reais do cronograma de transição CBS/IBS 2027-2033.
- Google Drive (`G:\Meu Drive\Outros Arquivos\Reforma Tributária - Estudos`,
  `G:\Meu Drive\Projetos de Execução\Consultorias\Guerra`): varredura por nome de arquivo não
  encontrou material específico sobre "serviços de educação" (nenhum arquivo com esse termo no
  nome nas duas pastas-raiz varridas).
- Projeto BUFON & FRASSON RTC: grep por "educa" no código-fonte não retornou nenhum classificador
  ou regra específica de serviços de educação reaproveitável.
- MindMeister (`mm_maps_list`): nenhum mapa mental sobre Reforma Tributária ou educação
  encontrado (os mapas existentes são de 2020, sobre PIS/COFINS e Lucro Real/Presumido/Simples,
  não relacionados à LC 214/2025).

## 6. Lacunas conhecidas

1. **Anexo II completo (lista de todos os códigos NBS de educação)** não foi extraído
   integralmente — apenas uma amostra de ~8 itens foi vista nos chunks retornados pelo RAG.
2. **Nenhuma jurisprudência** (CARF, STJ, STF) sobre a aplicação do art. 129 foi pesquisada nesta
   rodada — a lei é recente (2025) e o regime de transição só começa em 2027, então não há
   jurisprudência consolidada esperável ainda; não foi feita busca nos MCPs `guerra-stj`,
   `guerra-stf`, `mcp-compliance:pesquisar_carf` para esta pasta específica.
3. **Nenhum exemplo real de mercado** (caso concreto de uma instituição de ensino cliente do
   escritório) foi encontrado nas pastas do Drive varridas — o exemplo numérico acima é
   hipotético, usando os valores reais do cronograma de transição, não um caso real de cliente.
