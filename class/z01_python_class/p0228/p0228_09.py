# for 문을 사용해서 2단 출력
for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
    
# 입력받은 숫자의 단을 출력
# n = int(input('숫자를 입력하세요 > '))
# for i in range(1,10):
#     print('{}*{}={}'.format(n,i,n*i))
    
# 중첩 for
# for 안에 for
for i in range(3):
    print('i=',i)
    for j in range(2):
        print('j=',j)
        
for i in range(2,10):
    print('[{}단]'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()

# 출력 형태
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for j in range(5): # j = 0 1 2 3 4
    print(j+1,'번째 출력')
    for i in range(1,6): # i = 1 2 3 4 5
        print(i,end=' ')
    print()

# 짝수단만 출력
for i in range(2,10):
    if i % 2 == 0:
        print('{}단'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()

# 홀수단만 출력
for i in range(2,10):
    if i % 2 == 1:
        print('{}단'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()

# (*1,3,5,7,9)
for i in range(2,10):
    print('[{}단]'.format(i))
    for j in range(1,10):
        if j % 2 == 1:
            print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()


