# if - else
# if - elif - else
'''
if 조건문1 :
    실행문1 :
elif 조건문2 :
    실행문2 :
else:
    실행문 :

조건문1이 참이면 실행문1 실행 후 종료
조건문1이 거짓이고 조건문2가 참이면 실행문2 실행 후 종료
조건문 1,2가 거짓이면 실행문3 실행 후 종료
'''

# 변수가 양수이면 양수, 음수이면 음수 0이면 0이라고 출력
num = int(input('숫자를 입력하세요 >> '))

if num > 0 :
    print('{}은(는) 양수입니다.'.format(num))
elif num == 0 :
    print('{}은(는) 0입니다.'.format(num))
else :
    print('{}은(는) 음수입니다.'.format(num))

# 돈이 만원 이상 -> 택시를 탄다, 2천원 이상 -> 버스를 탄다
# 천원 이상 -> 따릉이를 빌린다 나머지 -> 걸어간다
money = int(input('금액을 입력하세요 >> ')) # 5000

if money >= 10000:
    print('택시를 탄다.')
elif money >= 2000 :
    print('버스를 탄다.')
elif money >= 1000 :
    print('따릉이를 빌린다.')
else:
    print('걸어간다.')


