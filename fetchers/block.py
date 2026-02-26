import random

def get():
    # Simulando ordens de bloco da CME
    direcao = random.choice(["buy", "sell", "none"])
    return {"block": direcao, "intensity": "strong"}

