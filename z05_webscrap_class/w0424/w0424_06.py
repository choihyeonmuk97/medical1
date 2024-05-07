import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By # 요소선택
from selenium.webdriver.common.keys import Keys # 키워드 입력
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

url = 'https://www.naver.com'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem = browser.find_element(By.XPATH,'//*[@id="query"]') # 엔터창 선택
elem.send_keys('네이버 항공권')
elem.send_keys(Keys.ENTER) # 엔터

elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a') # 항공권 홈페이지 클릭
elem.click()

# 새 창 이동
browser.switch_to.window(browser.window_handles[1])

elem = browser.find_element(By.XPATH,'/html/body/div/div/main/div[4]/div/div/div[2]/div[1]/button[1]') # 출발지 버튼 클릭
elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/button[1]') # 국내 선택
# elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/div/button[3]') # 김포 선택
# elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]') # 도착지 버튼 클릭
# elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/button[1]') # 국내 선택
# elem.click()

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/section/section/div/button[2]') # 제주 선택
# elem.click()

time.sleep(100)