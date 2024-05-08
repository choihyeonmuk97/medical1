from random import *

# print(randint(1,100))
# 랜덤한 숫자를 만들어서 (1~100)
# 입력한 값이 랜덤한 숫자랑 같으면 당첨 -> 프로그램 종료
# 아니면 다시 입력해주세요

i = 0
r = randint(1,101)
# 입력한 숫자가 랜덤숫자보다 작으면 더 큰수를 입력하세요
# 입력한 숫자가 랜덤숫자보다 크면 더 작은수를 입력하세요
# 1. 현재 입력한 숫자 모두를 인풋리스트에 넣으세요
inputlist = []
# 2. 10회 도전 후 종료되게 하세요
# 3. 10회 도전이 실패한 사람에게 랜덤숫자 알려주기
while i < 10:
    i += 1
    n = int(input('숫자를 입력하세요 > '))
    inputlist.append(n)
    if r == n:
        print('당첨', r)
        # print('프로그램을 종료합니다.')
        break
    elif r > n:
        print('더 큰 수를 입력하세요')
    else:
        print('더 작은 수를 입력하세요')
        
if i == 10:
    print('실패하셨습니다. 당첨번호는 {}입니다.'.format(r))

print(inputlist)

