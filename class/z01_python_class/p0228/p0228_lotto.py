from random import *
# 1 ~ 45 까지의 숫자를 넣어서

mynum = [] # input 사용 1~45
for i in range(6):
    n1 = int(input('{}번째 숫자를 입력하세요 > '.format(i+1)))
    mynum.append(n1)
print('-'*35)
lotto = [] # 1 ~ 45 사이 랜덤한 숫자 6자리
r = []
for i in range(1,46):
    r.append(i)
print(r)              # r=[1,2,3...,45] 생성됨

for i in range(100):
    tmp = randint(0,44) # 0~44번째..방 (r리스트)
    r[0],r[tmp]=r[tmp],r[0]

print(r) # 중복없이 섞여진 r 리스트
    
for i in range(6):
    lotto.append(r[i])

print(lotto) # 랜덤하고 중복없는 숫자 6개 
print(mynum)

ok = []
# 매치하는 숫자의 개수 비교
for i in range(6):
    if mynum[i] in lotto:
        ok.append(mynum[i])

print(ok) # 랜덤 숫자와 내가 입력한 숫자와 일치하는 리스트

