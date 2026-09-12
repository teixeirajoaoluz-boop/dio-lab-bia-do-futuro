"""Configurações do Farol RTC: chave de API, modelo e caminho da base de conhecimento."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

SRC_DIR = Path(__file__).resolve().parent
REPO_ROOT = SRC_DIR.parent
BASE_RTC_PATH = Path(os.getenv("BASE_RTC_PATH", REPO_ROOT / "BASE RTC"))
CLIENTE_PATH = Path(os.getenv("CLIENTE_PATH", REPO_ROOT / "data" / "perfil_cliente_rtc.json"))

TOP_K_CHUNKS = int(os.getenv("TOP_K_CHUNKS", "10"))
