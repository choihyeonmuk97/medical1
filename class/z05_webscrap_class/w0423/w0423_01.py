import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/bestChallenge'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# with open('webtoon1.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())























# browser = webdriver.Chrome()
# browser.get('https://www.naver.com/')

# time.sleep(10)

# element = driver.find_element_by_class_name('MyView-module__link_login___HpHMW')
# element.click()