import re
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

names = soup.find_all("div" , attrs={"class" : "col_inner"})

for name in names:
    datas = name.find("ul").find_all("li")
    day = name.find("span").get_text()
    print("<<<<{}>>>>" .format(day))
    for data in datas:
        web_name = data.find("a" , attrs={"class" : "title"}).get_text()
        link = data.a["href"]
        print(web_name)
        print("https://comic.naver.com" + link)