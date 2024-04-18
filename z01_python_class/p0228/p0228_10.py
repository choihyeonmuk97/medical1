# n1단 부터 n2단 까지 출력 (입력받기
n1 = int(input('숫자를 입력하세요 > '))
n2 = int(input('숫자를 입력하세요 > '))
for i in range(n1,n2+1):
    print('{}단'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()

# 크기 비교해서 n1값이 더 크면 n2-n1 값 바꾸기
n1 = int(input('숫자를 입력하세요 > '))
n2 = int(input('숫자를 입력하세요 > '))
if n1 > n2 :
    n1,n2 = n2,n1

for i in range(n1,n2+1):
    print('{}단'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()

# 2단부터 4단까지 
