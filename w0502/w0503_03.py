import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# 야놀자 검색 클릭 후 호텔, 날짜 6/5~6 -> 확인 -> 엔터 -> 스크롤 이동 반복 / 이미지,제목,평점,평가수,금액 저장
# yanolja 테이블 / yno,img,title,grade,grade_num,price comn

url = "https://www.yanolja.com/"
browser.get(url)
time.sleep(2)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]')
time.sleep(1)
elem.click()
time.sleep(1)

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//button[text()="확인"]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'//input[@class="SearchInput_input__342U2"]')
elem.click() 
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
time.sleep(5)

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)

cnt = 0
while True:
    if cnt == 5: break
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print('현재 높이 :',curr_height)
    cnt += 1


# 데이터 불러오기
soup = BeautifulSoup(browser.page_source,'lxml')

divs = soup.find_all('div',{'class':'PlaceListItemText_container__fUIgA text-unit'})
print(len(divs))

for div in divs[0:5]:
    img = div.find('div',{'class':'PlaceListImage_imageText__2XEMn'})['style']
    print('이미지 링크 :',img)

    title = div.find('div',{'class':'PlaceListTitle_container__qe7XH'}).text
    print('타이틀 :',title)

    grade = div.find('span',{'class':'PlaceListScore_rating__3Glxf'}).text
    print('평점 :',grade)

    grade_num = div.find('span',{'class':'PlaceListScore_rating__3Glxf'}).nextSibling.text
    grade_num = grade_num[1:-1].replace(',','')
    print('평가 수 :',grade_num)

    try:
        price = div.find('span',{'class':'PlacePriceInfoV2_discountPrice__1PuwK'})
        price = int(price.text.replace(',',''))
        print('가격 :',price)
    except:
        print('가격 : 0')
        continue



time.sleep(100)
