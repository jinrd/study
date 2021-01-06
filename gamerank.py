import requests
import re
from bs4 import BeautifulSoup

url = "https://www.gamemeca.com/ranking.php"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

rows = soup.find_all("div" ,attrs = {"class" : "game-name"})

nam = []
com = []
companys = soup.find_all("span" , attrs = {"class" : "company"})
for idx,row in enumerate(rows):
    nam.append(row.get_text())

for idx, company in enumerate(companys):
    com.append(company.get_text())
for i in range(len(nam)):
    print(i+1,"위 " ,nam[i] , com[i])


