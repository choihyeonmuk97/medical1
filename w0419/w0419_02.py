import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

'''
no = soup.find("p",{"class","no1"}).text
print("번호 :",no)

txt = soup.find("div",{"class","best-list"}).find("a",{"class","itemname"}).text
print("내용 :",txt)

price = soup.find("div",{"class","best-list"}).find("div",{"class","s-price"}).text
print("가격 :",price)
'''

best_div = soup.find("div",{"class","best-list"})
# li01= best_div.find("li")
# print(li01.p.text)
# print(li01.find("a",{"class","itemname"}).text)
# print(li01.find("div",{"class":"s-price"}).strong.span.text)    ->1개만 출력 (첫번째만 나온다)

lis = best_div.find_all("li")
print("상품 개수 :",len(lis))

for li in lis[0:4]:
    print("순위 :",li.p.text)
    print("제목 :",li.find("a",{"class","itemname"}).text)
    print("가격 :",li.find("div",{"class":"s-price"}).strong.span.text)
    print('-'*10)
