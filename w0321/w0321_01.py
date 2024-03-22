import requests

# 웹에 접근하여 html 소스를 가져옴
res = requests.get('https://www.google.com/')



print(res) # 200 : 정상 / 403,404 : 페이지 없음 / 500 : 프로그램 에러
print(type(res))
print('-'*40)
# requsets를 통해 html 소스 출력
print(res.text)