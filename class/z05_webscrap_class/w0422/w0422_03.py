import requests
from bs4 import BeautifulSoup

# url="https://browse.auction.co.kr/search?keyword=%ec%97%ac%ed%96%89&itemno=&nickname=&frm=ho[…]&arraycategory=&encKeyword=%ec%97%ac%ed%96%89&f=c:24010000"
url="https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# with open('auction.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

# print(soup.find("div",{"id":"section--inner_content_body_container"}))
section = soup.find("div",{"id":"section--inner_content_body_container"})
print('-'*200)
# print(section.find('div',{'class':'section--itemcard'}))
# 복수개 찾기
itemcards = section.find_all("div",{"class":"section--itemcard_info"})
print('개수 :',len(itemcards))

for i,itemcard in enumerate(itemcards[0:10]):
    print('[',i+1,'번째 ]')
    print('제목 :',itemcards[i].find("span",{"class":"text--title"}).text)
    # replace() : 특정부분 문자열을 다른 문자열로 대체
    price = int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(',',''))
    print('금액 :','{:,}'.format(price)) 
    
    # 후기 평점, 구매 건수
    list_score = itemcard.find("ul",{"class":"list--score"})
    lis = list_score.find_all('li')
    print('li 개수 :',len(lis))
    
    if len(lis) == 0:
        print('평점, 구매 건수 : 없음')
    elif len(lis) == 1:
        buycnt = int(lis[0].find('span',{'class','text--buycnt'}).text[3:])
        print('구매건수 :', buycnt)
    else: #li == 3
        for_a11y = float(lis[0].find('span',{'class','for-a11y'}).text[5:-1])
        print('후기 평점 :',for_a11y)
        buycnt = int(lis[2].find('span',{'class','text--buycnt'}).text[3:])
        print('구매 건수 :',buycnt)
    
    
    

    print('-'*200)

