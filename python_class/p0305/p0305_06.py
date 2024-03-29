import random

a = []
# 1~25까지 숫자를 list에 넣기
value = 1
for i in range(0,25):
    a.append(i+1)
print(a)
# 리스트를 섞기
random.shuffle(a)


# 2차원 리스트에 랜덤으로 섞은 숫자 넣기
arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    
for i in range(0,5):
    for j in range(0,5):
        arr[i][j] = a[(5*i)+j] # i, j 0일 때 a[0]번 방이 arr[0][0]...
    # print(arr)

# 출력
while True:
    print('-'*50)
    print('       [좌표맞추기 프로그램]')
    print('-'*50)
    print('순번',0,1,2,3,4,sep='\t')
    print('-'*50)
    for i in range(0,5):
        print(i,end='\t')
        for j in range(0,5):
            print(arr[i][j],end='\t')
        print()
    print('-'*50)
    x = int(input('X 좌표를 입력하세요'))
    y = int(input('Y 좌표를 입력하세요'))
    arr[x][y] = "X"

