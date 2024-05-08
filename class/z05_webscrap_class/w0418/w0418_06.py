import requests
from bs4 import BeautifulSoup

url ="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

div = soup.find("div",{"class":"box_type_l"}) # 테이블 클래스로 찾아도 됨
tr_all = div.find_all("tr")

samjun = tr_all[2]
sam_td = samjun.find_all("td")

for i in range(len(sam_td)):
    print(sam_td[i].text.split())


