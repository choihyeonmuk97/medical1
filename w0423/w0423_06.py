import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 서울, 인천, 경기 인구를 웹스크래핑
# 서울 인구, 인천 인구, 경기 인구 -> 합계 : 인구 출력

browser = webdriver.Chrome()
url = 'https://jumin.mois.go.kr/ageStatMonth.do'

browser.get(url) # 브라우저 페이지 열기
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')

# url = 'https://jumin.mois.go.kr/ageStatMonth.do'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,'lxml')

h = soup.find('table',{'class':'tbl_type1'})
citys = h.find_all('tr')
print('도시 수 :',len(citys))

seoul = citys[4].find('td',{'class':"td_admin"}).text
s_h = citys[4].find_all('td')[2].text
print(seoul)
print('인구 :',s_h)
print('-'*50)

incheon = citys[7].find('td',{'class':'td_admin'}).text
i_h = citys[7].find_all('td')[2].text
print(incheon)
print('인구 :',i_h)
print('-'*50)

ggd = citys[12].find('td',{'class':'td_admin'}).text
g_h = citys[12].find_all('td')[2].text
print(ggd)
print('인구 :',g_h)
print('-'*50)

nums = int(s_h.replace(',',''))
numi = int(i_h.replace(',',''))
numg = int(g_h.replace(',',''))
print('합계 인구 :','{:,}'.format(nums+numi+numg))




