import random

def get():
    # Simulando leitura de fluxo CLS (Bancos)
    # Em uma versão avançada, aqui conectaríamos com APIs de liquidez
    sentimento = random.choice(["bullish", "bearish", "neutral"])
    return {"sentiment": sentimento, "volume": "high"}
  
