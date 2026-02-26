def decide(details):
    score = 0
    
    # Peso 1: Euro (COT)
    eur = details["EUR"]["signal"].upper()
    if "BUY" in eur or "COMPRA" in eur: score += 3
    elif "SELL" in eur or "VENDA" in eur: score -= 3
    
    # Peso 2: Fluxo de Bancos (CLS)
    cls_sent = details["CLS"]["sentiment"]
    if cls_sent == "ALTA": score += 2
    elif cls_sent == "BAIXA": score -= 2
    
    # Peso 3: Ordens de Bloco (CME)
    blk = details["BLOCK"]["block"]
    if blk == "COMPRA": score += 2
    elif blk == "VENDA": score -= 2
    
    # Veredito Final (Mamão com açúcar)
    if score >= 4:
        return "🔥 HORA DE COMPRAR"
    elif score <= -4:
        return "🚨 HORA DE VENDER"
    elif score >= 2:
        return "✅ VIÉS DE ALTA (CUIDADO)"
    elif score <= -2:
        return "⚠️ VIÉS DE BAIXA (CUIDADO)"
    else:
        return "☕ NÃO FAÇA NADA"
