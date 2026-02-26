import random

def get():
    # Traduzindo as ordens de bloco
    direcao = random.choice(["COMPRA", "VENDA", "NENHUMA"])
    return {"block": direcao, "intensity": "FORTE"}
