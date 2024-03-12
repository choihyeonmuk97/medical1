print('2단 출력')
for i in range(1,10) :
    print('2 * {} = {}'.format(i, 2*i))

for i in range(1,10) :
    print('{} * {} = {}'.format(2, i, 2*i))

# 원하는 단을 입력받아 3단출력 
n = int(input('숫자를 입력하세요 > '))
for i in range(1,10):
    print('{} * {} = {}'.format(n,i,n*i))
    
# 5번 반복
for _ in range(5):
    n = int(input('원하는 단을 입력하세요 > '))
    for i in range(1,10):
        print('{} * {} = {}'.format(n,i,n*i))

