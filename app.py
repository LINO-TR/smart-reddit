import streamlit as st
import os
import sys

# Garante que o Python veja as pastas no Celular/Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetchers import cot
from engine.scorer import decide
from reddit import poster

st.set_page_config(page_title="Smart Money", page_icon="💰")

st.title("💰 Smart-Money Signals")

# --- Lógica de Estado (Garante que os dados não sumam no celular) ---
if 'dados' not in st.session_state:
    st.session_state.dados = None
if 'analise' not in st.session_state:
    st.session_state.analise = None

# --- BOTÃO 1: BUSCAR DADOS ---
if st.button("🔍 Buscar Dados e Analisar"):
    with st.spinner("Acessando relatórios institucionais..."):
        # Importante: certifique-se que o cot.get() retorna o dicionário esperado pelo scorer
        st.session_state.dados = {"EUR": cot.get()}
        st.session_state.analise = decide(st.session_state.dados)

# --- EXIBIÇÃO DOS RESULTADOS ---
if st.session_state.analise:
    st.markdown("---")
    st.subheader(f"Resultado: {st.session_state.analise}")
    st.json(st.session_state.dados)
    st.markdown("---")

    # --- BOTÃO 2: POSTAR NO REDDIT (Agora fora do if do primeiro botão) ---
    if st.button("📨 Confirmar Postagem no Reddit"):
        with st.spinner("Publicando no r/SmartMoneyBr..."):
            res = poster.post(st.session_state.dados, st.session_state.analise)
            st.success(res)
            
