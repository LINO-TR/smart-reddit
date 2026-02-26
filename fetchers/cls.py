import yfinance as ticker

def get():
    try:
        data = ticker.download("EURUSD=X", period="2d", interval="15m")
        # Compara preço atual com o anterior
        preco_atual = data['Close'].iloc[-1]
        preco_anterior = data['Close'].iloc[-2]
        
        if preco_atual > preco_anterior:
            return {"sentiment": "ALTA", "volume": "ALTO"}
        else:
            return {"sentiment": "BAIXA", "volume": "NORMAL"}
    except:
        return {"sentiment": "NEUTRO", "volume": "BAIXO"}
        
