# 중첩 if

a = 97
if a > 90:
    print('90보다 크다')
else:
    print('90보다 작습니다')
   

a = 97
if a > 90:
    print('90보다 큽니다')
    if a < 95:
        print('95보다 작습니다')
    else:
        print('95보다 큽니다')
else:
    print('90보다 작습니다')

# 만약 사과의 상태가 good 이며
# 1000원 이하면 10개 구매
# 1000원 초과 3개 구매 출력
# 사과의 상태가 good이 아니면 사과를 구매하지 않습니다

apple = 'good'
price = 500

if apple == 'good' and price <= 1000:
    print('10개 구매')
    if price > 1000:
        print('3개 구매')
else:
    print('사과를 구매하지 않습니다')

# 숫자 하나를 입력받아서 100보다 크면서 짝수면 짝수 홀수면 홀수
# 100보다 작으면 100보다 작다 출력

num = int(input('숫자를 입력하세요 >> '))
if num > 100:
    if num % 2 == 0:
        print('{}은(는) 짝수입니다.'.format(num))
    else:
        print('{}은(는) 홀수입니다.'.format(num))
else:
    print('{}은(는) 100보다 작습니다.'.format(num))



