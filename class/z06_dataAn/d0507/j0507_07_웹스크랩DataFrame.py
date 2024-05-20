import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}


browser =  webdriver.Chrome()


#year title viewer rating
m_dict = {}
y_list = []
t_list = []
v_list = []
r_list = []

for year in range(2019,2024):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    soup = BeautifulSoup(browser.page_source,'lxml')
    time.sleep(2)
    
    print('연도 :',year)
    y_list.append(year)
    movie_list = soup.find('div',{'class':'pdt2'})
    # print(movie_list)
    
    title = movie_list.find('strong',{'class':'tit-g clamp-g'}).text.strip()
    t_list.append(title)
    print('제목 :',title)
    
    viewer = movie_list.find('p',{'class':'conts-desc clamp-g'}).text.strip()
    viewer = int(viewer[3:-2].replace(',',''))
    v_list.append(viewer)
    print('관객 수 :',viewer)
    
    elem = browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[2]/div[1]/c-title/strong/a')
    elem.click()
    time.sleep(2)
    rating = browser.find_element(By.CLASS_NAME,'gem-star-point').text
    rating = float(rating[2:-3])
    # d_rating = soup.find('span',{'class':'gem-star-point'})
    # raiting = d_rating.find('span',{'class':'ico-pmp'}).nextSibling.strip() !!
    r_list.append(rating)
    print('평점 :',rating)
    
    print('-'*60)
    
m_dict['year']=y_list
m_dict['title']=t_list
m_dict['viewer']=v_list
m_dict['rating']=r_list
print(m_dict)

df = pd.DataFrame(m_dict)
print(df)