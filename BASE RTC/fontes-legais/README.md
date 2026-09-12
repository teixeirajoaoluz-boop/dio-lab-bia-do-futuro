# Fontes Legais

Duas camadas nesta pasta, de origens diferentes:

1. **Módulo `fontes_legais.py` do MCP planejamento-RTC** — validação de números de alíquota
   e classificação de produto contra planilhas do curso (ver seção abaixo). Não mapeia
   artigos de lei.
2. **Mapeamento legal artigo-a-artigo (adicionado depois, via RAG da Reforma Tributária)** —
   fecha exatamente essa lacuna. Ver `mapa-lc214-artigos.json`, `hierarquia-fontes-legais.json`,
   `glossario-reforma.json`, `cronograma-transicao-oficial.json`, `catalogo-fontes-oficiais.json`
   e `catalogo-rag-local.md`. Fonte: MCP `mcp-compliance` (tools `fonte_lc214_mapa_temas`,
   `alegacao_hierarquia_fontes`, `alegacao_glossario`, `alegacao_cronograma_transicao`,
   `fonte_catalogo`, `fonte_nt_catalogo`, `fonte_rfb_cetad`) + índice do RAG local de Marcos Lima
   (`G:\Meu Drive\Outros Arquivos\Reforma Tributária - Estudos\00_NORMAS E DADOS CANONICOS\`).

## Camada 1 — `fontes_legais.py` (mcp-planejamento-RTC)

Fonte analisada: `mcp_planejamento_rtc/fontes_legais.py` (145 linhas).

## O que este módulo NÃO é

Apesar do nome "fontes legais", o módulo **não mapeia artigos da LC 214/2025,
da EC 132/2023 ou de normas correlatas**. Não há nenhuma referência a número
de artigo, inciso ou parágrafo no arquivo-fonte. Isso é uma lacuna em relação
ao que se esperaria de um módulo com esse nome — registrar aqui para não
inventar mapeamento tema→artigo que não existe no código.

## O que ele realmente faz

É um leitor de duas planilhas Excel oficiais do curso de Reforma Tributária,
usadas como fonte primária de conferência (a "Revisão Chata" confronta os
números do modelo contra essas planilhas; se a fonte primária diverge do
modelo, é bloqueio de entrega):

1. **Planilha de alíquotas de transição**
   `MÓDULO 06 - AULAS 29 A 35 - ALIQUOTAS.xlsx`, aba
   "ANÁLISE DAS ALÍQUOTAS DE TRANSI[ÇÃO]".
   Função `extrair_transicao_oficial()` lê células por coordenada fixa e
   devolve:
   - alíquotas gerais (CBS, IBS, ICMS, ISS "cheios");
   - por ano (2027 a 2033): CBS, IBS e um fator de redução do ICMS
     (`icms_fator` = ICMS do ano ÷ ICMS geral).
   Regras especiais hardcoded: 2027 e 2028 não aparecem no bloco do ICMS na
   planilha, então o fator é forçado para `1.0` (ICMS integral); o CBS de
   2028 é copiado do CBS de 2027 (mesmo bloco "2027 - 2028" na planilha).

2. **Planilha de produtos/NCM da LC 214**
   `MÓDULO 06 - AULAS 01 A 18 - PRODUTOS LCP 214.xlsx`, aba "Consolidado".
   Função `consultar_produto(termo)` busca por NBS/NCM ou por trecho da
   descrição e devolve os registros que batem: anexo, item, descrição,
   código NBS/NCM/SH, tipo de tratamento e percentual (redução/alíquota).

## Onde os arquivos vivem

Ambos os xlsx ficam em:
`G:\Meu Drive\Projetos de Execução\MCP\mcp-planejamento-RTC\Legislações\Reforma_Tributaria\Materiais_Curso\`

Este repositório de conhecimento **não contém as planilhas**, apenas a regra
de extração. Qualquer consumidor futuro (o MCP de mentorias) vai precisar do
acesso a esses dois arquivos para reproduzir os números — eles não estão
embutidos em código nem duplicados aqui.

## O que `fontes_legais.py` não resolve (e onde isso foi resolvido)

Se o objetivo final é fundamentar respostas de mentoria em artigos de lei
(LC 214/2025, EC 132/2023, Notas Técnicas do Comitê Gestor do IBS etc.), o
módulo `fontes_legais.py` não serve como fonte — ele serve apenas para validar
números de alíquota e classificação de produto contra as planilhas do curso.
`mapa-normas.json` reflete isso: mapeia temas às **planilhas-fonte**, não a
artigos de lei.

**Essa lacuna foi fechada na Camada 2** (arquivos descritos no topo deste
README): `mapa-lc214-artigos.json` cobre 17 temas com artigos precisos da
LC 214/2025 (fato gerador, alíquotas, não cumulatividade, Split Payment,
Simples Nacional, transição 2026-2033, etc.), com URL direta para o texto
oficial no Planalto. Use as duas camadas em conjunto: Camada 1 para os
números já calculados (alíquotas de curso, produtos/NCM), Camada 2 para citar
a lei que os fundamenta.

## Camada 2 — Mapeamento legal artigo-a-artigo

| Arquivo | Conteúdo |
|---|---|
| `mapa-lc214-artigos.json` | 17 temas da LC 214/2025 com artigos exatos e URL oficial (Planalto) |
| `hierarquia-fontes-legais.json` | Ordem de precedência de 8 níveis (CF → LC → lei ordinária → NT → resolução → manifestação oficial → jurisprudência → doutrina), regra de lacuna normativa e o que é proibido afirmar |
| `glossario-reforma.json` | 18 termos técnicos (IBS, CBS, IS, Split Payment, RTC, PGDAS-D, Fator R etc.) com base legal |
| `cronograma-transicao-oficial.json` | Cronograma 2026-2033 com base legal por fase, cruzando com o cronograma de cálculo já existente em `aliquotas-transicao/` |
| `catalogo-fontes-oficiais.json` | LC 214/227/224, EC 132, LC 123, portais técnicos, atos regulamentadores e Notas Técnicas de NF-e/NFC-e/NFS-e |
| `catalogo-rag-local.md` | Índice (não transcrição) dos materiais próprios de Marcos Lima na pasta `Reforma Tributária - Estudos` — onde buscar o PDF/DOCX original de cada norma |

**Regra de uso:** toda afirmação jurídica nesta base canônica deve citar artigo,
lei e, se aplicável, o nível da hierarquia (`hierarquia-fontes-legais.json`).
Se a legislação não tratar expressamente um ponto, declarar isso — nunca
inferir posição da RFB sem ato normativo (ver `proibido` em
`hierarquia-fontes-legais.json`).
