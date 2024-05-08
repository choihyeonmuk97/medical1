import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(20)

soup = BeautifulSoup(browser.page_source,'lxml')

''' 파일 저장
with open('melon.html','w',encoding='utf8')as f:
    f.write(soup.prettify) 
    파일 불러오기
with open('melon.html','r',encoding='utf8')as f:
    soup = BeautifulSoup(f,'lxml')
'''

songs = soup.find_all('tr',{'id':'lst50'})
print(len(songs))

for s in songs:
    rank = s.find('span',{'class':'rank'}).text
    print('순위 :',rank)

    s_rank = s.find("span",{"class":"rank_wrap"})
    v_rank = s.find("span",{"class":"rank_wrap"})['title']
    print(v_rank)
    if v_rank =="순위 동일":
        v_rank = 0
    elif v_rank.find('단계 하락') != -1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else:
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)        
    print("순위변동 : {:+d}".format(v_rank))  # +부호 넣기

    img = s.find('img')['src']
    print('이미지 링크 :',img)

    title1 = s.find('div',{'class':'ellipsis rank01'})
    title = title1.find('a').text
    print('제목 :',title)

    singer1 = s.find('div',{'class':'ellipsis rank02'})
    singer = singer1.find('a').text
    print('가수 :',singer)

    r_likeNum = s.find("button",{"class":"button_etc like"})
    likeNum = r_likeNum.find("span",{"class":"none"}).nextSibling.strip()
    likeNum = likeNum.replace(',','').strip()
    print('좋아요 수 :',likeNum)
    print('-'*150)

    sql =f'''insert into melon values (melon_seq.nextval,{rank},{v_rank},'{img}','{title}','{singer}',{likeNum})'''
    cursor.execute(sql)
    
cursor.execute('commit')   
cursor.close()
conn.close()   







# 1개만 뽑아보기
# rank = songs[0].find('span',{'class':'rank'}).text
# print('순위 :',rank)

# s_rank = songs[0].find("span",{"class":"rank_wrap"})
# v_rank = songs[0].find("span",{"class":"rank_wrap"})['title']
# print(v_rank)
# if v_rank =="순위 동일":
#     v_rank = 0
# elif v_rank.find('단계 하락') != -1:
#     v_rank = s_rank.find("span",{"class":"down"}).text
#     v_rank = int(v_rank)*-1
# else:
#     v_rank = s_rank.find("span",{"class":"up"}).text
#     v_rank = int(v_rank)        
# print("순위변동 : {:+d}".format(v_rank))  # +부호 넣기

# img = songs[0].find('img')['src']
# print('이미지 링크 :',img)

# title1 = songs[0].find('div',{'class':'ellipsis rank01'})
# title = title1.find('a').text
# print('제목 :',title)

# singer1 = songs[0].find('div',{'class':'ellipsis rank02'})
# singer = singer1.find('a').text
# print('가수 :',singer)

# r_likeNum = songs[0].find("button",{"class":"button_etc like"})
# likeNum = r_likeNum.find("span",{"class":"none"}).nextSibling.strip()
# likeNum = likeNum.replace(',','').strip()
# print('좋아요 수 :',likeNum)

# 셀레니움
# rank = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[2]/div/span[1]').text
# print(rank) # 순위

# img = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[4]/div/a/img').get_attribute('src')
# print(img)

# title = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
# print(title)

# singer = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[6]/div/div/div[2]/a').text
# print(singer)

# likeNum = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[8]/div/button/span[2]').text
# likeNum = likeNum.replace(',','')
# print(likeNum)

# print('-'*150)