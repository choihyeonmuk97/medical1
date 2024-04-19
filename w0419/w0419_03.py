import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# print(len(soup.find("ul",{"class","search-product-list"}).find_all("li")))
ul_search = soup.find("ul",{"class","search-product-list"})

# 모든 상품 검색
lis = ul_search.find_all('li')
# print("리스트 개수 :",len(lis))

count = 0
for i,li in enumerate(lis[0:20]):
    print("[",i+1,"번째 상품 ]")
    # 광고 상품 제외 if
    if 'search-product__ad-badge' in li["class"]:
        continue
    
    # 평점이 5.0 이상만 나오게 하는 if
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    
    # 평가 인원이 200명 이상만 나오게 하는 if
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200:
        continue
    
    print(li["class"])
    print("제목 :",li.find("div",{"class":"name"}).text.strip())
    print("가격 :",li.find("strong",{"class":"price-value"}).text)
    print("평점 :",li.find("em",{"class":"rating"}).text)
    print("평가 인원 수 :",li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print('-'*200)


