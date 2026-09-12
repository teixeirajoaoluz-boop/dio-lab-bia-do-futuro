"""RAG por palavra-chave (BM25) sobre a BASE RTC.

Sem embeddings: cada arquivo .json vira um chunk (a base já é curada e pequena por
arquivo) e cada .md é dividido por seção (títulos '#'/'##'). O objetivo é sempre
conseguir apontar o arquivo-fonte exato usado para montar a resposta.
"""

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from rank_bm25 import BM25Okapi

from config import BASE_RTC_PATH, TOP_K_CHUNKS

HEADING_RE = re.compile(r"^#{1,3}\s+.*$", re.MULTILINE)
TOKEN_RE = re.compile(r"[a-z0-9]+")


@dataclass
class Chunk:
    source: str  # caminho relativo dentro da BASE RTC, ex: "aliquotas-transicao/cronograma-aliquotas.json"
    content: str


def _strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))


def _singularize(token: str) -> str:
    # Normalização morfológica bem simples (sem libs externas de PT-BR): sem isso,
    # "alíquota" (pergunta) nunca casa com "alíquotas" (conteúdo/nome de arquivo) no
    # BM25, que só compara tokens idênticos. Aplicada igualmente a query e corpus.
    if token.isdigit() or len(token) <= 3:
        return token
    if token.endswith(("oes", "aes")):
        return token[:-3] + "ao"
    if token.endswith("res") or token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def _tokenize(text: str) -> list[str]:
    tokens = TOKEN_RE.findall(_strip_accents(text.lower()))
    return [_singularize(t) for t in tokens]


def _split_markdown(text: str) -> list[str]:
    positions = [m.start() for m in HEADING_RE.finditer(text)]
    if not positions:
        return [text]
    positions.append(len(text))
    return [text[positions[i]:positions[i + 1]].strip() for i in range(len(positions) - 1) if text[positions[i]:positions[i + 1]].strip()]


def _load_chunks(base_path: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    for file_path in sorted(base_path.rglob("*")):
        if not file_path.is_file() or file_path.suffix not in (".json", ".md"):
            continue
        relative = file_path.relative_to(base_path).as_posix()
        text = file_path.read_text(encoding="utf-8")

        if file_path.suffix == ".json":
            try:
                parsed = json.loads(text)
                text = json.dumps(parsed, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                pass
            chunks.append(Chunk(source=relative, content=text))
        else:
            for section in _split_markdown(text):
                chunks.append(Chunk(source=relative, content=section))
    return chunks


class BaseRTCIndex:
    def __init__(self, base_path: Path = BASE_RTC_PATH):
        self.base_path = base_path
        self.chunks = _load_chunks(base_path)
        if not self.chunks:
            raise RuntimeError(f"Nenhum arquivo .md/.json encontrado em: {base_path}")
        # Repete os termos do caminho-fonte para dar mais peso a eles: nomes de
        # arquivo/pasta (ex.: "cronograma-aliquotas") costumam ser o resumo mais preciso
        # do conteúdo, e sem isso READMEs longos (que repetem termos do domínio em
        # prosa) dominam o ranking sobre os JSON compactos que têm o dado exato.
        corpus = [_tokenize(c.source) * 4 + _tokenize(c.content) for c in self.chunks]
        self._bm25 = BM25Okapi(corpus)

    def retrieve(self, query: str, top_k: int = TOP_K_CHUNKS) -> list[Chunk]:
        scores = self._bm25.get_scores(_tokenize(query))
        ranked = sorted(range(len(self.chunks)), key=lambda i: scores[i], reverse=True)
        return [self.chunks[i] for i in ranked[:top_k] if scores[i] > 0]
