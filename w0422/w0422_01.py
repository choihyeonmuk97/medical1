import requests
from bs4 import BeautifulSoup

# url="https://browse.auction.co.kr/search?keyword=%ec%97%ac%ed%96%89&itemno=&nickname=&frm=ho[…]&arraycategory=&encKeyword=%ec%97%ac%ed%96%89&f=c:24010000"
url="https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')








# with open ('auction1.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

# print(soup.find("div",{"class":"section--itemcard"}))

# title = (soup.find("span",{"class":"text--title"}).text)  찾기는 잘 찾았는데..
# print("제품명 :",title)

# price = (soup.find("strong",{"class":"text__price-seller"}).text)
# print("가격 :",price)

# print(soup.find("ll",{"class":"item awards"}))


