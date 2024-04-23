import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = 'https://finance.naver.com'

browser.get(url) # 브라우저 페이지 열기
time.sleep(3)
# elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a') # 네이버 메인에서 증권 클릭
# elem.click()
# time.sleep(3)

elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a') # 네이버 증권에서 인기종목 더보기 클릭
elem.click()
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')
print(soup.prettify())
with open('stock.html','w',encoding='utf8') as f:
    f.write(soup.prettify())
time.sleep(100)
