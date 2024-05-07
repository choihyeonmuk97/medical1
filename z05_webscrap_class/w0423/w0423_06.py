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

h = soup.find('table',{'class':'tbl_type1'}) # tbody로 들어왔으면 더 쉬웠겠다 !!
citys = h.find_all('tr')
# print('tr 수 :',len(citys))

seoul = citys[4].find('td',{'class':"td_admin"}).text
s_h = citys[4].find_all('td')[2].text
print(seoul,'인구 :',s_h)

incheon = citys[7].find('td',{'class':'td_admin'}).text
i_h = citys[7].find_all('td')[2].text
print(incheon,'인구 :',i_h)

ggd = citys[12].find('td',{'class':'td_admin'}).text
g_h = citys[12].find_all('td')[2].text
print(ggd,'인구 :',g_h)

nums = int(s_h.replace(',',''))
numi = int(i_h.replace(',',''))
numg = int(g_h.replace(',',''))
print('합계 인구 :','{:,}'.format(nums+numi+numg))
print('-'*50)

'''--------------------------------셀레니움------------------------------------'''

seoul1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[2]').text
s_h1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[3]').text
incheon1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[2]').text
i_h1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[3]').text
ggd1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[2]').text
g_h1 = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[3]').text

sh1 = int(s_h1.replace(',',''))
ih1 = int(i_h1.replace(',',''))
gh1 = int(g_h1.replace(',',''))

print(seoul1,"인구 :",s_h1)
print(incheon1,"인구 :",i_h1)
print(ggd1,"인구 :",g_h1)
print('합계 인구 :','{:,}'.format(sh1+ih1+gh1))


