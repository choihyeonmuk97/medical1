# 랜덤 숫자 1개 생성 1~100 중
# 입력한 숫자보다 크면 작은수를 입력하세요
# 입력한 숫자보다 작면 큰수를 입력하세요 라고 출력
# 정답을 맞추면 
# 총 입력한 횟수 : ? 회
# 현재까지 입력한 숫자 : 1,5,7,6,8,4,50 를 출력

import random

ran_num = random.randint(1,100) # 랜덤 숫자 생성
in_num = 0
cnt = 1
inp_num = []
while True:
    print('[ 랜덤숫자 맞추기 ]')
    in_num = int(input(f'{cnt}번째 도전. 1~100 사이의 숫자를 입력하세요. > '))
    inp_num.append(in_num)
    if ran_num > in_num:
        print('입력한 숫자보다 큰 수를 입력하세요. ')
    elif ran_num < in_num:
        print('입력한 숫자보다 작은 수를 입력하세요. ')
    elif ran_num == in_num:
        print('정답입니다 !! (정답 : {})'.format(ran_num))
        break
    cnt += 1

print(f'도전 횟수 : {cnt}회')
print('현재까지 입력한 숫자 : {}'.format(inp_num))
