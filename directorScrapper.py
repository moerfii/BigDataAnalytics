import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director"

r = requests.get(link)

soup = BeautifulSoup(r.text)
soup
with open("debug.html","w+") as f:
    f.write(r.text)
tables1 = soup.find_all("table",{"class":"wikitable unsortable"})
tables2 = soup.find_all("table",{"class":"wikitable sortable"})

len(tables1)
len(tables2)
tables = tables1 + tables2
table = tables[0]
directors = []
for table in tables:
    tbody = table.find("tbody")
    trows = tbody.find_all("tr")
    row = trows[1]
    row
    for row in trows:
        td = row.find("td")
        if td:
            directors.append(td.find("a").text)
