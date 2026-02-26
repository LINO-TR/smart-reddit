import praw, datetime as dt, os

def post(details, call):
    try:
        # Separa o Título Curto da Estratégia Longa
        veredito_curto, estrategia_completa = call
        
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT"),
            client_secret=os.getenv("REDDIT_SECRET"),
            user_agent="smart-signal by u/seuuser",
            username=os.getenv("REDDIT_USER"),
            password=os.getenv("REDDIT_PASS"))
        
        sub = os.getenv("REDDIT_SUB")
        
        # Título limpo: "25/02 | VIÉS DE ALTA"
        title = f"{dt.date.today():%d/%m} | {veredito_curto}"
        
        # Corpo do post organizado
        body = f"""
## 💡 Estratégia do Dia:
{estrategia_completa}

---
### 📊 Dados Analisados:
* **EURO:** {details['EUR']['signal']}
* **FLUXO:** {details['BLOCK']['block']}
* **BTC:** {details['BTC']['top']}

*Gerado automaticamente pelo Smart Money Intelligence*
        """
        
        reddit.subreddit(sub).submit(title=title, selftext=body)
        return "✅ Postado com sucesso no Reddit!"
    except Exception as e:
        return f"❌ Erro ao postar: {e}"
        
