import yfinance as ticker

def get():
    try:
        # Puxa as últimas 24 horas com velas de 1 hora
        data = ticker.download("BTC-USD", period="2d", interval="1h")
        
        if len(data) < 2:
            return {"top": "NEUTRO", "risk_level": "MÉDIO"}

        # Pega o preço de agora e o preço de 4 horas atrás
        preco_atual = data['Close'].iloc[-1]
        preco_4h = data['Close'].iloc[-4] if len(data) >= 4 else data['Close'].iloc[0]
        
        # ANALISADOR DE PRESSÃO:
        # Se o preço subiu nas últimas 4h = Pressão de Compra
        if preco_atual > preco_4h:
            return {"top": "SAUDÁVEL", "risk_level": "BAIXO"}
        # Se o preço caiu nas últimas 4h = Pressão de Venda
        else:
            return {"top": "RISCO", "risk_level": "ALTO"}
            
    except Exception:
        # Se tudo falhar, ele assume o último estado seguro
        return {"top": "ESTÁVEL", "risk_level": "MÉDIO"}
        
