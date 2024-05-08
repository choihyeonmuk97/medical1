import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser =  webdriver.Chrome()

    # with open('yeogi.html','w',encoding='utf8') as f:
    #     f.write(soup.prettify())  # 파일 쓰기

    # with open('yeogi.html','r',encoding='utf8') as f:
    #     soup = BeautifulSoup(f,'lxml') # 파일에서 불러오기

# for i in range(5):
#     url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page={i+1}"
#     browser.get(url)
#     time.sleep(2)

#     soup = BeautifulSoup(browser.page_source,'lxml')


#     titles = soup.find_all('a',{'class':'gc-thumbnail-type-seller-card css-wels0m'})
#     # print(titles)
#     print('개수 :',len(titles))
#     title = titles[0].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
#     print('제목 :',title.text)
    
#     print('-'*50)



url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1"
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,'lxml')


titles = soup.find_all('a',{'class':'gc-thumbnail-type-seller-card css-wels0m'})
# print(titles)
print('개수 :',len(titles))
title = titles[1].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
print('제목 :',title.text)
place = titles[0].find('div',{'class':'css-19li9i9'})
print(place.text)

print('-'*50)





for i in titles:
    title = i.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
    print('제목 :',title.text)
    place = i.find('div',{'class':'css-19li9i9'})
    print('장소 :',place.text)
    star = i.find('span',{'class':'css-9ml4lz'})
    print('평점 :',star.text)
    stars = i.find('span',{'class':'css-oj6onp'})
    print('평가자 수 :',stars.text)
    
    try: # img src 있는데 안나옴..
        img = i.find('img')['src']
        # print(img)
        # image = i.find('img',{'class':'thumbnail-image desktop:hover:bg-backgroundOverlayDarkInactive'})["src"]
        print('이미지링크 :',img)
    except:
        print('링크를 찾을 수 없습니다.')
        pass
    
    price = i.find('div',{'class':'css-yeouz0'}).text
    if price == '':
        print('가격 : 없음')
    else:
        print('가격 :',price)
        pass
    
    print('-'*50)





''' -> xpath
elem = browser.find_element(By.XPATH,'//h3[text()="★당일특가★ 하이원리조트 마운틴콘도"]')
print(elem.text)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[2]/span[1]')
print(elem.text)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[3]/div/span')
print(elem.text)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[3]/span')
print(elem.text)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[1]/div[1]/img').get_attribute('src')
print(elem)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[2]/div/div/div/div[2]')
print(elem.text)
'''

# conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
# cursor = conn.cursor()

# sql = ""

# conn.close() 