# 조건문 if - elif - else
# 들여쓰기 (tab) 각 구문에 맞게 (조건문, 중첩if 중요!!)

a = 3
if a == 0 :
    print('실행')
elif a == 1:
    print('1 실행')
elif a == 2:
    print('2 실행')
elif a == 3:
    print('3 실행')
else:
    print('else 실행')
    
# 중첩 if
# 0보다 크면 양수, 작으면 음수
# 10보다 작으면 10보다 작음, 크면 10보다 큼

n = 8
if n >= 0:
    print('양수')
    if n > 10:
        print('10보다 큼')
    else:
        print('10보다 작음')
else:
    print('음수')

# 숫자 1개 입력받아 짝수면 짝수 홀수면 홀수

num = int(input('숫자를 입력하시오 > '))
if num > 0:
    if num % 2 == 0:
        print('짝수')
    else : 
        print('홀수')

# 90점 이상 A, 이하는 F
# A+(98이상), A0, A-(93이하) 구간을 나누어 출력

score = int(input('숫자를 입력하세요 > '))
if score >= 90:
    # print('A')
    if score >= 98:
        print('A+')
    elif score <= 93:
        print('A-')
    else:
        print('A')
else:
    print('F')

if score >= 90:
    print('A',end='')
    if score >= 98:
        print('+')
    elif score <= 93:
        print('-')
else:
    print('F')




