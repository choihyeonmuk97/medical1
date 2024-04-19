import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')


print("타이틀 :",soup.title.text)

d_box = soup.find("input",{"class":"lWzCpb ZEB7Fb"}) #attts={}
dollar = d_box["value"]
print("미국 달러 :",dollar+"$")

w_box = soup.find("input",{"class","lWzCpb a61j6"})
won = w_box["value"]
print("대한민국 원 :",won+"￦")


