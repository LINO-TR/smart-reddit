import streamlit as st
import os
import sys

# Ajuste de caminho para o servidor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetchers import cot, cls, block, btc_top
from engine.scorer import decide
from reddit import poster

# Configuração da Página
st.set_page_config(page_title="Smart Money Panel", page_icon="📈", layout="wide")

# Estilização Personalizada para esconder o JSON feio
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Smart Money Intelligence")
st.write(f"**Usuário:** {os.getenv('REDDIT_USER', 'Operador')}")

# --- Lógica de Estado ---
if 'dados' not in st.session_state:
    st.session_state.dados = None
if 'analise' not in st.session_state:
    st.session_state.analise = None

# --- BARRA LATERAL (AÇÕES) ---
with st.sidebar:
    st.header("Comandos")
    if st.button("🚀 ATUALIZAR MERCADO", use_container_width=True):
        with st.spinner("Lendo fluxo institucional..."):
            st.session_state.dados = {
                "EUR": cot.get(),
                "CLS": cls.get(),
                "BLOCK": block.get(),
                "BTC": btc_top.get()
            }
            st.session_state.analise = decide(st.session_state.dados)
    
    st.divider()
    if st.session_state.analise:
        if st.button("📤 POSTAR NO REDDIT", use_container_width=True):
            res = poster.post(st.session_state.dados, st.session_state.analise)
            st.success(res)

# --- VISUALIZAÇÃO PRINCIPAL ---
if st.session_state.analise:
    # 1. Painel de Veredito (O "Velocímetro" em texto)
    st.subheader("🎯 Veredito do Algoritmo")
    
    # Define a cor do alerta
    status = st.session_state.analise
    if "COMPRA" in status or "Alta" in status:
        st.success(f"### {status}")
    elif "VENDA" in status or "Baixa" in status:
        st.error(f"### {status}")
    else:
        st.warning(f"### {status}")

    st.divider()

    # 2. Grid de Dados (Sem chaves { }!)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**🇪🇺 EURO (COT)**")
        # Tradução simples na tela
        sig = st.session_state.dados["EUR"]["signal"].upper()
        sig_pt = "COMPRA" if "BUY" in sig else "VENDA" if "SELL" in sig else "NEUTRO"
        st.write(f"Sinal: **{sig_pt}**")
        st.write(f"Força: `{st.session_state.dados['EUR']['strength']}/3`")
        st.markdown('</div>', unsafe_allow_html=True)


    with col2:
        st.markdown('<div class="metric-card" style="border-left-color: #28a745;">', unsafe_allow_html=True)
        st.markdown("**📊 FLUXO CME (Blocks)**")
        blk = st.session_state.dados["BLOCK"]["block"].upper()
        st.write(f"Ordens: **{blk}**")
        st.write(f"Volume: `Institucional`")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card" style="border-left-color: #ffc107;">', unsafe_allow_html=True)
        st.markdown("**₿ BITCOIN RISK**")
        risco = st.session_state.dados["BTC"]["top"].upper()
        emoji = "⚠️" if risco == "RISK" else "✅"
        st.write(f"Status: **{risco} {emoji}**")
        st.write("Métrica: `Top Cycle`")
        st.markdown('</div>', unsafe_allow_html=True)

    # Botão para os nerds que ainda querem ver o JSON
    with st.expander("🔍 Ver Logs Técnicos (JSON)"):
        st.json(st.session_state.dados)

else:
    st.info("Clique no botão 'Atualizar Mercado' na lateral para começar.")
    
