import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By # 요소선택
from selenium.webdriver.common.keys import Keys # 키워드 입력
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

url = 'https://www.naver.com '

browser = webdriver.Chrome()
browser.maximize_window() # 최대화
browser.get(url)

elem = browser.find_element(By.ID,'query')
elem.send_keys('시가총액')
elem.send_keys(Keys.ENTER) # input 박스에서 enter키 입력

# 시가총액 더보기 클릭
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/div[2]/a')
elem.click()

time.sleep(100)

