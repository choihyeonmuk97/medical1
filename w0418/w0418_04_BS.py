import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml') #text를 html로 파싱
# print(soup.prettify()) # html 소스를 정렬해서 출력함

print("<title> :",soup.title) # 태그정보를 가져옴
print("<title> text :",soup.title.get_text()) # 글자만 가져옴
print("<title> text :",soup.title.text) # 글자만 가져옴
print("<a> :",soup.a)
print("<a> :",soup.a.text)
print("<a> 속성 전체 :",soup.a.attrs) # 태그의 속성값을 모두 가져옴

print("<a>[속성] :",soup.a["href"]) # 특정 태그의 속성값 가져옴
