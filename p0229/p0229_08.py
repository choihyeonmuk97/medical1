# 1~100 까지 더하는데
# 총 합이 100이 넘었을때의 그'순간' 숫자와 합을 출력

sum = 0
# for i in range(1,101):
#     sum += i
#     if sum > 100:
#         print(sum,end=' ') 
#         print(i,end=' ')
# print()

for i in range(1,101):
    sum += i
    if sum > 100:
        break

print(i)
print(sum)

total = 0
i = 1
while i <= 100:
    total += i
    if total > 100:
        break
    i += 1
    
print(i)
print(total)
