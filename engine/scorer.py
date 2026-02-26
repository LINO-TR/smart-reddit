def get_strategy(score, cot_sig, flux_sig):
    # Matriz de Decisão: Resumos automáticos para o Reddit e App
    if score >= 4:
        return "🔥 CONFLUÊNCIA MÁXIMA: Institucional (COT) e Bancos (CME) alinhados na compra. Procure entradas em pullbacks. Alvos em zonas de liquidez acima."
    elif score <= -4:
        return "🚨 ALINHAMENTO DE QUEDA: Tubarões e Bancos vendendo forte. Cenário ideal para buscar vendas em regiões de resistência. Evite compras."
    elif cot_sig == "COMPRA" and flux_sig == "VENDA":
        return "⚠️ DIVERGÊNCIA: O institucional longo está comprado, mas os bancos estão realizando lucro agora. Espere o preço cair para comprar mais barato."
    elif cot_sig == "VENDA" and flux_sig == "COMPRA":
        return "⚠️ ARMADILHA: O institucional maior vende, mas o fluxo de curto prazo sobe. Pode ser um rali falso para capturar liquidez e voltar a cair."
    elif score >= 2:
        return "✅ VIÉS DE ALTA: Existe pressão compradora, mas falta confirmação de um dos lados. Opere com lotes menores."
    elif score <= -2:
        return "⚠️ VIÉS DE BAIXA: Pressão vendedora detectada, mas sem alinhamento total. Atenção aos suportes próximos."
    else:
        return "☕ MODO CAFÉ: Mercado lateral ou sem direção clara. O Smart Money está fora do jogo agora. Preserve seu capital."

def decide(details):
    score = 0
    eur = details["EUR"]["signal"].upper()
    cot_sig = "COMPRA" if "BUY" in eur else "VENDA" if "SELL" in eur else "NEUTRO"
    
    if cot_sig == "COMPRA": score += 3
    elif cot_sig == "VENDA": score -= 3
    
    flux_sig = details["BLOCK"]["block"].upper() # COMPRA, VENDA ou NENHUMA
    if flux_sig == "COMPRA": score += 2
    elif flux_sig == "VENDA": score -= 2

    # Retorna o Veredito e a Estratégia
    if score >= 4: veredito = "HORA DE COMPRAR"
    elif score <= -4: veredito = "HORA DE VENDER"
    elif score >= 2: veredito = "VIÉS DE ALTA"
    elif score <= -2: veredito = "VIÉS DE BAIXA"
    else: veredito = "NÃO FAÇA NADA"
    
    estrategia = get_strategy(score, cot_sig, flux_sig)
    return veredito, estrategia
    
