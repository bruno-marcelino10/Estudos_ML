import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from functools import reduce

class Serie:

    def get_yahoo(self, ativo, startdate):
        data = yf.download(ativo, start = startdate)
        target = data["Adj Close"].pct_change().dropna()
        target.columns = ["FIND11"]
        return target

    def get_BCB(self, codigo_serie):
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json"
        df = pd.read_json(url)
        df["data"] = pd.to_datetime(df["data"], dayfirst = True)
        df.set_index("data", inplace = True)
        df["valor"] = df["valor"].astype(float)
        return df

    def get_pib(self, url):
        pib = pd.read_html(url)[2]
        pib.columns = pib.loc[0]
        pib.drop(0, axis = 0, inplace = True)
        pib.reset_index(drop = True, inplace = True)

        datas, pibs = [], []
        for i in range(len(pib)):
            data_iter = pib.iloc[i, 0].replace(".", "")
            pib_iter = pib.iloc[i, 1].replace(".", "")              
            pib_iter = float(pib_iter.replace(",", ""))/10000    
            datas.append(data_iter)
            pibs.append(pib_iter)

        pib["Data"] = pd.to_datetime(datas, format = "%Y%m")
        pib["PIB"] = pibs
        pib.set_index("Data", inplace = True)
        return pib
    
    def merge(self, dfs):
        df = reduce(lambda left, right: left.join(right, how = "inner"), dfs)
        return df
        