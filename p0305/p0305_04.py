a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# 2차원 리스트 1~25까지 데이터 넣기
value = 1
for i in range(0,5):
    for j in range(0,5):
        a[i][j] = value #(5*i)+j+1
        value += 1
print(a)

# 좌표를 입력하면 좌표를 0으로 변경하는 프로그램을 구현
while True:
    # 2차원 리스트 출력
    print(0,0,1,2,3,4,sep='\t')
    print('-'*50)
    for i in range(0,5):
        print(i,end='\t')
        for j in range(0,5):
            print(a[i][j],end='\t')
        print()

    x = int(input('X 좌표를 입력하세요.'))
    y = int(input('Y 좌표를 입력하세요.'))
    a[x][y] = 'X' # 입력된 좌표값이 0으로 변경
