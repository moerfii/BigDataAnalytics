# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:34:02 2021

@author: Flo
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
URL_START = "https://www.boxofficemojo.com/title/"
URL_END = "/credits/"

def scrapeData(tconst):
    #print(f"tconst: {tconst}")
    r = requests.get(URL_START + tconst + URL_END)
    soup = BeautifulSoup(r.text)
    boxOfficeTable = soup.find("div",{'class':"a-section a-spacing-none mojo-performance-summary-table"})
    try:
        rows = boxOfficeTable.find_all("div",{'class':'a-section a-spacing-none'})
    except AttributeError:
        return [tconst,np.nan,np.nan,np.nan]
    l = [tconst]
    for row in rows:
        span = row.find("span",{"class":"money"})
        if not span:
            l.append(np.nan)
        else:
            l.append(span.text.replace('$',"").replace(',',""))
    return l


if __name__=="__main__":

    tconsts = pd.read_csv("tconsts.csv")
    
    #prev_i=1000
    prev_i=100
    s = time.time()
    for i in range(prev_i,len(tconsts)):
        #save every 1000 movies
        if i%100==0:
            if i==prev_i:
                df = pd.DataFrame(columns=["tconst","domestic","international","worldwide"])
            else:
                df.to_csv("boxOffice.csv",mode="a+",sep=",",index=False,header=False)
                df = pd.DataFrame(columns=["tconst","domestic","international","worldwide"])
        print(i)
        tconst = tconsts.at[i,"tconst"]
        data = scrapeData(tconst)
        df=df.append(pd.Series({
            "tconst":data[0],
            "domestic":data[1],
            "international":data[2],
            "worldwide":data[3]})
            ,ignore_index=True
        )
    print(time.time()-s)
