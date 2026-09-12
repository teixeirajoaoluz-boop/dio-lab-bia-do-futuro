# Alíquotas de Transição IBS/CBS/ICMS/ISS (2027-2033) — Guerra RTC

Base canônica das regras de cálculo usadas pela plataforma Guerra RTC para simular a transição
tributária da Reforma (LC 214/2025). Este documento descreve a REGRA DE NEGÓCIO; os valores
numéricos completos estão nos arquivos JSON desta mesma pasta.

## 1. Referencial x Aplicada — o conceito central

Para cada empresa, o operador informa manualmente 4 **alíquotas referenciais** (CBS, IBS, ICMS,
ISS) — a estimativa da carga tributária "plena" daquele tributo para a empresa quando o sistema
novo estiver 100% em vigor. A partir desse referencial, o sistema calcula automaticamente a
**alíquota aplicada** em cada ano do período de transição (2027 a 2033), que é a alíquota que
efetivamente incide naquele ano específico, considerando o cronograma legal de transição
(fonte: backend/base_sql/24_README_ALIQUOTAS_TRANSICAO.md).

A tabela `PROJETOBEF.aliquotas_transicao` armazena, por empresa e ano, os 4 pares de campos
(`*_referencial` e `*_aplicada`) — o referencial é repetido em todas as linhas do mesmo empresa,
e a aplicada varia ano a ano segundo a fórmula de cada tributo (fonte:
backend/base_sql/24_criar_tabela_aliquotas_transicao.sql). A geração é feita pela function
PL/pgSQL `gerar_aliquotas_transicao(empresa_id, cbs_ref, ibs_ref, icms_ref, iss_ref)`, que apaga
os registros antigos da empresa (não duplica) e insere as 7 linhas (2027 a 2033) recalculadas
(fonte: backend/base_sql/24_criar_function_gerar_aliquotas_transicao.sql).

## 2. Cronograma de conversão referencial → aplicada (regime normal)

A lógica de cada tributo segue um padrão distinto, refletindo o desenho da Reforma: CBS e IBS
"nascem" pequenos e sobem até virar o tributo pleno; ICMS e ISS começam no valor cheio e são
extintos gradualmente até zerarem em 2033 (fonte:
backend/base_sql/24_criar_function_gerar_aliquotas_transicao.sql).

- **CBS** (federal, substitui PIS/COFINS): valor **fixo absoluto**, não depende do referencial.
  8,40% em 2027-2028; 8,50% de 2029 a 2033.
- **IBS** (estadual/municipal, substitui ICMS/ISS): em 2027-2028 é fixo em 0,10% (fase de teste,
  irrelevante para o referencial). De 2029 em diante passa a ser um **percentual crescente do
  referencial informado**: 10% (2029) → 20% (2030) → 30% (2031) → 40% (2032) → 100% (2033, IBS
  pleno).
- **ICMS**: mantém 100% do referencial em 2027-2028, depois cai em degraus de 10 pontos
  percentuais ao ano (90% em 2029, 80% em 2030, 70% em 2031, 60% em 2032) até ser **extinto
  (0%) em 2033**.
- **ISS**: segue exatamente a mesma curva de queda do ICMS (100% → 90% → 80% → 70% → 60% → 0%
  em 2033).

Note a simetria: o que o ICMS/ISS perdem em alíquota é, por desenho da Reforma, absorvido pelo
IBS crescente — 2033 é o primeiro ano em que o sistema novo (CBS+IBS) opera sozinho, sem
ICMS/ISS residual (fonte: backend/base_sql/24_criar_function_gerar_aliquotas_transicao.sql e
24_README_ALIQUOTAS_TRANSICAO.md). O cronograma completo ano a ano, incluindo o exemplo numérico
prático documentado no README de origem (referencial CBS 8,50 / IBS 5,00 / ICMS 18,00 / ISS
5,00), está em `cronograma-aliquotas.json`.

## 3. Os "3 casos" de fornecedor no cálculo de crédito

A investigação desta base identificou, nos scripts populacionais (20_ e 21_), que a plataforma
trata o fornecedor de um jeito diferente dependendo de qual das 3 situações ele se enquadra ao
calcular a alíquota efetiva de IBS/CBS a aplicar sobre a operação:

1. **Fornecedor optante pelo Simples Nacional**: não usa o cronograma referencial→aplicada do
   regime normal. Em vez disso, consulta a tabela `PROJETOBEF.aliquota_sn_ibs_cbs`, que traz a
   alíquota EFETIVA de CBS e IBS já pronta por Anexo do Simples (1 a 5, faixa de receita MÉDIA) e
   por ano (2027/2028, 2029, 2030, 2031, 2032, 2033) — números vindos diretamente da tabela
   oficial de conversão do Simples Nacional para o IBS/CBS, sem fórmula proporcional (fonte:
   backend/base_sql/20_criar_tabela_aliquota_sn_ibs_cbs.sql e
   backend/base_sql/20_popular_aliquota_sn_ibs_cbs.py, dados originais em
   `01_api_participantes/DADOS API PARTICIPANTES/#ALIQUOTA_SN_IBS_CBS.csv`). Os valores extraídos
   estão em `aliquotas-sn-simples-nacional.json`. **Atenção**: o CSV populado só contém os Anexos
   1 a 5 — o comentário do script SQL cita Anexos "1, 2, 3, 4, 5, 6", mas não há dado do Anexo 6
   no arquivo fonte do repositório.
2. **Produto/atividade encontrado com direito à redução de 30%**: quando a atividade principal do
   fornecedor (ou, por extensão, a razão social/CNAE) contém alguma das palavras-chave associadas
   às profissões regulamentadas do Art. 127 da LC 214/2025 (ex.: "advocacia", "contabilidade",
   "engenharia"), o sistema aplica uma **redução de 30% sobre a alíquota de IBS/CBS** que seria
   devida. Essa regra é puramente de **busca textual** (`LIKE`/`ILIKE` sobre a atividade
   principal, case-insensitive) contra a tabela `PROJETOBEF.reducao_ibs_cbs_30`, que guarda ~120
   palavras/variações cobrindo as 18 categorias legais (fonte:
   backend/base_sql/21_criar_tabela_reducao_ibs_cbs_30.sql e
   backend/base_sql/21_popular_reducao_ibs_cbs_30.py). A lista completa está em
   `reducao-30-por-cento.json`.
3. **Produto/fornecedor não encontrado em nenhuma regra especial**: cai no caminho padrão —
   aplica-se a alíquota **referencial** da empresa (fluxo descrito nas seções 1 e 2 acima), sem
   nenhum ajuste adicional de Simples Nacional ou de redução de 30%.

## 4. Lacunas e dados não disponíveis estaticamente

- **Redução de 30% para PRODUTOS/mercadorias (não serviços)**: os scripts 20_/21_ revisados só
  populam uma tabela de palavras-chave para **serviços de profissões regulamentadas** (Art. 127).
  Não existe, no repositório, nenhuma tabela ou script que popule uma lista de produtos, NCMs ou
  categorias de mercadoria com redução de 30% — se essa regra existir na plataforma para
  produtos, seu dado concreto não está materializado em seed estático nos arquivos revisados.
  Isso está sinalizado explicitamente em `reducao-30-por-cento.json` (campo
  `gap_identificado`) — não foi inventado nenhum valor.
- **Anexo 6 do Simples Nacional**: citado apenas em comentário de código, sem dado populado no
  CSV fonte (ver seção 3, item 1).
- **Alíquotas referenciais por empresa**: são sempre input manual (não há seed/CSV de valores
  reais de empresas no repositório) — o cronograma desta base descreve apenas a FÓRMULA de
  conversão, não valores de empresas específicas.

## 5. Arquivos desta pasta

- `cronograma-aliquotas.json` — regra de conversão referencial → aplicada, ano a ano (regime
  normal), 2027-2033.
- `aliquotas-sn-simples-nacional.json` — alíquotas efetivas de CBS/IBS por Anexo do Simples
  Nacional (dado concreto extraído do CSV populado no repositório).
- `reducao-30-por-cento.json` — palavras-chave/categorias de serviço com direito à redução de
  30%, e o gap identificado quanto a produtos/mercadorias.
