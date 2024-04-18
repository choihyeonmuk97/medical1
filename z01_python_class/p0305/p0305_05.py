
import random
num = random.randint(1,100)
cnt = 0
save_num = []
# 숫자맞추기 프로그램을 구현
# 1~10까지 숫자 랜덤으로 생성하여 숫자를 맞추는 프로그램

while True:
    in_num = int(input('1~100까지의 숫자를 입력하세요.'))
    save_num.append(in_num)
    if num > in_num:
        print('입력한 숫자보다 더 큽니다.')
    elif num < in_num:
        print('입력한 숫자보다 더 작습니다.')
    else:
        print('정답입니다.')
        print('{}번 도전을 하셨습니다.'.format(cnt))
        break
    cnt += 1


