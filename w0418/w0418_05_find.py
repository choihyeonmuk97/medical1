import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# find: 태그 정보를 찾는 함수
# 클래스로 찾는 방법
# print(soup.find(attrs={"class":"box_type_l"}))
# print(soup.find("tr",{"class":"type1"})) 가능
print(soup.find("tr",attrs={"class":"type1"}))
type_tr = soup.find("tr",{"class":"type1"})
print(type_tr.th) # 첫번째 만나는 태그를 출력
print(type_tr.find_all("th")) # 모든 태그를 출력 
ths = type_tr.find_all("th")

for th in ths:
    print("제목 :",th.text)