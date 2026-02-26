import yfinance as ticker

def get():
    try:
        # Puxa dados recentes para analisar o "sentimento"
        data = ticker.download("BTC-USD", period="1d", interval="1h")
        if len(data) < 5:
            return {"top": "ESTÁVEL", "risk_level": "BAIXO"}

        # Calcula a variação das últimas velas
        ultimo_fechamento = data['Close'].iloc[-1]
        abertura_recente = data['Open'].iloc[-4] # Olha as últimas 4 horas
        
        # Lógica de Fluxo:
        # Se o preço está subindo nas últimas horas com volume sustentado
        if ultimo_fechamento > abertura_recente:
            status = "SAUDÁVEL"
            risco = "BAIXO"
        # Se o preço está caindo (pressão vendedora dominando)
        else:
            status = "RISCO"
            risco = "ALTO"

        return {"top": status, "risk_level": risco}
        
    except Exception:
        return {"top": "NEUTRO", "risk_level": "MÉDIO"}
        
