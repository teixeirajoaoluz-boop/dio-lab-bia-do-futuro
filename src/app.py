"""Interface Streamlit do Farol RTC."""

import json

import streamlit as st

from agente import Agente
from config import CLIENTE_PATH

st.set_page_config(page_title="Farol RTC", page_icon="🧭")
st.title("🧭 Farol RTC")
st.caption("Agente consultor sobre a Reforma Tributária (IBS/CBS) — respostas baseadas na BASE RTC.")

with st.sidebar:
    st.subheader("Cliente ativo")
    if CLIENTE_PATH.exists():
        perfil = json.loads(CLIENTE_PATH.read_text(encoding="utf-8"))
        empresa = perfil.get("empresa", {})
        st.markdown(f"**{empresa.get('razao_social', '—')}**")
        st.caption(empresa.get("descricao_atividade", ""))
        st.caption(f"Regime: {empresa.get('regime', '—')} · CNAE: {empresa.get('cnae_principal', '—')}")
    else:
        st.caption("Nenhum perfil de cliente configurado.")


@st.cache_resource
def carregar_agente() -> Agente:
    return Agente()


if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])
        if mensagem.get("fontes"):
            st.caption("Fontes: " + ", ".join(mensagem["fontes"]))

pergunta = st.chat_input("Pergunte sobre alíquotas, regimes, cronograma de transição...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    try:
        agente = carregar_agente()
    except RuntimeError as erro:
        with st.chat_message("assistant"):
            st.error(str(erro))
    else:
        with st.chat_message("assistant"):
            with st.spinner("Consultando a BASE RTC..."):
                resposta, fontes = agente.responder(pergunta)
            st.markdown(resposta)
            if fontes:
                st.caption("Fontes: " + ", ".join(fontes))
        st.session_state.mensagens.append({"role": "assistant", "content": resposta, "fontes": fontes})
