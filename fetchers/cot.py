import pandas as pd, requests, datetime as dt
def get():
    try:
        url = "https://cftc.gov/dea/newcot/f_disagg.txt"
        df  = pd.read_csv(url, sep=",", header=0, low_memory=False)
        eur = df[df["Market_and_Exchange_Names"].str.contains("EURO FX", na=False)].iloc[-1]
        longs = int(eur["Asset_Managers_Positions_Long_All"])
        shorts = int(eur["Asset_Managers_Positions_Short_All"])
        net = longs - shorts
        return {"pair":"EUR","signal":"buy" if net > 0 else "sell","strength":2}
    except:
        return {"pair":"EUR","signal":"neutral","strength":0}
      
