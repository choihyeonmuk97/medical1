num2 = []
n = []
for i in range(1,26):
    if i % 5 == 0:
        n.append(i) # 5] -> num2[0] / 10] -> num2[1] ....~~
        num2.append(n)
        n=[]
    else:
        n.append(i) # [1,2,3,4 / [6,7,8,9

print(num2)