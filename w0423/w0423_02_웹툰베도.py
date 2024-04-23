import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

browser = webdriver.Chrome()
browser.get('https://comic.naver.com/bestChallenge')

time.sleep(3) # 이거 없으면 none 계속나온다 -> 데이터를 받아올 시간을 줘야함
soup = BeautifulSoup(browser.page_source,'lxml')

# with open('webtoon2.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

li_list = soup.find('ul',{'class':'AsideList__content_list--FXDvm AsideList__challenge--HeKuU'})
lis = li_list.find_all('li',{'class':'AsideList__item--i30ly'})
# print(lis)

for li in lis:
    rank = li.find('strong',{'class':'AsideList__ranking--sNPZy'}).text
    title = li.find('span',{'class':'text'}).text
    aut = li.find('a',{'class':'ContentAuthor__author--CTAAP'}).text
    img_url = li.find('img',{'class':'Poster__image--d9XTI'})['src']
    print('순위 :',rank)
    print('제목 :',title)
    print('작가 :',aut)
    print('이미지 :',img_url)
    img_poster = requests.get(img_url,headers=headers)
    with open('webtoons_{}.jpeg'.format(rank),'wb')as f:
        f.write(img_poster.content) # 이미지 저장
    print('-'*150)
    




''' requests로 정보 가져오기
url = 'https://comic.naver.com/bestChallenge'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

with open('webtoon1.html','w',encoding='utf8') as f:
    f.write(soup.prettify())
'''


