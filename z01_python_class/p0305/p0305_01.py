# 리스트에 1~25까지 숫자를 리스트에 입력
num = []
for i in range(1,26): # 0,25 면 append시 i+1
    num.append(i)
print(num)

# 1부터 25까지 2차원 리스트 5개씩 짤라서
# [[1,2,3,4,5],[6,7,8,9,10],....,[21,22,23,24,25]]
num2 = []
n = []
for i in range(1,26):
    if i % 5:
        n.append(i)
        num2.append(n)

print(num2)