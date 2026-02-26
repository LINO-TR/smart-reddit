import yfinance as ticker

def get():
    try:
        data = ticker.download("EURUSD=X", period="1d", interval="15m")
        # Lógica simples de momentum (substitui o sorteio)
        mudanca = data['Close'].diff().iloc[-1]
        
        if mudanca > 0:
            return {"block": "COMPRA", "intensity": "FORTE"}
        elif mudanca < 0:
            return {"block": "VENDA", "intensity": "FORTE"}
        else:
            return {"block": "NENHUMA", "intensity": "FRACA"}
    except:
        return {"block": "NENHUMA", "intensity": "DESCONHECIDA"}
        
