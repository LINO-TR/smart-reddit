import yfinance as ticker

def get():
    try:
        data = ticker.download("EURUSD=X", period="2d", interval="1h")
        if len(data) < 4: return {"block": "NENHUMA", "intensity": "FRACA"}
        
        atual = data['Close'].iloc[-1]
        referencia = data['Close'].iloc[-4]
        
        # Define se o bloco de ordens é de compra ou venda baseado na tendência de 4h
        if atual > referencia:
            return {"block": "COMPRA", "intensity": "FORTE"}
        elif atual < referencia:
            return {"block": "VENDA", "intensity": "FORTE"}
        else:
            return {"block": "NENHUMA", "intensity": "NEUTRA"}
    except:
        return {"block": "NENHUMA", "intensity": "DESCONHECIDA"}
        
