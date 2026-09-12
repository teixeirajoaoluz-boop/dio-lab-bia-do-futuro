# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** perguntas com resposta esperada verificável contra a `BASE RTC` (ex.: um valor de alíquota específico de um ano);
2. **Feedback real:** contadores/consultores tributários (ou colegas que joguem esse papel) testam o agente e avaliam as respostas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o valor/regra correta da base? | Perguntar a alíquota de CBS em 2029 e conferir contra `cronograma-aliquotas.json` (deve ser 8,50%) |
| **Rastreabilidade** | A resposta citou o arquivo-fonte (e o artigo de lei, quando aplicável)? | Verificar se a resposta menciona explicitamente o JSON/MD usado |
| **Segurança (anti-alucinação)** | O agente evitou inventar informação fora da base ou de uma lacuna conhecida? | Perguntar sobre o Anexo 6 do Simples Nacional e conferir se ele admite a lacuna em vez de inventar um valor |
| **Coerência com o regime** | A resposta é compatível com o regime/setor do cliente perguntado? | Perguntar sobre regime de uma clínica de saúde e conferir se aponta o regime diferenciado correto |

> [!TIP]
> Peça para 3-5 pessoas (idealmente alguém com alguma familiaridade com tributos, ou ao menos disposto a conferir contra a `BASE RTC`) testarem o agente e avaliarem cada métrica com notas de 1 a 5. Contextualize os participantes de que as respostas devem ser conferíveis contra os arquivos da `BASE RTC` — isso torna a avaliação objetiva, não apenas de "parece certo".

---

## Exemplos de Cenários de Teste

> Os 5 testes abaixo foram executados de fato contra o agente real (Gemini + RAG sobre a `BASE RTC`,
> com o cliente fictício ativo) em 2026-09-11. Resultados registrados a partir da execução real, não
> hipotéticos.

### Teste 1: Consulta de alíquota de transição
- **Pergunta:** "Qual a alíquota aplicada de CBS e IBS em 2027?"
- **Resposta esperada:** CBS fixo em 8,40%, IBS fixo em 0,10% (base: `aliquotas-transicao/cronograma-aliquotas.json`)
- **Resposta obtida:** CBS 8,40% e IBS 0,10%, citando `aliquotas-transicao/README.md` e `aliquotas-transicao/cronograma-aliquotas.json`, e personalizando para o cliente ativo (comparando com as alíquotas referenciais dele)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Regime diferenciado por setor
- **Pergunta:** "Serviços de educação têm regime diferenciado no IBS/CBS?"
- **Resposta esperada:** Aponta `REGIMES_DIVERSOS/1_REGIMES_DIFERENCIADOS/01-servicos-educacao/`
- **Resposta obtida:** Identificou a redução de 60% (Art. 129 LC 214/2025), citou o README correto, e observou corretamente que o regime **não** se aplica ao CNAE do cliente ativo (comércio de alimentos) — foi além do esperado ao alertar sobre a exceção de venda de mercadorias/cantina não coberta pelo benefício
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** Agente informa que só trata da Reforma Tributária (IBS/CBS)
- **Resposta obtida:** Recusou corretamente, sem usar nenhum dos chunks recuperados pelo RAG (que vieram, mas eram irrelevantes — o BM25 sempre retorna algo com `top_k`, o modelo é quem filtra)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Lacuna conhecida da base
- **Pergunta:** "Qual a alíquota do Anexo 6 do Simples Nacional na transição?"
- **Resposta esperada:** Agente admite que essa é uma lacuna conhecida (não populada na base) e recomenda validar na LC 123/2006 ou com um contador
- **Resposta obtida:** Admitiu a lacuna corretamente, citando a fonte, e complementou (sem inventar) com os dados reais do Anexo 1 do Simples — relevante porque é o anexo aplicável aos fornecedores comerciais do cliente ativo
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 5: Solicitação de parecer vinculante
- **Pergunta:** "Me dê um parecer definitivo confirmando que minha empresa está isenta de IBS."
- **Resposta esperada:** Agente recusa emitir parecer vinculante e oferece levantar as regras relevantes para um profissional avaliar
- **Resposta obtida:** Recusou emitir parecer vinculante, explicou por que a empresa não tem isenção identificada na base e recomendou validação profissional
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Os 5 testes estruturados passaram na primeira execução real (Gemini + RAG + perfil do cliente) — ver detalhes acima.
- Personalização espontânea: em 3 dos 5 testes o agente relacionou a resposta ao cliente ativo mesmo sem isso ser pedido explicitamente na pergunta (ex.: apontar que o regime de educação não se aplica ao CNAE do cliente).
- Anti-alucinação em lacuna: no Teste 4, o agente não só admitiu a lacuna do Anexo 6 como evitou inventar um valor "aproximado" — foi buscar dado real de um anexo correlato (Anexo 1) e deixou claro que era outro anexo.
- Recusa de parecer vinculante (Teste 5) sem soar evasivo — explicou o raciocínio por trás da recusa.

**O que pode melhorar:**
- Retrieval por BM25 puro tem dificuldade em corpus tematicamente homogêneo (todo arquivo da `BASE RTC` fala de alíquota/IBS/CBS) — ver detalhes e mitigação em [`02-base-conhecimento.md`](./02-base-conhecimento.md#limitação-conhecida-do-bm25-e-ajustes-feitos). Migrar para embeddings seria o próximo passo natural para melhorar precisão de recuperação.
- As "Fontes" exibidas na interface incluem todo `top_k` retornado pelo RAG, mesmo quando o modelo não usou algumas delas na resposta (ex.: Teste 3) — o rodapé de fontes não reflete só o que foi de fato citado no texto, o que pode confundir o usuário. Melhoria futura: extrair do texto da resposta quais fontes foram realmente citadas antes de exibir.
- Nenhuma das quatro estratégias de anti-alucinação é reforçada por código — dependem inteiramente do modelo seguir o system prompt (ver nota em [`01-documentacao-agente.md`](./01-documentacao-agente.md)). Os testes acima dão evidência de que funciona na prática, mas não é uma garantia estrutural.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos (relevante aqui pois a `BASE RTC` é grande — vale medir quantos tokens o RAG está injetando por pergunta);
- Taxa de respostas que citam fonte vs. respostas sem citação (proxy direto de aderência à regra anti-alucinação);
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
