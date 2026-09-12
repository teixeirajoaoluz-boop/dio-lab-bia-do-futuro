# Simples Nacional — regime específico de IBS/CBS

**Este segmento NÃO duplica conteúdo.** A base canônica de Simples Nacional já existe e está
madura em duas pastas na raiz de `GUERRA_MENTORIA_REGRAS RTC`:

- `simples-nacional/` — Anexos I-V da LC 123/2006 (`anexos-lc123.json`), Fator R e sublimite
  (`parametros-simples.json`), e a transição IBS/CBS no DAS com os três cenários (dentro do DAS,
  por fora com regime regular, atual) em `transicao-ibs-cbs.json`.
- `aliquotas-transicao/aliquotas-sn-simples-nacional.json` — alíquotas efetivas reais do SN por
  Anexo e ano (2027-2033).

Este README existe apenas para registrar, no bloco "Regimes Específicos", o ponto que falta
cobrir explicitamente conforme apontado no request: o **regime facultativo próprio do optante,
com creditamento restrito do tomador (art. 47, § 9º, II — não art. 127, ver achado abaixo)**.

## ACHADO IMPORTANTE (2026-08-27): a citação do art. 127 para o creditamento restrito estava ERRADA

Confirmado por leitura direta do texto oficial da LC 214/2025 (Câmara dos Deputados, norma
atualizada): o **art. 127** é, na verdade, o **artigo de abertura do Capítulo II — "DA REDUÇÃO EM
TRINTA POR CENTO DAS ALÍQUOTAS DO IBS E DA CBS"** — regime de redução de 30% para a prestação de
serviços por profissionais de atividade intelectual regulamentada (administradores, advogados,
arquitetos, contabilistas, engenheiros, médicos veterinários etc., 18 categorias, incisos I-XVIII).
Esse artigo **não tem nenhuma relação com Simples Nacional** — é um regime de redução de alíquota
por categoria profissional, tema totalmente distinto.

O artigo real do **creditamento restrito do tomador de fornecedor optante do Simples Nacional** é
o **art. 47, § 9º, inciso II** (Seção XII "Da Não Cumulatividade", dentro do regime geral de
créditos). Texto oficial do § 9º e incisos:

> "§ 9º Na hipótese de o pagamento do IBS e da CBS ser realizado por meio do Simples Nacional,
> quando não for exercida a opção pelo regime regular de que trata o § 3º do art. 41 desta Lei
> Complementar:
> I - não será permitida a apropriação de créditos do IBS e da CBS pelo optante pelo Simples
> Nacional; e
> II - será permitida ao contribuinte sujeito ao regime regular do IBS e da CBS a apropriação de
> créditos do IBS e da CBS correspondentes aos valores desses tributos pagos na aquisição de bens
> e de serviços de optante pelo Simples Nacional, em montante equivalente ao devido por meio desse
> regime."

Ou seja: o **inciso I** veda o creditamento pelo **próprio optante do SN** (ele não pode se
creditar de IBS/CBS enquanto estiver "por dentro" do DAS); o **inciso II** é a regra do
**creditamento restrito do tomador** — o adquirente do regime regular credita-se não da alíquota
cheia destacada, mas do **montante equivalente ao efetivamente devido/recolhido pelo Simples
Nacional** na operação. É exatamente a mecânica já modelada em `transicao-ibs-cbs.json` no cenário
`por_dentro` (`creditoParaAdquirente.limite`) — a mecânica de cálculo estava certa, só a citação
do artigo estava errada.

**Impacto conhecido**: o arquivo `C:\GUERRA_MENTORIA_REGRAS RTC\cadeia-negocios-creditos\regras-credito-aquisicoes.json`
também cita art. 127 para essa regra (mesmo erro) — está **fora do escopo desta tarefa** e não foi
alterado; sinalizado no relatório final para correção em processo separado.

## O que já está coberto em `simples-nacional/transicao-ibs-cbs.json`

- **Cenário "por_dentro"** (IBS/CBS recolhidos junto do DAS): o adquirente do regime regular só
  credita o valor de IBS/CBS **efetivamente embutido no DAS** — não a alíquota cheia
  (`creditoParaAdquirente.limite`, fundamento correto **LC 214/2025, art. 47, § 9º, II** — não
  art. 127, ver achado acima).
- **Cenário "por_fora"** (opção pelo regime regular de apuração de IBS/CBS, mantendo o Simples só
  para os tributos federais/previdenciário): fundamento **art. 41, § 3º** (natureza de opção do
  contribuinte, forma/periodicidade pendente de regulamentação) — crédito ao adquirente passa a
  ser pela **alíquota cheia destacada no documento** (art. 47, § 3º).
- **Redução de 30%** para serviços de profissão intelectual regulamentada (18 categorias) —
  **art. 127** — regime à parte, sem relação com Simples Nacional (ver achado acima); já modelada
  como `reducoesAplicaveis` dentro do cenário "por_fora" — a modelagem em si está correta, apenas
  não deve ser confundida com o creditamento restrito do tomador de fornecedor do SN.
- **Crédito presumido sobre estoque** na entrada do novo regime — **art. 381** (confiança: média).

## Fundamento legal (consolidado e corrigido)

| Regra | Artigo(s) LC 214/2025 |
|---|---|
| Regime geral do SN na Reforma | 99-127 |
| Vedação ao creditamento pelo próprio optante do SN | **art. 47, § 9º, I** |
| Creditamento restrito do tomador de fornecedor optante do SN (limite = valor devido no SN) | **art. 47, § 9º, II** |
| Crédito do adquirente limitado ao destacado no DAS (cenário por_dentro) | art. 47, § 9º, II |
| Opção pelo regime regular de apuração (por fora) | 41, § 3º |
| Crédito pleno ao adquirente na opção "por fora" | 47, § 3º |
| Redução de 30% — profissões intelectuais regulamentadas (SEM relação com SN) | 127 (Capítulo II — regime distinto) |
| Crédito presumido sobre estoque de transição | 381 |
| Cronograma de transição do SN no DAS | 343-348 |

Fonte: LC 214/2025, art. 47, § 9º, incisos I e II — texto oficial consolidado (norma atualizada,
Câmara dos Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).

## Fontes consultadas

- `C:\GUERRA_MENTORIA_REGRAS RTC\simples-nacional\transicao-ibs-cbs.json`
- `C:\GUERRA_MENTORIA_REGRAS RTC\simples-nacional\parametros-simples.json`
- `C:\GUERRA_MENTORIA_REGRAS RTC\simples-nacional\anexos-lc123.json`
- `C:\GUERRA_MENTORIA_REGRAS RTC\aliquotas-transicao\aliquotas-sn-simples-nacional.json`
- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` (tema "Simples Nacional —
  IBS e CBS", MCP `mcp-compliance` → `fonte_lc214_mapa_temas`)

## Lacunas conhecidas

- As lacunas já registradas em `transicao-ibs-cbs.json` (ex.: alíquota de referência do regime
  pleno é premissa, não valor legal fixado; forma/periodicidade da opção "por fora" pendente de
  regulamentação) continuam valendo e não foram reabertas aqui.
- **Divergência não corrigida em produção**: `cadeia-negocios-creditos/regras-credito-aquisicoes.json`
  ainda cita art. 127 para o creditamento restrito do tomador de fornecedor SN — correto é art. 47,
  § 9º, II (ver achado no topo deste README). Fora do escopo desta correção; pendente de decisão
  do processo principal.
