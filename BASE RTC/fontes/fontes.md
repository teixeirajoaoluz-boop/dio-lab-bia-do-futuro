# Fontes da Base Canônica

Proveniência das regras. Toda regra da base precisa de fonte rastreável aqui.

## 1. Doutrina de cruzamento de informações fiscais

Base conceitual dos indicadores e da matriz de cruzamentos, extraída de aulas sobre auditoria digital e cruzamento de informações fiscais:

- [Cruzamentos de informações fiscais — aula completa](https://www.youtube.com/watch?v=cFM3IAjy9tw)
- [Cruzamentos de informações por indicadores](https://www.youtube.com/watch?v=IXrhx0GXNaM)
- [Contrainteligência fiscal e auditoria digital](https://www.youtube.com/watch?v=tZdGtf7Cwes)

### Princípios extraídos

| Princípio | Aplicação na plataforma |
|-----------|-------------------------|
| As informações nascem nos documentos fiscais eletrônicos, transitam pelas escriturações fiscais e deságuam na contabilidade | Define o `fluxoCanonico` e o sentido de cada cruzamento |
| O cruzamento pode ser feito por **indicadores** ou por **obrigações** | A plataforma implementa por indicador, com a obrigação como ponta |
| Receita bruta, tributos a recolher e escrituração de documentos são os indicadores que não podem ser omitidos em nenhuma competência | `prioridade: obrigatorio_mensal` |
| Ausência de escrituração de documento é a causa-raiz das divergências nos outros indicadores | Justifica o cruzamento XML × SPED como prioritário |
| Validação de PVA/PGE é apenas de layout, não de conteúdo | Justifica a validação qualitativa do painel |
| Documento com XML e sem escrituração — e o inverso — são ambos indício de problema | Cruzamento bidirecional em `verificar` |
| Auditoria digital serve para validar, mitigar risco, identificar créditos e subsidiar planejamento | Objetivo do painel de Conferência de Dados |

### Registros citados como ponto de coleta

| Informação | Registro |
|-----------|----------|
| Receita de mercadorias | C100 / C190 — SPED Fiscal |
| Receita de serviços | A100 — EFD Contribuições |
| DRE contábil | J150 — ECD |
| Balanço patrimonial | J100 — ECD |
| DRE fiscal | L300 — ECF |
| ICMS-ST a recolher | E250 — SPED Fiscal |
| PIS a recolher | M200 / M210 — EFD Contribuições |
| COFINS a recolher | M600 / M610 — EFD Contribuições |
| IRPJ a pagar | N630 — ECF |
| CSLL a pagar | N670 — ECF |
| Estoque | Bloco H — SPED Fiscal |
| CIAP / imobilizado | Bloco G — SPED Fiscal |

## 2. Exigibilidade por regime tributário

| Regra | Fundamento |
|-------|-----------|
| Optante do Simples pode adotar contabilidade simplificada | LC 123/2006, art. 27 |
| Declaração mensal única do Simples (PGDAS-D) | LC 123/2006, art. 25 |
| DEFIS anual | Resolução CGSN 140/2018 |
| Obrigados à ECD | IN RFB 2003/2021 |
| Obrigados à ECF e dispensa do optante do Simples | IN RFB 2004/2021 |
| Dispensa de EFD Contribuições ao optante do Simples | IN RFB 1252/2012, art. 5º |
| EFD ICMS/IPI e tratamento do optante conforme UF | Ajuste SINIEF 2/2009 |
| Crédito de ICMS do imobilizado em 1/48 | LC 87/1996 (Lei Kandir) |
| Faixas, anexos e Fator R do Simples | LC 123/2006, Anexos I a V |

## 3. Reforma Tributária (IBS/CBS)

| Regra | Fundamento |
|-------|-----------|
| Regras gerais de IBS e CBS, creditamento e transição | LC 214/2025 |
| Alíquotas de transição 2027–2033 aplicadas nas projeções | Estudo interno `ALIQUOTAS.xlsx` |

## 4. Base do Simples Nacional (`simples-nacional/`)

### Tabelas e enquadramento

| Regra | Fundamento | Confiança |
|-------|-----------|-----------|
| Faixas de RBT12, alíquota nominal, parcela a deduzir e repartição dos Anexos I a V | LC 123/2006, Anexos I a V (redação da LC 155/2016) | Alta — texto legal |
| Fórmula da alíquota efetiva `((RBT12 × nominal) − dedução) ÷ RBT12` | LC 123/2006, art. 18, § 1º-A | Alta |
| Teto de receita bruta de R$ 4.800.000 | LC 123/2006, art. 3º, II | Alta |
| Sublimite de R$ 3.600.000 para ICMS e ISS | LC 123/2006, art. 13-A e art. 19 | Alta |
| Limite do MEI de R$ 81.000, com DAS fixo | LC 123/2006, art. 18-A, § 1º | Alta |
| Fator R = FS12 ÷ RBT12, corte de 28%, migração do Anexo V para o III | LC 123/2006, art. 18, § 5º-M; Resolução CGSN 140/2018, art. 26 | Alta |
| Composição do FS12: salários, CPP, FGTS, pró-labore e 13º; exclui aluguéis, lucros, estagiários e MEI | Resolução CGSN 140/2018, art. 26; simulador `sn-transicao` | Alta |
| Teto de 5% para a parcela de ISS no DAS, com redistribuição do excedente | LC 123/2006, art. 18, §§ 1º-A e 1º-B | Alta |
| CPP fora do DAS no Anexo IV | LC 123/2006, art. 18, § 5º-C | Alta |

### Cenários da Reforma para o optante

| Regra | Fundamento | Confiança |
|-------|-----------|-----------|
| Recolhimento de IBS e CBS dentro do DAS, com crédito ao adquirente limitado ao valor recolhido | LC 214/2025, arts. 41 e 47 | Média — depende de regulamentação |
| Opção por apurar IBS e CBS pelo regime regular, fora do DAS, com crédito integral nas duas pontas | LC 214/2025, art. 41, § 3º e art. 47, § 3º | Média |
| Redução de 30% para profissões intelectuais fiscalizadas por conselho | LC 214/2025, art. 127 | Média |
| Crédito presumido sobre estoque na entrada do novo regime | LC 214/2025, art. 381 | Média |
| Fase de teste em 2026 com CBS 0,9% e IBS 0,1% | LC 214/2025, arts. 343 a 348 | Alta |
| Cronograma 2027–2032 e alíquota de referência de 26,5% no regime pleno | Projeção — a alíquota será fixada por lei ordinária | Premissa editável na tela |

### Referência operacional

Comportamento de tela e lógica de comparação seguem o **Simulador Guerra RTC** (Prof. Fellipe Guerra), documentado em `C:\Projetos Tecnologicos\06_SimuladorGuerraRTC\00_DOCBASE`:

- `README.md` — arquitetura, catálogo de simuladores e alíquotas por competência.
- `RELEASE-2026-05-23.md` — Fator R com FS12 e regra de oscilação entre os Anexos V e III.
- `AUDITORIA-NORMATIVA-2026-05-22.md` — correções normativas de artigos da LC 214/2025.

O código dos simuladores é publicado como HTML estático e não está versionado nessa pasta; as tabelas foram reconstruídas a partir do texto legal e conferidas contra o caso de referência do simulador (Anexo III, 4ª faixa, RBT12 de R$ 1.800.000 → alíquota efetiva de 14,02%).

## 5. Convenções internas

| Regra | Origem |
|-------|--------|
| Tolerância de 15% em receita fiscal × ECD | Convenção do projeto Guerra RTC |
| Tolerância de 20% em aquisições × custos ECD | Convenção do projeto Guerra RTC |
| Tolerância de 5% em receita fiscal × PGDAS-D | Convenção do projeto Guerra RTC |
| Tolerância de 2% em XML × SPED | Convenção do projeto Guerra RTC |
| Premissa padrão de crescimento de 5% a.a. quando o histórico é insuficiente | Convenção do projeto Guerra RTC |

Tolerâncias são convenções internas, não normas — ajustáveis, mas sempre nesta base, nunca no código.
