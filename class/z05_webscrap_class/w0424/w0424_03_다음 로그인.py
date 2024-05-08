import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

url = 'https://www.daum.net/'
browser = webdriver.Chrome()

browser.get(url)
time.sleep(3)
# 로그인 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a')
elem.click()
time.sleep(random.randint(2,5))

# # 아이디 입력
# elem = browser.find_element(By.ID,'loginId--1')
# elem.send_keys('aaa')
# time.sleep(random.randint(2,5))

# # 비밀번호 입력
# elem = browser.find_element(By.ID,'password--2')
# elem.send_keys('1111')
# time.sleep(random.randint(2,5))

# jquery = $("#id").val() / js = document.getElementById("id").value
# input_js = ''.format('aaa','1111')

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("loginId--1").value="{id}"; \
            document.getElementById("password--2").value="{pw}"; \
            '.format(id='aaa',pw='1111')
# time.sleep(random.randint(2,5))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

# 로그인 버튼 클릭
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,'highlight')
elem.click()
time.sleep(random.randint(2,5))

time.sleep(100)



