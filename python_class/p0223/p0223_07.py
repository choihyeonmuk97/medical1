# 넹
cal = input('수식을 입력하세요 (+,-,*,/) > ')
n1 = int(input('숫자를 입력하세요 >> '))
n2 = int(input('숫자를 입력하세요 >> '))

if cal == '+':
    print(n1+n2)
elif cal == '-':
    print(n1-n2)
elif cal == '*':
    print(n1*n2)
elif cal == '/':
    print(n1/n2)
else:
    print('잘못된 수식을 입력하였습니다.')


    
    