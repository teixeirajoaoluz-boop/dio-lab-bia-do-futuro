# 🧭 Farol RTC — Agente Consultor sobre a Reforma Tributária

Projeto do desafio de encerramento "Agente Financeiro Inteligente com IA Generativa" da DIO,
adaptado para um caso de uso específico: um agente consultor especialista na **Reforma Tributária
sobre o Consumo** (EC 132/2023 e LC 214/2025) — a transição do sistema ICMS/ISS/PIS/COFINS/IPI para
o novo IBS/CBS (2027-2033).

## O Que Ele Faz

Contadores, consultores tributários e gestores financeiros de empresas precisam entender um
cronograma de transição que muda ano a ano, dezenas de regimes diferenciados por setor e regras de
crédito que dependem do regime do fornecedor — tudo isso espalhado em milhares de páginas de norma.

O **Farol RTC** responde essas perguntas consultando uma base de conhecimento canônica e curada (a
[`BASE RTC/`](./BASE%20RTC/)), sempre citando o arquivo-fonte usado. Quando a informação não existe
na base — uma "lacuna conhecida" já documentada —, ele admite isso explicitamente em vez de
inventar. Ele também personaliza as respostas para um cliente fictício ativo
([`data/perfil_cliente_rtc.json`](./data/perfil_cliente_rtc.json)), simulando o início de uma
consultoria real.

> [!TIP]
> Quer entender por que esse caso de uso foi escolhido no lugar do "agente financeiro" genérico
> sugerido pelo desafio original? Veja [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md).

## Como Rodar

```powershell
cd src
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# copie .env.example para .env e preencha sua GEMINI_API_KEY antes de rodar
Copy-Item .env.example .env

.\.venv\Scripts\python.exe -m streamlit run app.py
```

Mais detalhes (variáveis de ambiente, arquitetura do RAG) em [`src/README.md`](./src/README.md).

## Documentação do Projeto

| Documento | Conteúdo |
|---|---|
| [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md) | Caso de uso, persona, arquitetura e estratégias anti-alucinação |
| [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md) | Como a `BASE RTC` é usada, estratégia de RAG e suas limitações conhecidas |
| [`docs/03-prompts.md`](./docs/03-prompts.md) | System prompt, exemplos de interação e edge cases |
| [`docs/04-metricas.md`](./docs/04-metricas.md) | Métricas de avaliação e resultados reais dos testes executados |
| [`docs/05-pitch.md`](./docs/05-pitch.md) | Roteiro do pitch de 3 minutos |

## Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 BASE RTC/                       # Base de conhecimento canônica (Reforma Tributária)
│   └── ... (alíquotas, regimes, CFOP, fontes legais, Simples Nacional etc.)
│
├── 📁 data/
│   └── perfil_cliente_rtc.json        # Cliente fictício usado para personalizar respostas
│
├── 📁 docs/                           # Documentação do projeto (ver tabela acima)
│
├── 📁 src/                            # Aplicação do agente
│   ├── app.py                         # Interface Streamlit
│   ├── agente.py                      # System prompt + chamada ao Gemini (via REST)
│   ├── rag.py                         # Busca por palavra-chave (BM25) sobre a BASE RTC
│   ├── config.py                      # Configurações e variáveis de ambiente
│   └── requirements.txt
│
├── 📁 assets/                         # Roteiro original do desafio (referência)
│
└── 📁 examples/                       # Referências do desafio original da DIO
```

## Aviso

Este é um projeto de estudo. As respostas do Farol RTC têm caráter consultivo e não substituem
parecer de um contador ou advogado tributarista responsável — ver limitações declaradas em
[`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md).
