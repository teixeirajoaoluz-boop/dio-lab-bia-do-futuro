# Regimes Aduaneiros Especiais — Suspensão/Diferimento de IBS/CBS na Importação

## 1. Fundamento legal

LC 214/2025, Título II "Dos Regimes Aduaneiros Especiais e dos Regimes de Bagagem, de Remessas
Internacionais e de Fornecimento de Combustível para Aeronaves em Tráfego Internacional",
Capítulo I "Dos Regimes Aduaneiros Especiais" — confirmado por leitura do texto oficial
consolidado: **art. 84** (Seção I "Do Regime de Trânsito"), **art. 85** (Seção II "Dos Regimes de
Depósito" — abrange entreposto aduaneiro), **art. 88-89** (Seção III "Dos Regimes de Permanência
Temporária" — admissão temporária), **art. 90** (Seção IV "Dos Regimes de Aperfeiçoamento" — Recof,
drawback-suspensão, admissão temporária para aperfeiçoamento ativo, exportação temporária para
aperfeiçoamento passivo).

Fonte: LC 214/2025, arts. 84-90 — texto oficial consolidado (norma atualizada, Câmara dos
Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).

## 2. Regra específica — em que difere do regime geral

No regime geral de importação, o IBS/CBS incide no desembaraço aduaneiro do bem importado, com
direito a crédito para o importador contribuinte (arts. 6-9 — fato gerador de importação). Os
regimes aduaneiros especiais do art. 90 **suspendem** essa incidência enquanto o bem permanecer
sob o regime, mecânica que difere do regime geral em dois pontos centrais:

1. **Diferimento condicionado à finalidade do bem, não ao momento da operação**: o IBS/CBS não é
   exigido no desembaraço, mas fica **suspenso** até que se defina o destino final do bem —
   reexportação (extinguindo a obrigação, sem nunca haver tributo devido) ou nacionalização
   definitiva (convertendo a suspensão em exigibilidade, com apuração retroativa ao desembaraço,
   normalmente com acréscimos legais se o prazo do regime for descumprido).
2. **Entreposto aduaneiro** (art. 85): o bem fica armazenado sob controle aduaneiro sem que a
   importação se complete para fins tributários — o IBS/CBS só nasce se e quando o bem sai do
   entreposto para consumo interno; enquanto armazenado, não há fato gerador consumado.

Isso é qualitativamente diferente de uma isenção ou alíquota zero: **o tributo não é dispensado**,
apenas tem sua exigibilidade **suspensa e condicionada a evento futuro** (reexportação vs.
nacionalização) — se o bem for nacionalizado, o IBS/CBS acaba sendo devido, ao contrário de uma
operação genuinamente desonerada.

## 3. Exemplo de cálculo numérico

**Cenário**: empresa importa insumo de R$ 1.000.000 sob regime de drawback-suspensão (art. 90) para
industrializar e reexportar o produto final integralmente.

1. **Desembaraço aduaneiro sob o regime**: IBS/CBS **suspenso** — nenhum valor é recolhido no
   momento da importação, diferente do regime geral em que haveria exigência imediata (e posterior
   direito a crédito). Usando a alíquota de referência ilustrativa de ~17,7% apenas para
   dimensionar o valor que fica suspenso: `1.000.000 × 17,7% ≈ R$ 177.000` de IBS/CBS **não
   recolhido no momento**, mas também **sem crédito gerado** enquanto durar a suspensão.
2. **Hipótese A — reexportação dentro do prazo do regime**: a suspensão se converte em extinção
   da obrigação. Nenhum IBS/CBS é devido sobre o insumo importado — resultado equivalente (mas por
   mecanismo distinto) a uma operação de exportação, que já é imune por natureza (art. 49 e
   seguintes da LC 214/2025).
3. **Hipótese B — a empresa desiste de reexportar e nacionaliza o insumo**: a suspensão se converte
   em exigibilidade. O IBS/CBS de R$ 177.000 passa a ser devido, com o fato gerador retroagindo à
   data do desembaraço original — normalmente sujeito a juros/multa por descumprimento do regime
   (o detalhamento desses acréscimos não foi confirmado nesta pesquisa, ver Lacunas).

O ponto de mecânica distinta frente ao regime geral: **não existe, em nenhum momento, um crédito
"pendente" a ser usado pelo importador** enquanto o bem estiver sob o regime — diferente do regime
geral, em que o importador contribuinte recolhe e imediatamente tem direito ao crédito. Aqui, a
neutralização acontece pela não incidência condicionada, não pelo mecanismo de créditos e débitos.

## 4. Fontes consultadas

- Texto oficial consolidado da LC 214/2025 (norma atualizada, incorpora LC 227/2025), Câmara dos
  Deputados — leitura literal dos arts. 84 a 90 (Título II, Capítulo I).
- MCP `mcp-rag-reforma` (`buscar_reforma`, tier="chunk") — arts. 84, 85, 90, 95, 96, 97, 99 da
  LC 214/2025 (pesquisa anterior, agora confirmada por texto literal).
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — tema não coberto nos 17
  mapeados anteriormente.

## 5. Lacunas conhecidas

- **Percentual/valor de acréscimos legais** (juros/multa) em caso de descumprimento do prazo do
  regime (nacionalização após vencimento) — não pesquisado (o art. 89, §2º remete à correção pela
  Selic para o caso de admissão temporária com pagamento parcial, mas os acréscimos moratórios
  específicos para descumprimento do regime de trânsito/depósito/aperfeiçoamento não foram
  detalhados nesta pesquisa).
- **Jurisprudência consolidada de drawback no regime antigo** (PIS/COFINS/ICMS-importação) como
  pano de fundo interpretativo — o request do usuário aponta isso como potencialmente útil, mas os
  MCPs `guerra-stf`/`guerra-stj`/`guerra-cjf` não foram consultados nesta rodada; a extrapolação de
  jurisprudência do regime antigo para IBS/CBS é, de todo modo, incerta por ser tributo novo — deve
  ser tratada como "pano de fundo", não como precedente direto.
- **Regulamentação infralegal** (Decreto/Resolução CGIBS/RFB) detalhando prazos, condições de
  habilitação e obrigações acessórias específicas por tipo de regime (Recof, drawback, admissão
  temporária, entreposto) — não pesquisada; a LC 214/2025 provavelmente remete a normas
  infralegais para esses detalhes operacionais.
- Texto integral literal dos artigos citados não foi obtido via fetch direto do Planalto — vieram
  de paráfrase/trecho do RAG.
