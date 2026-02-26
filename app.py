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
    # Separando os dois valores que vêm do scorer.py
    veredito, estrategia = st.session_state.analise 
    
    st.subheader("🎯 Veredito do Algoritmo")
    
    # Exibe apenas o Título do Veredito com cor
    if "COMPRAR" in veredito or "ALTA" in veredito:
        st.success(f"### {veredito}")
    elif "VENDER" in veredito or "BAIXA" in veredito:
        st.error(f"### {veredito}")
    else:
        st.warning(f"### {veredito}")
    
    # Exibe a Estratégia em um quadro separado e limpo
    st.info(f"**💡 ESTRATÉGIA RECOMENDADA:**\n\n{estrategia}")

    st.divider()
    # ... (restante das colunas com as barras que você já tem)

    # 2. Grid de Dados (Sem chaves { }!)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**🇪🇺 EURO (COT)**")
        sig = st.session_state.dados["EUR"]["signal"].upper()
        sig_pt = "COMPRA" if "BUY" in sig else "VENDA" if "SELL" in sig else "NEUTRO"
        
        # CÁLCULO DA BARRA: Força 0/3 vira 0.1, 1/3 vira 0.33, 3/3 vira 1.0
        forca_cot = st.session_state.dados["EUR"]["strength"] / 3
        st.progress(max(forca_cot, 0.05)) # Garante que apareça pelo menos um risquinho
        
        st.write(f"Sinal: **{sig_pt}** ({st.session_state.dados['EUR']['strength']}/3)")

    with col2:
        st.markdown("**📊 FLUXO CME**")
        blk = st.session_state.dados["BLOCK"]["block"].upper()
        
        # CÁLCULO DA BARRA: Se for NENHUMA fica 0.1, se tiver direção enche 1.0
        forca_cme = 1.0 if blk != "NENHUMA" else 0.1
        st.progress(forca_cme)
        
        st.write(f"Ordens: **{blk}**")

    with col3:
        st.markdown("**₿ BITCOIN**")
        status_btc = st.session_state.dados["BTC"]["top"]
        
        # CÁLCULO DA BARRA: SAUDÁVEL fica em 0.3, qualquer outro (Risco) enche 1.0
        forca_btc = 0.3 if status_btc == "SAUDÁVEL" else 1.0
        st.progress(forca_btc)
        
        st.write(f"Status: **{status_btc}** {'✅' if status_btc == 'SAUDÁVEL' else '⚠️'}")


    # Botão para os nerds que ainda querem ver o JSON
    with st.expander("🔍 Ver Logs Técnicos (JSON)"):
        st.json(st.session_state.dados)
else:
    st.info("Clique no botão 'Atualizar Mercado' na lateral para começar.")
    
