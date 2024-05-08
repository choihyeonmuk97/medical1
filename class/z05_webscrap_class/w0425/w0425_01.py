import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By # 요소선택
from selenium.webdriver.common.keys import Keys # 키워드 입력
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

url = 'https://www.naver.com'
url = 'https://flight.naver.com'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# elem = browser.find_element(By.NAME,"query") # 엔터창 선택
# elem.send_keys('네이버 항공권')
# elem.send_keys(Keys.ENTER) # 엔터

# time.sleep(2)

# elem = browser.find_element(By.CLASS_NAME,'link_name') # 항공권 홈페이지 클릭
# elem.click()

# # 새 창 이동
# browser.switch_to.window(browser.window_handles[1])
# time.sleep(2)

elem = browser.find_element(By.XPATH,'/html/body/div/div/main/div[4]/div/div/div[2]/div[1]/button[1]') # 출발지 버튼 클릭
elem.click()

time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM') # 국내 선택
elem.click()

time.sleep(2)

elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[2] # 김포 선택
elem.click()

time.sleep(2)
'''------------------------------------------------------------------------------------------------------------------------------------------'''
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]') # 도착지 버튼 클릭
elem.click()

time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM') # 국내 선택
elem.click()

time.sleep(2)

elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1] # 제주 선택
elem.click()

time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]') # 출발일정 클릭
elem.click()

time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/button/b') # 출발일자 선택
elem.click()

time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/button/b') # 도착일자 선택
elem.click()                            

time.sleep(2)

for i in range(2):
    elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]/button') # 인원 선택 (증가 안시켰음)
    elem.click() 

time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button') # 항공권 검색
elem.click() 

time.sleep(10)

for i in range(30):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


time.sleep(100)