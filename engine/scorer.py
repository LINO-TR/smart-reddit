def decide(details):
    score = 0
    # Lógica simplificada e robusta
    if details["EUR"]["signal"] == "buy": score += 3
    if details["EUR"]["signal"] == "sell": score -= 3
    
    if score >= 2: return "CENÁRIO BOM PRA COMPRAR"
    if score <= -2: return "CENÁRIO BOM PRA VENDER"
    return "NEUTRO / FORA"
  
