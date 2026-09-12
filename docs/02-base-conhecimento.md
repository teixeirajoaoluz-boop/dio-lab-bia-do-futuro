# Base de Conhecimento

## Dados Utilizados

No lugar dos dados mockados originais do desafio (`data/`), este agente usa a **`BASE RTC`** —
uma base canônica e estática (Markdown + JSON) sobre a Reforma Tributária (IBS/CBS), já curada com
citação de fonte em cada regra:

| Pasta | Formato | Utilização no Agente |
|-------|---------|----------------------|
| `aliquotas-transicao/` | JSON | Cronograma de alíquotas CBS/IBS/ICMS/ISS 2027-2033 e redução de 30% (Art. 127 LC 214/2025) |
| `cadeia-negocios-creditos/` | JSON + MD | Regras de crédito de IBS/CBS por regime do fornecedor e fórmulas do motor de apuração (débito/crédito/saldo) |
| `cfop/` | JSON | Famílias, espelhos e grupos especiais de CFOP para cruzamento fiscal |
| `checklist-dossie/` | JSON + MD | Estrutura de dossiê técnico e checklist de entrega por perfil de cliente |
| `classificacao-produtos/` | MD + JSON | Cadeia NCM→CST→cClassTrib e motor de classificação farmacêutica |
| `fontes/` | MD | Proveniência normativa das regras de cruzamento fiscal/contábil |
| `fontes-legais/` | JSON + MD | Mapeamento tema→artigo da LC 214/2025, hierarquia de fontes (8 níveis), glossário, cronograma oficial e catálogo de normas |
| `formulas-glossario/` | JSON | Glossário de ~199 fórmulas/campos calculados da plataforma de origem |
| `indicadores/` | JSON | Indicadores e regras de cruzamento com tolerância |
| `obrigacoes/` | JSON | Obrigações acessórias e registros de origem |
| `premissas-projecoes/` | JSON + MD | Schema e checklist de premissas mínimas para projeção 2027-2033 |
| `regimes/` | JSON | Exigibilidade por regime tributário e regras de veredito |
| `REGIMES_DIVERSOS/` | MD (25 subpastas) | Regimes diferenciados, específicos e aduaneiros especiais por setor (saúde, educação, cesta básica, ZFM etc.) |
| `simples-nacional/` | JSON | Anexos I-V da LC 123/2006, Fator R, sublimite e transição do IBS/CBS no DAS |

Além da `BASE RTC`, o agente também carrega:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|----------------------|
| `data/perfil_cliente_rtc.json` | JSON | Cliente fictício (empresa de comércio de alimentos) usado para personalizar respostas — ver seção "Adaptações nos Dados" abaixo |

> [!TIP]
> Os arquivos mockados originais do desafio (`historico_atendimento.csv`, `perfil_investidor.json`,
> `produtos_financeiros.json`, `transacoes.csv`) foram removidos de `data/` por não fazerem sentido
> para este caso de uso — foram substituídos pelo par `BASE RTC` + `perfil_cliente_rtc.json`.

---

## Adaptações nos Dados

A `BASE RTC` já veio pronta e estruturada (não é um dos datasets mockados do desafio original) —
ela foi extraída de código-fonte vivo de uma plataforma de consultoria tributária real
(`02_Guerra RTC`) e de um MCP de planejamento (`mcp-planejamento-RTC`), com cada pasta citando o
arquivo de origem da regra. Ela é **estática por decisão**: não há script de regeneração automática,
e lacunas de dado (campos não populados nas fontes originais) estão documentadas explicitamente em
cada `README.md` de subpasta, em vez de terem sido preenchidas com suposição.

Para o agente deste laboratório, a adaptação feita foi: (1) tratar a `BASE RTC` como a base de
conhecimento principal via RAG, e (2) manter a lista de "Lacunas conhecidas" (ver
`BASE RTC/README.md`) como uma tabela de exclusão — se a pergunta cair em um desses pontos, o agente
deve responder admitindo a lacuna em vez de tentar completá-la.

Além disso, criamos `data/perfil_cliente_rtc.json` — um **cliente fictício** (empresa de comércio
de alimentos) para personalizar as respostas, requisito explícito do desafio. Ele não inventa uma
estrutura própria: os campos `empresa`/`ecf`/`derivados`/`crescimento_aa`/`razao_credito`/
`serie_anual` seguem literalmente o contrato de `premissas.json` documentado em
`BASE RTC/premissas-projecoes/schema-premissas.json`, e o bloco `aliquotas_referenciais_guerra_rtc`
segue o conceito descrito em `BASE RTC/aliquotas-transicao/README.md`. Campos como `derivados` e
`serie_anual` foram deixados propositalmente vazios/nulos — simulam um cliente no início da
consultoria, cujas premissas ainda não foram todas coletadas (ver checklist em
`BASE RTC/premissas-projecoes/checklist-premissas-minimas.md`). O agente recebe esse perfil em
todo turno da conversa (ver `agente.py`, método `responder`) e é instruído a nunca preencher esses
campos vazios com valor inventado.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Dado o volume da base (~15 pastas temáticas + 25 subpastas de regimes, em JSON/Markdown), carregar
tudo no prompt não é viável. A estratégia é um **RAG leve**:

1. Indexar os arquivos `.md`/`.json` da `BASE RTC` em chunks (por seção de README, por objeto JSON) em um vetor local (ex.: embeddings + busca por similaridade, ou até busca por palavra-chave para o MVP).
2. Sempre manter no contexto fixo os arquivos "índice" de baixo custo: `fontes-legais/mapa-lc214-artigos.json`, `fontes-legais/glossario-reforma.json` e `fontes-legais/hierarquia-fontes-legais.json` — eles ajudam o agente a saber "onde procurar" e a citar a fonte correta.
3. Recuperar sob demanda (top-k) os arquivos de detalhe relevantes à pergunta (ex.: `aliquotas-transicao/cronograma-aliquotas.json` para perguntas de alíquota, ou a subpasta de `REGIMES_DIVERSOS/` correspondente ao setor perguntado).

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O system prompt (ver [`03-prompts.md`](./03-prompts.md)) é fixo e define persona, regras e formato de
citação. Os trechos da `BASE RTC` recuperados pelo RAG entram como contexto dinâmico por mensagem,
junto com a instrução de que a resposta deve citar o arquivo/fonte utilizado.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Pergunta do usuário: "Qual a alíquota aplicada de CBS e IBS em 2027, para regime normal?"

Contexto recuperado (RAG):
[Fonte: aliquotas-transicao/cronograma-aliquotas.json]
{
  "ano": 2027,
  "cbs_aplicada": { "regra": "fixo", "valor_pct": 8.40 },
  "ibs_aplicada": { "regra": "fixo", "valor_pct": 0.10 },
  "icms_aplicada": { "regra": "percentual_da_referencial", "fator": 1.00 },
  "iss_aplicada": { "regra": "percentual_da_referencial", "fator": 1.00 }
}

[Fonte: fontes-legais/mapa-lc214-artigos.json]
{
  "tema": "cronograma_transicao",
  "artigos_lc214": ["Art. 125", "Art. 126"]
}

Instrução: responda citando o arquivo-fonte e o artigo de lei quando disponível, e deixe claro que
em 2027-2028 CBS e IBS são valores fixos (8,40% e 0,10%), não percentuais sobre a alíquota
referencial da empresa — enquanto ICMS/ISS ainda são cobrados integralmente (fator 1,00).
```

---

## Limitação Conhecida do BM25 e Ajustes Feitos

Ao testar a recuperação com perguntas reais, percebemos que buscas por palavra-chave puro (BM25)
têm dificuldade num corpus tão homogêneo tematicamente quanto a `BASE RTC`: como praticamente todo
arquivo fala de "alíquota", "IBS", "CBS" etc., esses termos perdem poder discriminativo, e um
`README.md` longo (que repete o vocabulário do domínio em prosa) pode superar no ranking um `.json`
compacto que tem o valor exato perguntado.

Dois ajustes foram feitos em `rag.py` para mitigar isso:
1. **Normalização morfológica simples** (sem lib de PT-BR): sem ela, "alíquota" (singular, na
   pergunta) nunca batia com "alíquotas" (plural, no nome do arquivo/conteúdo) — o BM25 só compara
   tokens idênticos.
2. **Peso extra para o caminho do arquivo-fonte** no texto indexado, já que o nome do arquivo/pasta
   costuma ser o resumo mais preciso do conteúdo.

Uma terceira tentativa — dar um peso fixo maior para todo chunk `.json` — foi **revertida**: ela
trouxe de volta arquivos `.json` irrelevantes para o topo do ranking sem de fato resolver a
recuperação do arquivo certo, piorando a precisão geral. Optamos por aumentar `TOP_K_CHUNKS` (de 6
para 10) como rede de segurança em vez de uma regra por tipo de arquivo. Na prática, verificamos que
mesmo quando o `.json` exato não fica entre os primeiros, a seção correspondente do `README.md` da
mesma pasta costuma repetir os valores numéricos em prosa e aparece no top 10 — então a resposta
final ainda sai correta, só citando uma fonte "irmã" (igualmente válida) em vez do JSON.

**Limitação que fica em aberto:** BM25 continua sendo a estratégia mais simples entre as duas
avaliadas (ver [`04-metricas.md`](./04-metricas.md), seção "O que pode melhorar") — para uma versão
futura, migrar para embeddings resolveria esse tipo de caso de forma mais robusta, ao custo de mais
uma dependência e um provedor de embeddings.
