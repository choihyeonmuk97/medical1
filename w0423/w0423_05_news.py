import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# browser = webdriver.Chrome()
# url = 'https://news.naver.com/main/ranking/popularDay.naver'

# browser.get(url) # 브라우저 페이지 열기
# time.sleep(3)

# soup = BeautifulSoup(browser.page_source,'lxml')

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

officeCard = soup.find('div',{'class':'_officeCard _officeCard0'})
ranks = officeCard.find_all('div',{'class':'rankingnews_box'})

for rank in ranks:
    lis = rank.find_all('li')
    print('제목 :',lis[0].find("a",{"class":"list_title"}).text)
    print('-'*150)
    



''' 이건 섹션 하나짜리였음.. 전부 하는거였다..
n_list = soup.find('div',{'class':'rankingnews_box'}).text
# print(n_list)
ranks = n_list.find_all('em',{'class':'list_ranking_num'}).text
# print(ranks)
title = n_list.find_all("a",{"class":"list_title nclicks('RBP.rnknws')"}).text
# print(title)
image = n_list.find_all('a',{"class":"list_img nclicks('RBP.rnknws')"})["src"]
# print(image)
'''



