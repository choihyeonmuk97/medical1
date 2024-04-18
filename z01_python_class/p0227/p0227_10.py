num = []
# for문을 사용해서 1~10까지 숫자를 채우세요
for i in range(1,11):
    num.append(i)
    
print(num)

num2 = []
# 1~10까지의 짝수를 넣으세요
for i in range(1,11):
    if i % 2 == 0:
        num2.append(i)

print(num2)

# 1~10까지 합을 for 사용해서 구할 수 있음
num = [1,2,3,4,5,6,7,8,9,10]
# num리스트를 사용해서 1~10까지의 합
s1 = 0
for n in num: 
    # print(n, end=' ')
    s1 += n
print(s1)

s2=0
for i in range(len(num)):
    # print(num[i], end=' ')
    s2 = s2 + num[i]
print(s2)

# num2리스트 내 합
s3=0
for n in num2:
    s3 += n
print(s3)

s4 = 0
for i in range(len(num2)):
    s4 = s4 + num2[i]
print(s4)