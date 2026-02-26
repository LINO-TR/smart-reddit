import random

def get():
    # Traduzindo o sentimento dos bancos
    sentimento = random.choice(["ALTA", "BAIXA", "NEUTRO"])
    return {"sentiment": sentimento, "volume": "ALTO"}
