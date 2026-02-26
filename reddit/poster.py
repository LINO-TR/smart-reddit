import praw, datetime as dt, os
def post(details, call):
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT"),
            client_secret=os.getenv("REDDIT_SECRET"),
            user_agent="smart-signal by u/seuuser",
            username=os.getenv("REDDIT_USER"),
            password=os.getenv("REDDIT_PASS"))
        
        sub = os.getenv("REDDIT_SUB")
        title = f"{dt.date.today():%d/%m} | {call}"
        body = f"Resumo: {details}"
        
        reddit.subreddit(sub).submit(title=title, selftext=body)
        return "Postado com sucesso!"
    except Exception as e:
        return f"Erro ao postar: {e}"
      
