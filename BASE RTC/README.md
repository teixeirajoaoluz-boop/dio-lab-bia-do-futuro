# Base Canônica Global — Mentorias Reforma Tributária (RTC)

Fonte única de verdade, **100% estática** (Markdown + JSON, sem código de front/back), reunindo
todas as regras matemáticas e regras de negócio da Reforma Tributária (IBS/CBS) que hoje vivem
espalhadas entre a plataforma Guerra RTC e o MCP `mcp-planejamento-RTC`.

**Propósito:** ser a matéria-prima para um futuro MCP de mentorias — qualquer mentoria em
andamento (Dorna, Cataratas, Armize, Aluma) ou nova consultoria no padrão RT360 (ex.: Grupo
Stoque Mercantil) consulta esta base para montar a análise da Reforma Tributária, sem depender
do código da plataforma nem de acesso ao banco de dados.

## Como esta base foi montada

Extraída de duas fontes de código-fonte vivas:

| Origem | O que forneceu |
|---|---|
| `02_Guerra RTC/00_Dados Canonicos/` | Regras de cruzamento fiscal/contábil, CFOP, Simples Nacional (Anexos I-V), indicadores, obrigações — **copiado integralmente**, é a base canônica já madura do projeto |
| `02_Guerra RTC/backend/base_sql/*.sql` e `*.py` | Alíquotas de transição, redução de 30%, regras de crédito por regime do fornecedor, glossário de fórmulas |
| `MCPs/05_Consultor_Tributario/mcp-planejamento-RTC/mcp_planejamento_rtc/*.py` | Motor de cálculo (engine), classificação farma, premissas, fontes legais, checklist e estrutura de dossiê |

Cada pasta abaixo tem seu próprio `README.md` citando o arquivo-fonte de cada regra. Nada foi
inventado: onde a fonte não tinha o dado (ex.: uma tabela só populada em produção, um CSV externo
não lido), isso está **registrado explicitamente como lacuna** dentro do arquivo correspondente —
ver seção "Lacunas conhecidas" abaixo.

## Estrutura

### Herdado de 00_Dados Canonicos (cruzamento fiscal/contábil)

| Pasta | Conteúdo |
|-------|----------|
| `regras-fiscais-cruzamento-informacoes.md` | Regra do pipeline de cruzamento (documento raiz original) |
| `cfop/` | Famílias, espelhos e grupos especiais de CFOP |
| `fontes/` | Proveniência normativa das regras de cruzamento |
| `indicadores/` | Indicadores e cruzamentos com tolerância |
| `obrigacoes/` | Obrigações acessórias e registros de origem |
| `regimes/` | Exigibilidade por regime tributário e regras de veredito |
| `simples-nacional/` | Anexos I-V da LC 123/2006, Fator R, sublimite, transição IBS/CBS no DAS |

### Novo — Reforma Tributária / RT360 (extraído do código nesta rodada)

| Pasta | Conteúdo | Origem |
|-------|----------|--------|
| `aliquotas-transicao/` | Cronograma CBS/IBS/ICMS/ISS 2027-2033, alíquotas SN por anexo, redução de 30% (Art. 127 LC 214/2025) | `backend/base_sql/24_*`, `20_*`, `21_*` |
| `classificacao-produtos/` | Cadeia NCM→CST→cClassTrib, motor de classificação farmacêutica (4 baldes tributários, Anexo XIV, 382 princípios ativos) | `backend/base_sql/07_*`, `13_*`, `farma.py` |
| `cadeia-negocios-creditos/` | Regras de crédito de IBS/CBS por regime do fornecedor, fórmulas do motor de apuração (débito/crédito/saldo) | `backend/base_sql/34a_*`, `engine.py` |
| `premissas-projecoes/` | Schema de premissas exigidas para projeção 2027-2033, checklist do que é obrigatório preencher | `premissas.py`, `backend/base_sql/26_*`, `25_*` |
| `formulas-glossario/` | Glossário de 199 fórmulas/campos calculados da plataforma | `00_banco_AWS/GLOSSARIO FORMULAS.csv` |
| `fontes-legais/` | Mapeamento tema→planilha do curso (`fontes_legais.py`) **+** mapeamento tema→artigo da LC 214/2025, hierarquia de 8 níveis, glossário, cronograma oficial e catálogo de normas (via MCP `mcp-compliance` + RAG local) | `fontes_legais.py` + `mcp-compliance` + `Reforma Tributária - Estudos/00_NORMAS E DADOS CANONICOS` |
| `checklist-dossie/` | Checklist de entrega e estrutura do dossiê técnico por perfil de cliente | `checklist.py`, `dossie.py` |

## Lacunas conhecidas (não inventadas, apenas registradas)

Estas lacunas foram identificadas durante a extração e estão detalhadas nos README de cada pasta.
Ao construir o MCP de mentorias sobre esta base, trate-as como pendências de origem de dado, não
como bug desta base:

1. **Redução de 30%** só tem dado populado para serviços de profissão regulamentada (18 categorias,
   Art. 127 LC 214/2025) — não há regra equivalente para produtos/mercadorias no repositório.
2. **Alíquotas SN por anexo** só cobrem Anexos 1-5; o Anexo 6, citado em comentário SQL, não tem
   dado populado.
3. **cClassTrib definitivo** de 3 dos 4 baldes tributários do módulo farma está marcado como
   placeholder no próprio código-fonte ("confirmar na tabela oficial").
4. **CSV `CAD_NCM_CST_CCLASSTRIB.csv`** (fonte de todo mapeamento NCM fora do farma, ~3.487
   registros) não foi lido nesta extração — é dado externo, precisa ser buscado à parte.
5. **`engine.py`** depende de uma "memória 08" (`premissas.serie_anual`) cuja estrutura não está
   documentada em nenhum SQL lido — dependência externa registrada, não inventada.
6. ~~**Fontes legais**: o módulo `fontes_legais.py` não mapeia artigos específicos de LC 214/2025 ou
   EC 132/2023 — mapeia apenas dois temas a planilhas de apoio (alíquotas por ano e NCM).~~
   **Resolvida.** `fontes-legais/` agora tem uma segunda camada com o mapeamento artigo-a-artigo
   da LC 214/2025 (17 temas), hierarquia de 8 níveis de fontes, glossário de 18 termos, cronograma
   oficial com base legal e catálogo de normas/Notas Técnicas — extraído do MCP `mcp-compliance`
   e indexado ao RAG local de Marcos Lima (`Reforma Tributária - Estudos`). Continua faltando:
   texto integral de cada artigo (só há URL de fetch) e o conteúdo doutrinário/acadêmico da
   pasta `01_ARTIGOS E PESQUISA ACADEMICA` do RAG, que não foi indexado nesta rodada.
7. **Checklist/dossiê**: os artefatos do perfil "exportadora" (parecer, apresentação, DRE, notas
   fiscais modelo) são gerados por scripts externos no Google Drive, não lidos nesta extração —
   só os rótulos/estrutura são conhecidos aqui.
8. **Glossário de fórmulas**: o CSV real só popula 4 das 8 colunas do schema SQL
   (`tabela`, `coluna`, `sigla`, `expressao_texto`) — `descricao`, `entradas`, `autor`, `versao`
   ficam `null` por não existirem na planilha de origem.
9. **Schema de premissas** é uma reconstrução a partir do código e de um exemplo real de cliente
   (Novo Frio) — o schema JSON oficial, se existir, vive no Google Drive e não foi lido.

## Como manter esta base atualizada

Esta é uma base **estática por decisão** (não há script de regeneração automática). Quando uma
regra mudar na plataforma Guerra RTC ou no MCP `mcp-planejamento-RTC`:

1. Edite o arquivo correspondente aqui (README/JSON) e cite a nova fonte.
2. Não copie código — traduza a regra para prosa/JSON, como foi feito nesta extração.
3. Se a lacuna listada acima for resolvida (ex.: o CSV de NCM for lido), atualize a seção
   "Lacunas conhecidas".
