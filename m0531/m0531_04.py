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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://www.coupang.com/vp/products/227331483?itemId=720227345&vendorItemId=4822351124&q=%ED%95%98%EB%A6%BC+%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4&itemsCount=36&searchId=47ebc727c6ee4321a0f2798d9ea5d0e3&rank=0&isAddedCart=#sdpReview"

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

time.sleep(2)

soup = BeautifulSoup(browser.page_source,'lxml')

elem = browser.find_element(By.XPATH,'//*[@id="btfTab"]/ul[1]/li[2]') # 상품평 누름..
time.sleep(5)
elem.click()

# 모든상품보기 인데 터짐..
# elem = browser.find_element(By.XPATH,'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[2]/div[3]/div[1]/div[1]/img[2]') 
# time.sleep(5)
# elem.click()

time.sleep(100)
