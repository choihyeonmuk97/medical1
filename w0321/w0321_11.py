import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5+%EB%B6%84%EC%96%91'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

# with open ('new.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

# d_list = (soup.find('div',{'class':'cont_place'})) => 얘는 등촌3단지만

d_list = (soup.find('ol',{'class':'list_place'}))
dd_list = d_list.find_all('dd')

for i in range(len(d_list)):    
    print(d_list.find('a',{'class':'fn_tit'}).text)
    print('-'*60)
    print('매매시세 :',dd_list[1].text)
    print('전세시세 :',dd_list[2].text)
    print('-'*60)








# print(dd_list)
# print('[ 등촌주공 3단지 ]')
# print('-'*60)
# print('매매시세 :',dd_list[1].text)
# print('전세시세 :',dd_list[2].text)
# print('-'*60)
