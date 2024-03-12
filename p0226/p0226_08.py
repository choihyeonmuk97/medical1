# random 함수
from random import *

print(random()) # 0.0~1.0 미만의 임의의 값 생성

print(int(random()*10)) # 0~10
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1) # 1~10

print(int(random()*45)+1)# 1~45이하 임의의 값

print(randrange(1,46)) # 1~46미만

print(randint(1,45)) #1~45 미만

# 1~10 사이의 숫자를 입력받아서 변수 1
# 변수2는 1~10 사이의 랜덤 숫자
# 랜덤한 숫자와 같으면 [당첨],
# 다르면 [랜덤숫자는 {}로 일치하지 않습니다.]

n1 = int(input('1~10사이의 숫자를 입력하세요 > '))
n2 = randint(1,10) # int((random()*10)+1) 같음

if n1 == n2:
    # print(n1, n2)
    print('당첨!')
else :
    # print(n1, n2)
    print('랜덤숫자는 {}로 일치하지 않습니다.'.format(n2))
