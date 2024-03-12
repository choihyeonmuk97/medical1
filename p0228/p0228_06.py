from random import *

n1 = randrange(1,11) # 1 ~ 10 까지의 정수

# 랜덤한 숫자 6개 lotto리스트
lotto = []
for i in range(6):
    n2 = randint(1,10) # 1 ~ 10 까지의 정수
    print(n2)
    lotto.append(n2)
print(lotto)

# 중복 없이 숫자를 받고 싶다.
for i in range(6):
    n2 = randint(1,10) # 1 ~ 10 까지의 정수
    if n2 not in lotto:
        lotto.append(n2)
print(lotto)

# 내가 입력한 숫자 6개 mynum리스트
mynum = []
for i in range(6):
    n = int(input('{}번째 숫자를 입력하세요 > '.format(i+1)))
    mynum.append(n)
print(mynum)
