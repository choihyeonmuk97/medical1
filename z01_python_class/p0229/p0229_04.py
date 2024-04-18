# 숫자 두개를 입력받고
# 연산자를 입력받아 
# 무한히 계산하는 계산기를 만드는데
# 첫번째 숫자에 0을 입력하면 프로그램 종료

while True:
    n1 = int(input('숫자를 입력하세요 > '))
    if n1 == 0:
        print('프로그램을 종료합니다.')
        break

    cal = input('수식을 입력하세요 > ')
    n2 = int(input('숫자를 입력하세요 > '))

    if cal == '+':
        n1 + n2 == n1+n2
        print('{} + {} = {:,}'.format(n1,n2,n1+n2))
    elif cal == '-':
        n1 - n2 == n1-n2
        print('{} - {} = {:,}'.format(n1,n2,n1-n2))
    elif cal == '*':
        print('{} * {} = {:,}'.format(n1,n2,n1*n2))
    elif cal == '/':
        print('{} / {} = {:,.2f}'.format(n1,n2,n1/n2))
    else:
        print('잘못 입력하셨습니다.')

