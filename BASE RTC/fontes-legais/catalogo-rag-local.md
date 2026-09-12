# Catálogo do RAG local — pasta "Reforma Tributária - Estudos"

Índice (não transcrição de conteúdo) dos materiais próprios de Marcos Lima usados como
fonte primária de doutrina, normas e dados de apoio. Local:
`G:\Meu Drive\Outros Arquivos\Reforma Tributária - Estudos\`

Estes são PDFs/planilhas/apresentações reais — este catálogo aponta para eles, não copia
o conteúdo (arquivos binários grandes, fora do escopo de uma base estática em texto). Ao
montar o MCP de mentorias, ler o arquivo apontado sob demanda (fetch/leitura pontual),
não pré-carregar tudo.

## `00_NORMAS E DADOS CANONICOS/` — a pasta mais relevante para fundamentação legal

| Subpasta | Conteúdo | Destaques |
|---|---|---|
| `01_EC 132 e LC 214/` | Texto integral da EC 132/2023 e LC 214/2025, sumário navegável da LC 214, anexos de produtos | `Reforma Tributária - SUMÁRIO LC 214.xlsx` é um índice já pronto por artigo/tema — cruzar com `mapa-lc214-artigos.json` desta base |
| `02_LC 224 e Beneficios Fiscais/` | LC 224/2025, INs RFB 2305/2026 e 2306/2026, TIPI, parecer-modelo sobre redução de benefícios PIS/COFINS | Inclui `PARECER MODELO.pdf` e planilha `PRODUTOS LC 214.xlsx` — referência prática já validada pelo escritório |
| `03_Notas Tecnicas NFe-NFCe-NFSe/` | Notas técnicas oficiais NF-e/NFC-e/NFS-e (RTC) + histórico de versões (out-dez/2025) | Espelha o `catalogo-fontes-oficiais.json` desta base, com os PDFs reais anexados |
| `04_Decretos e Resolucoes CGIBS/` | Decreto 12.955/2026 (Split Payment), Resolução CGSB nº 6/2026 (Regulamento do IBS), minuta de regulamento | Nível 5 da hierarquia de fontes (`hierarquia-fontes-legais.json`) |
| `05_PLP 68 e PLP 1087/` | Textos em discussão (PLP 68/2024, PLP 1087/2025) e atas de reunião (bares e restaurantes) | Histórico legislativo — útil para entender a evolução do texto até a LC 214 final |
| `06_Tributacao de Altas Rendas e IRPJ-CSLL/` | IN RFB 2299/2025 (altas rendas), Lei 15.270, memória de cálculo própria de Marcos Lima | Fora do escopo IBS/CBS, mas correlato (Reforma da Renda) |
| `07_Contabilidade e CPCs/` | CPC 21, CPC 26, CPC 05, ICPC 08, Lei 6.404/1976, artigo revisado por pares sobre registro contábil | Fundamenta a lacuna de contabilização (CPC 51/NBC TG 51) citada em `mapa-lc214-artigos.json` |
| `08_Piloto Operacional RFB/` | Materiais das Lives do Piloto da Reforma (calculadora, split payment, cashback, ambiente de produção restrita) | Fonte primária operacional — nível 6 da hierarquia (manifestações oficiais) |
| `09_Legislacao Correlata/` | Legislação correlata (ex.: L10931) | Apoio pontual |

## Outras pastas do RAG (fora do escopo desta extração — não são fonte legal)

- `01_ARTIGOS E PESQUISA ACADEMICA/` — doutrina (nível 8 da hierarquia), artigos peer-reviewed
- `02_PALESTRAS E APRESENTACOES/` — material didático próprio (slides de palestras/cursos)
- `03_MATERIAIS DE APOIO PARA PALESTRAS E DADOS/` — dados de apoio para aulas
- `04_CURSOS E MENTORIAS/` — materiais de curso/mentoria (inclui "00_MATERIAIS SECRETOS REFORMA")
- `05_CONSULTORIA POR CLIENTE/` — dossiês específicos de cliente (não genéricos, fora do escopo desta base canônica)
- `06_BASE DE DADOS DE TESTE/` — dados de teste

## Como usar isto no MCP de mentorias

1. Para fundamentar um artigo específico: primeiro `mapa-lc214-artigos.json` (tema→artigo→URL oficial).
2. Se precisar do texto consolidado com anotações do próprio Marcos: abrir o PDF/DOCX correspondente
   em `01_EC 132 e LC 214/` ou `02_LC 224 e Beneficios Fiscais/`.
3. Para Notas Técnicas de NF-e: `catalogo-fontes-oficiais.json` (`notas_tecnicas_nfe`) tem o resumo;
   o PDF completo está em `03_Notas Tecnicas NFe-NFCe-NFSe/`.
4. Para doutrina/artigos acadêmicos (nível 8, usar só se não houver norma/jurisprudência): pasta
   `01_ARTIGOS E PESQUISA ACADEMICA/` do RAG — não replicada aqui.
