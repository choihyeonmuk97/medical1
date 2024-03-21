# 1~100 합계를 구하는데 3의 배수는 제외하고 더하기 (continue)
# while or for

i = 0 
sum = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    # print(i)    
    sum += i
    
print(sum)

sum1 = 0
for i in range(1,101):
    if i % 3 == 0:
        continue
    sum1 += i
    
print(sum1)

