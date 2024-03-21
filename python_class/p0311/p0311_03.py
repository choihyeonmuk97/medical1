# 구구단 : 이중 for문
# 변수 1개 사용해야함

temp = 0
for i in range (1,10):
    # if i == 2 -> break
    for j in range(1,10):
        if j == 5:
            temp = 1
            break # 여기에서 프로그램을 종료하는 방법
        print(f'{i} * {j} = {i*j}')
    if temp == 1 :  break
        
    