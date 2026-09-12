# Cruzamento de Informações Fiscais — Base Canônica para Auditoria da Plataforma RT360

Fontes: mapas mentais "Auditorias Digitais — Cruzamentos das Informações Fiscais" (Prof. Marcos Lima) e "Auditoria Digital e Cruzamentos Fiscais" (Prof. Fellipe Guerra); material técnico da disciplina IPOG "Auditoria Digital e Cruzamento das Informações" e da disciplina "Simples Nacional" (G:\Meu Drive\Outros Arquivos\IPOG\Disciplinas); e críticas reais registradas na Mentoria Dorna (WhatsApp "IA RTC - Prof Marcos Lima", jun-ago/2026) sobre a plataforma RT360.

## 1. Fluxo de geração da informação (por que os cruzamentos existem)

Documento fiscal eletrônico → escrituração fiscal (EFD/SPED) → contabilidade (ECD/ECF) → obrigações acessórias derivadas (DCTF, REINF, DIRF, eSocial, PERDCOMP, DIRPF).
Toda inconsistência que a plataforma aponta como "incompatível" deve ser rastreável a uma quebra em algum elo desta cadeia — é isso que os cruzamentos abaixo testam.

## 2. Cruzamentos canônicos por obrigação (par a par)

| Cruzamento | O que testa |
|---|---|
| EFD ICMS/IPI × Documentos Fiscais (NF-e/XML) | Documento não localizado na EFD; XML não localizado; divergência de valores |
| EFD ICMS/IPI × DCTF | Divergência de valores de IPI |
| EFD ICMS/IPI × EFD Contribuições | Blocos C e D — mercadorias x serviços |
| DCTF × EFD Contribuições | PIS, COFINS e CPRB |
| EFD Contribuições × Documentos Fiscais | Documento/XML não localizado; divergência de valores |
| ECD × ECF | Demonstrações contábeis |
| ECD × EFD ICMS/IPI | Receita × Estoques |
| ECD × EFD Contribuições | Receita × Bases de créditos |
| ECF × DIRF | Rendimentos |
| ECF × PERDCOMP | Valores de créditos tributários |
| ECF × DCTF | Valores dos tributos |
| ECF × EFD Contribuições | Receita e bases de créditos |
| ECF × EFD ICMS/IPI | Receitas e estoques |

## 3. Cruzamentos canônicos por indicador (visão gerencial)

| Indicador | Fontes cruzadas |
|---|---|
| Receita Bruta | DF-e × EFD ICMS/IPI × EFD Contribuições × ECD × ECF |
| Distribuição de Lucros | DIRF × DIRPF × ECD × ECF × REINF |
| Estoques/CMV | DF-e × EFD ICMS/IPI × ECD × ECF |
| Tributos a Recolher | DF-e × EFDs × ECDs × ECF × DCTF (por tributo: NF-e→ICMS/PIS/COFINS/IPI; EFD ICMS/IPI→ICMS/IPI; EFD Contribuições→PIS/COFINS; DCTF→IPI/PIS/COFINS) |
| Folha de Pagamentos | CAGED × RAIS × eSocial × ECD × ECF |
| Retenções | DIRF × REINF × DCTF × ECD × ECF |
| Fornecedores e Formas de Pagamento | DF-e × EFDs × ECDs × Instituições Financeiras |
| Imobilizado | DF-e × EFD ICMS/IPI × ECD × ECF |
| Capital Social | ECD × ECF × DIRPF |
| Escrituração de Documentos | DF-e × EFDs |

## 4. Camada específica IBS/CBS (Reforma Tributária) — extensão do canônico

Não consta nos mapas (anteriores à LC 214/2025), mas é a mesma lógica aplicada ao novo modelo. Baseado nos gaps reais identificados na RT360:

| Cruzamento IBS/CBS | O que testa | Caso real que originou |
|---|---|---|
| CNAE (cadastro) × NCM completo (item) × Descrição do item × Descrição TIPI × LC 214/2025 | Classificação tributária (cClassTrib) coerente com a atividade real da empresa, não só pelos 6 primeiros dígitos do NCM | Aço-Fer: "Anel de Vedação PVC" classificado como dispositivo médico (redução 100%) só pelo prefixo do NCM |
| CFOP × natureza da operação | Filtrar da base de "Receitas" apenas CFOPs que representam receita de fato — excluir remessa entre filiais, simples remessa, baixa de estoque, devolução, entrega futura (5117/5922) | Aço-Fer: CFOPs de remessa/devolução entrando como receita |
| CFOP × direito a crédito (aquisições) | CFOPs de entrada relevantes (1101, 1253, 1303, 1353, 1407, 1551, 1653, 2407 etc.) precisam aparecer nas aquisições geradoras de crédito; CFOP de serviço (1949) não deve compor crédito de mercadoria mas precisa ter fluxo próprio de tratamento | Aço-Fer: CFOPs de crédito "sumindo" da apuração; 1949 sendo tratado incorretamente |
| CFOP de devolução (1201, 1202, 1411, 2202...) × regra de estorno | Devoluções não podem ser contadas como receita nem como aquisição nova | Levantado por Gustavo/Dorna, sem regra formal ainda |
| Receita Importada (EFD/XML) × Livros/Sistema Contábil | Valor por CFOP e por período deve bater entre o que a plataforma importou e o razão contábil do cliente | DEMIL, Newlook, Carlos Leme, Kaplan, Posto do Grilo: receita importada menor que a contábil — CFOPs 5102, 5106, 6102, 6106 não capturados em alguns meses |
| CT-e × Receita (transportadoras) | Empresas com CNAE de transporte precisam ter o CT-e lido como gerador de receita, não só NF-e | Transportadora Turística Natal: receita não puxava por falha de leitura de CT-e |
| Plano de contas contábil × origem do crédito | Contas contábeis classificadas pelo cliente como "geradoras de crédito" precisam refletir na projeção de aquisições; conta sem origem fiscal deve ser expurgada | Plano de contas padronizado enviado pelo escritório; aquisição de origem contábil não refletindo na projeção |
| Regime tributário (Simples × Lucro Real/Presumido) × dashboard de crédito | Empresa do Simples não deve ser avaliada com os mesmos parâmetros de crédito do Lucro Real/Presumido; projeção de aquisição do Simples não deve puxar CFOP de saída | Projeção de aquisições do Simples Nacional puxando CFOPs de saída |
| Premissa de crescimento × série histórica SPED | Toda empresa precisa de taxa de crescimento (padrão ou calculada pelo histórico); ausência gera projeção distorcida | 21 de 24 empresas do lote sem premissa cadastrada |
| Rastreabilidade: linha de CFOP consolidada × documento fiscal de origem | Toda soma de linha precisa abrir para o(s) documento(s) que a compõem, para permitir auditoria de diferença | Implementado como modal "Origem da Soma — CFOP XXXX" após crítica do Gustavo |

## 4A. Cruzamentos por bloco específico do SPED (granularidade de campo)

Fonte: `IPOG - Perguntas Auditorias Digitais.docx`. Detalha, no nível de bloco/registro, os cruzamentos da seção 2 — usar quando a plataforma precisar apontar exatamente *onde* está a divergência, não só *entre quais obrigações*.

| Bloco/registro | Cruza com | Risco identificado |
|---|---|---|
| Registro C170 (EFD ICMS/IPI — item do documento fiscal) | CST × NCM × CFOP do mesmo item | Classificação tributária do item incoerente com a operação declarada |
| Bloco E (EFD ICMS/IPI — apuração ICMS) | DARE (arrecadação estadual) | ICMS apurado ≠ ICMS recolhido |
| Bloco M (EFD Contribuições — apuração PIS/COFINS) | DARF (arrecadação federal) | PIS/COFINS apurado ≠ PIS/COFINS recolhido |
| Bloco H (EFD ICMS/IPI — inventário) | Documentos Fiscais Eletrônicos e DCTF | Omissão de entrada: Inventário Fiscal < Inventário Físico; estoque valorizado a custo médio ponderado |
| DCTF | SPED Contábil (ECD) | Indicadores de IRRF, Contribuição Sindical, IRPJ, PIS, ICMS, ISS |
| DCTF | DIRF | Retenções declaradas × retenções informadas na fonte |
| e-Financeira | SPED Contábil (ECD) | Movimentação bancária incompatível com o patrimônio declarado (evolução patrimonial) |

Impacto em cadeia de erro de estoque: divergência no Bloco H se propaga para CMV → Resultado Líquido → base de Dividendos/Distribuição de Lucros.

## 4B. Causa raiz e casos de autuação (aplicação prática do cruzamento)

Fonte: `Auditoria_Digital_e_Cruzamentos_de_Informações_Fis.pptx` (material 2026, IPOG). Para cada cruzamento da seção 2, associar não só o risco mas a causa raiz típica — é isso que transforma um alerta de "divergência" num diagnóstico acionável.

Exemplo de padrão causa-raiz (replicar esse formato para os 13 cruzamentos da seção 2 ao expandir o documento):
- **EFD ICMS/IPI × EFD Contribuições (Blocos C e D)** → Risco: os blocos deveriam ser idênticos nas mesmas operações → Causa raiz típica: correção lançada em apenas uma das duas escriturações.

Casos de autuação citados como referência de padrão (problema → causa → solução):
1. Créditos de PIS/COFINS tomados sem NF-e válida na base.
2. Omissão de receita por NF-e emitida e não escriturada.
3. Divergência de estoque por perdas/quebras não documentadas.
4. ICMS com diferimento aplicado incorretamente (fora das hipóteses legais).
5. Substituição Tributária (ST) calculada com MVA/base errada.

## 4C. Softwares de mercado e roteiro de implementação de auditoria digital

Softwares citados no material (para benchmarking de funcionalidade, não recomendação de compra): e-Auditoria, Systax, Becomex, Tax Group, Audição Fiscal — funcionalidades típicas: validação de layout do SPED, cruzamento automático entre obrigações, validação de créditos, dashboards, histórico/rastreabilidade.

Roteiro de implementação em 6 etapas (prazo de referência: 60-90 dias): 1) diagnóstico do ambiente de dados → 2) definição de objetivos/KPIs → 3) escolha/configuração do software → 4) capacitação da equipe → 5) rotinas de execução (mensal/trimestral/anual) → 6) monitoramento contínuo.

## 4D. Simples Nacional — cruzamentos e regras específicas

Fonte: disciplina IPOG "Simples Nacional" (material didático + e-book RCT + relatório-modelo de auditoria + caso prático PGDAS × contábil).

**Cruzamentos aplicáveis ao Simples** (mesma lógica da seção 2, adaptada):
- PGDAS × Escrituração contábil — bater a receita bruta declarada no PGDAS com o razão contábil, por CFOP e por período (caso real testado: `Caso Prático 4 - PRÁTICA SIMPLES NACIONAL_PGDAS.pdf`).
- DCTF × DIRF — retenções sofridas/declaradas.
- DCTF × SPED Contribuições — coerência das apurações informadas.
- DEFIS × CFOPs × Balancete/Resultado — estrutura usada no relatório-modelo `Simples Nacional - Auditoria.doc` (objeto de exame: SPED Fiscal, SPED Contribuições, SPED ECF, SPED Contábil, DIRF, DCTF, 12 meses cada).

**Fator R** (LC 123/2006 art. 18 §§5º-B/5º-D/5º-I/5º-J/5º-K/5º-M/24; LC 155/2016 art. 11 III; Resolução CGSN 94/2011 art. 25-A/26; Resolução CGSN 135/2017): r = Folha de salários 12 meses (com encargos/pró-labore/FGTS/INSS patronal) ÷ Receita bruta 12 meses. r ≥ 28% → Anexo III; r < 28% → Anexo V (atividades intelectuais: TI, engenharia, medicina, arquitetura, consultoria, jornalismo etc.). Ponto de cruzamento/auditoria: folha (eSocial/ECD) × receita bruta (PGDAS) recalculando o r declarado.

**Exclusão do Simples Nacional** — três formas (opção, obrigatória, de ofício). Gatilhos cruzáveis via dados: excesso de receita bruta (>20% → efeito no mês seguinte; ≤20% → efeito no ano-calendário seguinte), atividade vedada, débito tributário, despesas > 20% dos ingressos no período, aquisição de mercadorias > 80% dos ingressos, falta de emissão de documento fiscal, omissão de segurado na folha. Exclusão de ofício impede nova opção por 3 anos-calendário — todos são indicadores testáveis cruzando SPED × folha × notas fiscais.

**RCT (Recuperação de Créditos Tributários) no Simples** — ICMS-ST e PIS/COFINS monofásico frequentemente ficam indevidamente incluídos na base do DAS; LC 147/2014 determinou a exclusão dessas receitas da base de cálculo. Setores mais expostos: bares, restaurantes, distribuidoras de bebida, supermercados, farmácias, postos de gasolina, autopeças, perfumarias. Fontes de cruzamento para o levantamento: PER/DCOMP, DCTF, SPED Fiscal, SPED Contribuições, SPED ECF, SPED Contábil, cadastro de produtos por NCM.

## 5. Checklist de auditoria para uma empresa na RT360 (aplicação prática)

1. **Classificação de itens**: cCLassTrib sugerido bate com CNAE + NCM completo + descrição do item + descrição TIPI + regra da LC 214? Sinalizar toda redução/imunidade que dependa só do prefixo do NCM para revisão manual.
2. **Receitas Importadas**: nenhum CFOP de remessa/devolução/baixa de estoque/entrega futura contando como receita; total bate com o livro fiscal/contábil do cliente por período e por CFOP.
3. **Aquisições — Origem Fiscal**: todos os CFOPs de entrada com direito a crédito aparecem; CFOP 1949 (serviço) não contamina crédito de mercadoria e tem fluxo de importação próprio; devoluções de compra não entram como aquisição nova.
4. **Projeções (Receita e Aquisição)**: fórmula usada nas Projeções é a mesma usada no Dashboard; toda empresa tem premissa de crescimento (padrão ou calculada); regime tributário da empresa (SN × Presumido/Real) reflete no cálculo de crédito exibido.
5. **Rastreabilidade**: toda linha agregada (por CFOP, por conta contábil) tem caminho para os documentos fiscais/XMLs de origem.
6. **Documentos especiais**: CT-e sendo lido corretamente para empresas de transporte; notas de serviço tomado sendo importadas (não só reimportação genérica).
7. **Plano de contas do cliente**: contas marcadas como geradoras de crédito refletem na projeção; contas sem origem fiscal são expurgadas.
8. **Empresas do Simples Nacional**: receita do PGDAS bate com a contábil por CFOP/período; Fator R recalculado a partir de folha × receita bruta confere com o Anexo aplicado; nenhum gatilho de exclusão (receita, atividade vedada, débito, proporção de despesas/aquisições) passou despercebido; CFOPs monofásicos/ST não estão sendo incluídos indevidamente na base do DAS.

## 6. Uso deste documento

Serve de referência para: (a) validar reclamações de "informação incompatível" reportadas por clientes/mentorados na RT360 — verificar se o cruzamento correspondente da tabela foi aplicado; (b) fundamentar pedidos de ajuste de sistema com o time técnico, citando o cruzamento canônico que está sendo violado; (c) treinar novos analistas na lógica de auditoria digital antes de liberá-los para revisão de empresas.
