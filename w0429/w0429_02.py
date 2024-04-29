import time
import requests
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

url = 'https://flight.naver.com'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)

# 실제구문 1개 가져오기 : browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
# 실제구문 여러개 가져오기 : browser.find_elements(By.XPATH,'//b[text()="15"]')

# 문자열과 일치할 때 선택 : '//i[text()="김포국제공항"]'
# 문자열이 포함되어 있을 때 선택 : '//i[contains(text(),"김포국제공항")]'
# id를 이용하여 선택 : '//i[@id="_next"]'
# class를 이용하여 선택 : '//i[@class="_next"]'

# 전체 문서 : //     -출발지 선택-
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()
time.sleep(1)

# 도착지 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 제주국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
time.sleep(1)
elem.click()
time.sleep(1)

# 가는날 버튼 선택
browser.find_element(By.XPATH,'//button[text()="가는 날"]').click() 
time.sleep(1)

#출발일자 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print('14일 개수 :',len(elem))
elem[1].click()
time.sleep(1)

# 도착일 선택
browser.find_element(By.XPATH,'//button[text()="오는 날"]').click()
time.sleep(1)

# 도착일자 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
print('15일 개수 :',len(elem))
elem[1].click()
time.sleep(1)

# 인원수 선택
browser.find_element(By.XPATH,'//button[contains(text(),"성인")]').click()
time.sleep(1)

# 1명 추가 선택
browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]').click()
time.sleep(1)

# 항공권 검색 클릭
for i in range(2): # 인원 수 창을 닫기 위해 두번 클릭
    browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
    time.sleep(1)

# 페이지가 이동하는데 걸리는 시간 대기 !! timesleep을 해도 된다
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)

# 스크롤 이동 
prev_height = browser.execute_script('return document.body.scrollHeight')
print('최초 높이 :',prev_height)
time.sleep(3)

# 스크롤이 끝까지 내려가기 위해 반복문 사용
while True:
    browser.execute_script("Window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 스크롤 높이 체크
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print('현재 높이 :',curr_height)

# 웹 스크래핑
# soup = BeautifulSoup(browser.page_source)
# with open('filght.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
    
input('Enter키를 입력하면 프로그램을 종료합니다.')
browser.quit()


time.sleep(100)
