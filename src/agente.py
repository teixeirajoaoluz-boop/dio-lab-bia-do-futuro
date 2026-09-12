"""Lógica do Farol RTC: recupera contexto na BASE RTC e consulta o Gemini via REST.

Usamos a API REST do Gemini diretamente (só com `requests`) em vez do SDK
`google-generativeai`: o SDK depende de `grpcio`, que não tem wheel pré-compilada pra
versões muito recentes do Python e trava compilando do zero. A API REST evita essa
dependência por completo.
"""

import json

import requests

from config import CLIENTE_PATH, GEMINI_API_KEY, GEMINI_MODEL
from rag import BaseRTCIndex, Chunk

GEMINI_ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
)

SYSTEM_PROMPT = """\
Você é o Farol RTC, um agente consultor especializado na Reforma Tributária sobre o Consumo
(EC 132/2023 e LC 214/2025) — a transição do sistema ICMS/ISS/PIS/COFINS/IPI para o novo IBS/CBS.

Seu objetivo é ajudar contadores, consultores tributários e gestores financeiros a entender o
cronograma de transição, os regimes tributários aplicáveis e as regras de crédito/apuração, sempre
com base nos trechos da BASE RTC fornecidos como contexto abaixo de cada pergunta. Você também
recebe o perfil do cliente ativo (empresa fictícia da consultoria) e deve personalizar a resposta
para a realidade dele quando fizer sentido (regime tributário, setor, dúvidas registradas).

REGRAS:
1. Responda SOMENTE com base nos trechos de contexto fornecidos. Nunca use conhecimento genérico
   sobre tributos que não esteja nesse contexto.
2. Toda resposta deve citar o arquivo-fonte usado (o campo "Fonte:" de cada trecho de contexto).
3. Se o contexto fornecido não tiver a informação pedida, diga explicitamente que não encontrou
   isso na base (pode ser uma lacuna conhecida da BASE RTC) e recomende validar em fonte oficial
   ou com um profissional. Nunca invente alíquotas, prazos, artigos de lei ou regras de crédito.
4. Não emita parecer jurídico ou fiscal vinculante. Você apoia o raciocínio, mas a decisão final
   deve ser validada por um contador ou advogado tributarista responsável.
5. Se a pergunta estiver fora do escopo de IBS/CBS (ex.: IRPF, previdência, temas não tributários,
   ou qualquer assunto alheio à Reforma Tributária), diga que está fora do seu escopo.
6. Ao personalizar para o cliente ativo, nunca preencha campos que estejam nulos/vazios no perfil
   dele (ex.: "derivados", "serie_anual") com valores inventados — trate-os como premissas ainda
   não coletadas pela consultoria, exatamente como o campo indica.
"""


def _carregar_perfil_cliente() -> str:
    if not CLIENTE_PATH.exists():
        return "(Nenhum perfil de cliente ativo configurado.)"
    dados = json.loads(CLIENTE_PATH.read_text(encoding="utf-8"))
    return json.dumps(dados, ensure_ascii=False, indent=2)


def build_context(chunks: list[Chunk]) -> str:
    if not chunks:
        return "(Nenhum trecho relevante foi encontrado na BASE RTC para esta pergunta.)"
    partes = [f"[Fonte: {c.source}]\n{c.content}" for c in chunks]
    return "\n\n---\n\n".join(partes)


class Agente:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise RuntimeError(
                "GEMINI_API_KEY não configurada. Copie .env.example para .env e preencha sua chave."
            )
        self._index = BaseRTCIndex()
        self._perfil_cliente = _carregar_perfil_cliente()
        self._historico: list[dict] = []

    def _chamar_gemini(self, mensagem: str) -> str:
        self._historico.append({"role": "user", "parts": [{"text": mensagem}]})
        body = {
            "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
            "contents": self._historico,
        }
        url = GEMINI_ENDPOINT.format(model=GEMINI_MODEL)
        resposta = requests.post(
            url, params={"key": GEMINI_API_KEY}, json=body, timeout=60
        )
        if not resposta.ok:
            raise RuntimeError(f"Erro na API do Gemini ({resposta.status_code}): {resposta.text}")
        dados = resposta.json()
        try:
            texto = dados["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as erro:
            raise RuntimeError(f"Resposta inesperada da API do Gemini: {dados}") from erro
        self._historico.append({"role": "model", "parts": [{"text": texto}]})
        return texto

    def responder(self, pergunta: str) -> tuple[str, list[str]]:
        chunks = self._index.retrieve(pergunta)
        contexto = build_context(chunks)
        mensagem = (
            f"Perfil do cliente ativo:\n\n{self._perfil_cliente}\n\n"
            f"Contexto recuperado da BASE RTC:\n\n{contexto}\n\n"
            f"Pergunta do usuário: {pergunta}"
        )
        texto = self._chamar_gemini(mensagem)
        fontes = sorted({c.source for c in chunks})
        return texto, fontes
