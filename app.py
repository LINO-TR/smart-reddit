import streamlit as st, os, sys
# Garante que o Python veja as pastas no Celular/Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetchers import cot
from engine.scorer import decide
from reddit import poster

st.set_page_config(page_title="Smart Money", page_icon="💰")

st.title("💰 Smart-Money Signals")

if st.button("Buscar Dados e Analisar"):
    details = {"EUR": cot.get()}
    call = decide(details)
    st.subheader(f"Resultado: {call}")
    
    if st.button("Confirmar Postagem no Reddit"):
        res = poster.post(details, call)
        st.success(res)
      
