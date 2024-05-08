# 반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값):
'''
for i in range(3): # i = 0, 1, 2
    print('안녕')
    # i = 0 일때
    # i = 1 일때
    # i = 2 일때
for i in range(3): # i = 0, 1, 2
    print(i)
    
# 숫자 한개를 입력받아 1부터 입력한 수 까지의 합
n1 = int(input('숫자 > '))

sum1 = 0
for i in range(1,n1+1):
    sum1 += i
    print(sum1)
print('1에서 {}까지의 합은 {}입니다.'.format(n1,sum1))

# 1~100까지 짝수의 합
sum1 = 0
for i in range(1,101):
    if i % 2 == 0:
        sum1 = sum1 + i # sum1 += i
       # print(sum1, end =' ')   
print('1에서 100까지 짝수의 합은 {}입니다.'.format(sum1))

# 짝수만 출력
for i in range(1,101):
    if i % 2 == 0:
        print(i, end=' ')
print()

# 1~10까지의 곱
sum2 = 1
for i in range(1,11):
    sum2 = sum2 * i
print(sum2)

