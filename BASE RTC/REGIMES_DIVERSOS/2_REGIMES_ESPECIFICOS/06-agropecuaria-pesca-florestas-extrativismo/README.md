# Agropecuária, Pesca, Florestas e Extrativismo — Crédito Presumido do Produtor Rural + Redução de 60%

## 1. Fundamento legal — dois institutos distintos, não confundir

O tema "Produtor Rural e Agronegócio" já estava mapeado em
`fontes-legais/mapa-lc214-artigos.json` como **arts. 128-137**. A pesquisa desta rodada (RAG +
estudo já existente no projeto irmão BUFON) mostrou que esse intervalo cobre a **redução de
alíquota** (instituto 1), enquanto o **crédito presumido do adquirente** de produtor rural não
contribuinte — o mecanismo de cálculo mais distintivo do setor — está em **arts. 163-168**,
**fora** do intervalo originalmente mapeado. Isso já havia sido identificado e documentado no
estudo `01_ESTUDO_CREDITO_PRESUMIDO_PRODUTOR_RURAL.md` do projeto BUFON & Frasson RTC (ver Fontes).

| Instituto | Artigo(s) confirmado(s) | O que faz |
|---|---|---|
| Redução de 60% das alíquotas | **art. 137** | Produtos agropecuários/aquícolas/pesqueiros/florestais/extrativistas *in natura* e insumos agropecuários (rol do art. 128, incisos VIII-IX) |
| Redução a zero (cesta básica estendida) | **art. 148** | Hortícolas, frutas e ovos listados em anexo — categoria distinta da redução de 60% |
| Definição de produtor rural não contribuinte | **art. 164** | Receita < R$ 3.600.000/ano-calendário |
| Corte de obrigatoriedade / opção / renúncia | **arts. 165 e 166** | PF/PJ com receita ≥ R$ 3,6 milhões é contribuinte automaticamente (art. 165, § 3º); abaixo disso pode optar/renunciar |
| Crédito presumido ao adquirente | **art. 168** (caput e §§ 1º-10) | Fórmula de cálculo do crédito na compra de produtor rural/integrado não contribuinte |
| Extensão a cooperativas | **art. 168, § 9º** | Associado não contribuinte e não optante do SN; exceto beneficiamento com retorno |

**Confirmação por leitura direta do texto oficial (2026-08-27)**: o Título IV, Capítulo VII —
"DO PRODUTOR RURAL E DO PRODUTOR RURAL INTEGRADO NÃO CONTRIBUINTE" — abre exatamente no
**art. 164** (não contribuinte, limite de R$ 3.600.000,00/ano-calendário) e se estende até o
**art. 168** (crédito presumido do adquirente, fórmula e §§ 1º-10). Os arts. 165-167 tratam de
opção/renúncia ao regime de não contribuinte e atualização anual do limite pelo IPCA. A tabela
acima está correta e confirmada linha a linha contra o texto oficial.

Fonte: LC 214/2025, arts. 164 a 168 — texto oficial consolidado (norma atualizada, Câmara dos
Deputados,
https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.pdf).

## 2. Regra específica — em que difere do regime geral

O regime geral gera crédito ao adquirente **espelhando o débito do fornecedor** (não cumulatividade
plena). O produtor rural pessoa física (ou PJ com receita abaixo do limite) normalmente **não é
contribuinte** — logo, não há débito na venda dele, e o regime geral vedaria qualquer crédito ao
comprador (art. 49 e parágrafo único da LC 214/2025: isenção/imunidade/não sujeição não geram
crédito, salvo previsão expressa).

O art. 168 cria essa exceção expressa: um **crédito presumido**, calculado por fórmula própria —
**não** espelha nenhum débito real do produtor (que não existiu), é um valor fixado por política
pública para não penalizar quem compra de produtor rural não contribuinte.

### Fórmula (Regulamento CBS, art. 247, espelho do art. 168, § 3º)

```
CP = (VO × C) / (1 + C)
```

- `CP` = crédito presumido
- `VO` = valor da operação (valor pago ao produtor; se produtor integrado, é a remuneração do
  contrato de integração — art. 168, § 2º)
- `C` = coeficiente do percentual oficial do período, definido **anualmente até setembro** por ato
  conjunto do Ministro da Fazenda e do Comitê Gestor do IBS, com vigência a partir de 1º de janeiro
  do ano seguinte (art. 168, § 4º), calculado pela proporção entre o IBS/CBS cobrado nas aquisições
  de produtores não contribuintes e o valor desses fornecimentos, em média de até 5 anos-calendário
  (§ 5º, com flexibilização 2027-2031 no § 10)

O documento fiscal da aquisição deve discriminar: (i) valor da operação, (ii) valor do crédito
presumido, (iii) valor líquido fiscal = (i) − (ii) (art. 168, § 1º, I-III).

**O coeficiente `C` não tem valor numérico fixado na própria lei** — depende do ato conjunto
anual, que não foi localizado nesta pesquisa (ver Lacunas). O motor de cálculo do projeto BUFON
trata isso corretamente: bloqueia o cálculo se `C` não estiver cadastrado, em vez de assumir um
valor (`creditoPresumidoArt168.js`, função `calcularCreditoArt168` retorna status `BLOQUEADO`,
motivo `SEM_C`, quando o coeficiente é nulo).

## 3. Exemplo de cálculo numérico

**Cenário hipotético**: adquirente do regime regular compra R$ 100.000 em produtos de um produtor
rural pessoa física não contribuinte (receita anual abaixo de R$ 3,6 milhões). Suponha, apenas
para fins didáticos (o valor real de `C` não está confirmado — ver Lacunas), um coeficiente
`C = 0,10`:

```
VO = 100.000
C  = 0,10 (hipotético — não é o valor oficial)
CP = (100.000 × 0,10) / (1 + 0,10) = 10.000 / 1,10 = R$ 9.090,91
VL = VO − CP = 100.000 − 9.090,91 = R$ 90.909,09
```

O adquirente apropria R$ 9.090,91 de crédito presumido (segregado entre IBS e CBS conforme a
fração de cada tributo), mesmo sem ter havido qualquer débito de IBS/CBS na venda do produtor.

**Depois, na revenda** (regime geral, produto agropecuário com redução de 60% do art. 137): se o
adquirente revende o produto por R$ 130.000 e a alíquota de referência fosse ~17,7%
(IBS+CBS, ilustrativo):

```
Alíquota efetiva (com redução de 60%) = 17,7% × (1 − 60%) = 7,08%
Débito na revenda ≈ 130.000 × 7,08% ≈ R$ 9.204
Crédito a abater = crédito presumido da compra (R$ 9.090,91) + eventuais outros créditos
Saldo a recolher ≈ 9.204 − 9.090,91 ≈ R$ 113,09 (antes de outros créditos)
```

Isso demonstra a combinação dos dois institutos: a **redução de 60%** (art. 137) reduz a alíquota
na saída, e o **crédito presumido** (art. 168) neutraliza a ausência de débito na entrada — dois
mecanismos diferentes, cada um agindo em uma ponta da cadeia, e nenhum dos dois é "só uma alíquota
menor".

## 4. Fontes consultadas

- `C:\GUERRA_MENTORIA_REGRAS RTC\fontes-legais\mapa-lc214-artigos.json` — tema "Produtor Rural e
  Agronegócio" (arts. 128-137).
- `C:\Projetos Tecnologicos\01_Projeto BUFON & FRASSON RTC\PROJETO TECNOLOGICO\V3 - 15062026\00_Base_Canonica\02_Crédito Presumido de Produtir Rural - IBS e CBS\01_ESTUDO_CREDITO_PRESUMIDO_PRODUTOR_RURAL.md`
  — estudo dedicado, já identifica e resolve a divergência 128-137 vs 163-168, cita arts. 49, 164,
  165, 166, 167, 168, 271, 381 com trechos.
- `C:\Projetos Tecnologicos\01_Projeto BUFON & FRASSON RTC\PROJETO TECNOLOGICO\V3 - 15062026\backend\modules\dossie-vf\engine\creditoPresumidoArt168.js`
  — motor de cálculo real já implementado (fórmula `CP=(VO×C)/(1+C)`, bloqueio quando `C` ausente).
- MCP `mcp-rag-reforma` (`buscar_reforma`, tier="chunk") — confirmação do art. 137 (redução de 60%)
  e art. 148 (redução a zero, cesta básica estendida).

## 5. Lacunas conhecidas

- **Valor numérico do coeficiente `C`** do crédito presumido (art. 168, §§ 4º-6º) — depende de ato
  conjunto anual do Ministro da Fazenda e do Comitê Gestor do IBS; não localizado nesta pesquisa
  nem no estudo BUFON (marcado lá como "PENDENTE DE FONTE / ATO CONJUNTO"). O exemplo numérico
  usa `C = 0,10` apenas como valor didático.
- **Diferenciação de `C` por categoria de bem/serviço, nível de receita e tipologia do produtor**
  (art. 168, § 6º, redação dada por LC 227) — mecânica qualitativa confirmada, sem tabela de
  valores.
- **Requisito de CAD/PRO / inscrição estadual** para o produtor — não encontrado como exigência
  expressa do art. 168 (registrado como pendente também no estudo BUFON).
- **Regra específica de produtor rural PJ optante do Simples Nacional** — remete a Res. CGIBS
  n. 6/2026 e ao art. 41, § 3º combinado com art. 165; detalhamento operacional completo não
  consolidado.
- **Alíquota exata da redução de 60%** — confirmada como percentual (art. 137), mas a alíquota de
  referência total sobre a qual incide (~17,7%) é ilustrativa, não um valor legal fixado (depende
  de resolução do Comitê Gestor).
