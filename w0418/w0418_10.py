import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
t_table = soup.find("table",{"class":"type_5"})
trs = t_table.find_all("tr")
# print(trs)

for i in range(2,15):
    td_list = trs[i].find_all("td")
    if len(td_list) == 1: # td_list의 길이가 1이면 넘어간다 
        continue
    print('-'*20)
    for j in td_list:
        print(j.text.strip())
    