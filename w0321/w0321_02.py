import requests

# 웹에 접근하여 html 소스를 가져옴
res = requests.get('https://www.melon.com/')

print(res) # 200 : 정상 / 403,404 : 페이지 없음 / 500 : 프로그램 에러
print('코드 :',res.status_code) # 리턴한 소스의 코드값 출력
print(type(res.status_code))
if res.status_code == requests.codes.ok:
    print('정상페이지 호출')
else:
    print('공습경보')

res.raise_for_status() # 코드가 200이 아니면 오류처리해서 예외처리 강제로

print(type(res))
print('-'*40)
# requsets를 통해 html 소스 출력
print(res.text)