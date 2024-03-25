import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
# print(soup)
s_all = soup.find('div',{'class':'box_type_l'})
tr_list = s_all.find_all('tr')
stock = tr_list[2]
td_list = stock.find_all('td')

# for i in range(2,7):
#     stock = tr_list[i]
#     td_list = stock.find_all('td')
#     print('순위 :',td_list[0].text)
#     print('종목명 :',td_list[1].find('a').text)
#     print('검색비율 :',td_list[2].text)
#     print('현재가 :',td_list[3].text)
#     print('PER :',td_list[10].text)
#     print('ROE :',td_list[11].text)
#     print('-'*60)

for i in range(2,15):
    stock = tr_list[i]
    td_list = stock.find_all('td')
    if len(td_list) == 1:
        continue
    print('순위 :',td_list[0].text)
    print('종목명 :',td_list[1].find('a').text)
    print('검색비율 :',td_list[2].text)
    print('현재가 :',td_list[3].text)
    print('PER :',td_list[10].text)
    print('ROE :',td_list[11].text)
    print('-'*60)
