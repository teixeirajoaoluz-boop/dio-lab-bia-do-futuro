# Código da Aplicação — Farol RTC

Agente consultor sobre a Reforma Tributária (IBS/CBS), com RAG por palavra-chave (BM25) sobre a
`BASE RTC/` na raiz do repositório e LLM via API REST do Google Gemini (chamada direta com
`requests`, sem o SDK `google-generativeai` — veja a nota abaixo).

## Estrutura

```
src/
├── app.py              # Interface do chat (Streamlit)
├── agente.py           # System prompt + orquestração (recupera contexto e chama o Gemini)
├── rag.py              # Indexação e busca por palavra-chave (BM25) sobre a BASE RTC
├── config.py           # Configurações (API key, modelo, caminho da base)
├── requirements.txt    # Dependências
└── .env.example        # Modelo de variáveis de ambiente
```

## Como Rodar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar a chave de API
cp .env.example .env
# edite .env e preencha GEMINI_API_KEY com uma chave do Google AI Studio

# 3. Rodar a aplicação
streamlit run app.py
```

## Notas

- A `BASE RTC/` (raiz do repositório) é lida diretamente do disco — não é reindexada em nenhum
  banco vetorial. A cada início da aplicação, todos os `.md`/`.json` são carregados em memória e
  indexados com BM25 (biblioteca `rank-bm25`).
- Cada resposta do agente cita o(s) arquivo(s)-fonte usados, exibidos como legenda abaixo da
  mensagem no chat.
- `data/perfil_cliente_rtc.json` é injetado em todo turno da conversa para personalizar as
  respostas ao cliente fictício ativo (exibido também na barra lateral do app).
- **Por que REST e não o SDK `google-generativeai`**: o SDK depende de `grpcio`, que em versões
  muito recentes do Python (ex.: 3.14) pode não ter wheel pré-compilada e travar compilando do
  zero por muito tempo. `agente.py` chama `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`
  diretamente com `requests`, evitando essa dependência.
