# 1~5까지의 합계
sum = 1+2+3+4+5
print(sum)
total = 0
total = total + 1
total = total + 2
total = total + 3
total = total + 4
total = total + 5
print(total)
t = 0
for i in range(1,6,1):
    t = t + i
t = 0
for i in range(1,6,1):
    t += i
print(t)

# 1~10까지 합
t = 0
for i in range(1,11,1):
    t += i
    print(t)
print('1부터 10까지의 합은 : {}입니다.'.format(t))
# 1~100까지 합
t = 0
for i in range(1,101,1):
    t += i
print('1부터 100까지의 합은 : {}입니다.'.format(t))

# 입력한 수 부터 입력한 수 까지의 합
n1 = int(input('숫자 > '))
n2 = int(input('숫자 > '))
sum1 = 0
for i in range(n1,n2+1,1):
    sum1 = sum1+i
print(sum1)