# 1~100까지의 합
sum1 = 0
for i in range(1,101):
    sum1 += i
print('1~100까지의 합은 {}입니다.'.format(sum1))

# 1~100까지 짝수의 합
sum2 = 0
for i in range(1,101):
    if i % 2 == 0:
        sum2 = sum2 + i
print('1~100까지 짝수의 합은 {}입니다.'.format(sum2))

# 1~100까지 홀수의 합
sum3 = 0
for i in range(1,100):
    if i % 2 != 0: # -> i % 2 == 1
        sum3 = sum3 + i
print('1~100까지 홀수의 합은 {}입니다.'.format(sum3))

# 1~10 까지의 합
sum1 = 0
for i in range(1,11):
    sum1 += i
print('1~10까지의 합은 {}입니다.'.format(sum1))

num = [1,2,3,4,5,6,7,8,9,10]
# num리스트 안에 있는 값들의 합
sum2 = 0
for i in range(len(num)):
    sum2 = sum2 + num[i]
print(sum2)

sum2 = 0
for n in num:
    sum2 = sum2 + n
print(sum2)

