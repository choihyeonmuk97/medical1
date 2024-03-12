# 1. 나이가 10살 이상, 키가 150 이상 탑승가능
# input을 이용하여 탑승 가능여부를 출력하기

age = int(input('나이를 입력하세요 > '))
height = int(input('키를 입력하세요 > '))
if age >= 10:
    if height >= 150:
        print('탑승 가능')
    else:
        print('탑승 불가능')
else:
    print('탑승 불가능')

# 2. 숫자 3개(정수)를 입력받고, 연산 1개를 입력받아
# +++ --- *** /// (나머지는 2째자리까지 표현)

a = int(input('숫자를 입력하세요 > '))
b = int(input('숫자를 입력하세요 > '))
c = int(input('숫자를 입력하세요 > '))
c1 = input('연산자를 입력하세요 > ')

if c1 == '+':
    print ('{}+{}+{}={}'.format(a,b,c,a+b+c))
elif c1 == '-':
    print ('{}-{}-{}={}'.format(a,b,c,a-b-c))
elif c1 == '*':
    print ('{}*{}*{}={}'.format(a,b,c,a*b*c))
elif c1 == '/':
    print ('{}/{}/{}={:.2f}'.format(a,b,c,a/b/c))
else:
    print('잘못된 수식을 입력하였습니다.')

