from random import *

n1 = randrange(1,10) # 1-9 사이의 정수
n2 = randrange(10) # 0-10 사이의 정수
n3 = randint(1,10) # 1-10 사이의 정수

print(n1,n2,n3)

lotto = []
# lotto에 1~10사이의 랜덤한 숫자 6개를 넣어보세요
for i in range(6):
    n = randint(1,10)
    print(n)
    lotto.append(n)
print(lotto)

mynum = []
# 내가 직접 입력한 숫자 6개
for i in range(6):
    Mynum = int(input('로또당첨기원 > '))
    print(Mynum)
    mynum.append(Mynum)
print(mynum)

