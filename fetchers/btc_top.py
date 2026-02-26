import requests

def get():
    try:
        # Lógica de simulação de risco para o exemplo
        return {"top": "SAUDÁVEL", "risk_level": "BAIXO"}
    except:
        return {"top": "DESCONHECIDO", "risk_level": "MÉDIO"}
