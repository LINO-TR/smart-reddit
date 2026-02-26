import yfinance as ticker

def get():
    try:
        data = ticker.download("EURUSD=X", period="2d", interval="1h")
        if len(data) < 4: return {"sentiment": "NEUTRO", "volume": "BAIXO"}
        
        atual = data['Close'].iloc[-1]
        referencia = data['Close'].iloc[-4] # 4 horas atrás
        
        if atual > referencia:
            return {"sentiment": "ALTA", "volume": "ALTO"}
        elif atual < referencia:
            return {"sentiment": "BAIXA", "volume": "ALTO"}
        else:
            return {"sentiment": "NEUTRO", "volume": "NORMAL"}
    except:
        return {"sentiment": "NEUTRO", "volume": "BAIXO"}
        
