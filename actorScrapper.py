import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.imdb.com/list/ls050274118/"

r = requests.get(link)
soup = BeautifulSoup(r.text)

divs = soup.find_all("div",{"class":"lister-item mode-detail"})
l = []
div = divs[0]
for div in divs:
    h3 = div.find("h3")
    name = h3.find("a").text
    l.append(name.strip())

df = pd.DataFrame(columns=["top_actors"])
df['top_actors'] = l
df.to_csv("data/top_actors.csv")
