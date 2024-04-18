''' 반복문 : for, while

for 변수 in 반복가능한데이터 :
    수행문

for 카운터 변수 in range(시작값, 끝값+1, 증감값) :
    수행문
    
'''

for i in range(0,10,1): 
    print('수행문')

for i in range(0,3): # 증감값이 1인 경우 생략이 가능함
    print(i,'두번째 수행문')

for i in range(5): # 5번 반복
    print('세번째 수행문')

for _ in range(7):
    print('안녕하세요')
    
for i in range(10,0,-2): 
    print(i,'수행문')

l1 = [100,200,300,400,500]
#      0   1   2   3   4 
# 리스트 안 요소 확인 in / not in
'''
for 변수 in 리스트명:
    실행문

for 변수 in range(len(리스트명))
    실행문
    리스트명[변수]
'''

for n in l1:
    print(n)

for i in range(len(l1)):
    print(i)
    print(l1[i])

# for 사용 1~100 사이의 홀수
# 1. if
for i in range(1,100):
    if i % 2 != 0:
        print(i, end=' ')
print()
# 2. if x (증감)
for i in range(1,100,2):
    print(i,end=' ')
print()
# 50~1 사이의 6의 배수를 역순으로 출력
for i in range(50,1,-1):
    if i % 6 == 0:
        print(i, end=' ')
print()

# input 사용
# 2개의 숫자를 입력받음
# 출력 : 사칙연산 a+-*/b=c
# 계산을 10번 반복하는 코드 만드세요

for i in range(10): 
    n1 = int(input('숫자를 입력하세요 > '))
    n2 = int(input('숫자를 입력하세요 > '))
    print('{} + {} = {}'.format(n1,n2,n1+n2))
    print('{} - {} = {}'.format(n1,n2,n1-n2))
    print('{} * {} = {}'.format(n1,n2,n1*n2))
    print('{} / {} = {:.2f}'.format(n1,n2,n1/n2))


for i in range(10):
    n1 = int(input('숫자를 입력하세요 > '))
    n2 = int(input('숫자를 입력하세요 > '))
    cal = input('수식을 입력하세요 > ')
    if cal == '+':
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif cal == '-':
        print('{} - {} = {}'.format(n1,n2,n1-n2))
    elif cal == '*':
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif cal == '/':
        print('{} / {} = {:.2f}'.format(n1,n2,n1/n2))
    else:
        print('오류')

