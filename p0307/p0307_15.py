import random

# 25개의 1차원 리스트 생성 0 - 20개, 1 - 5개
alist = [0 for i in range(25)]
# print(alist)
for i in range(5):
    alist[i] = 1
    
print(alist)
print('-'*60)

# 랜덤 섞기
random.shuffle(alist)
print(alist)
print('-'*60)

'''
blist = [[0]*5 for i in range(5)] # 5*5의 공간을 생성 / 컴프리헨션
for i in range(5):
    for j in range(5):
        blist[i][j] = alist[5*i+j]

for문 이용하는것 보다 시간 단축
'''
# 5*5 2차원 리스트에 넣기
blists = []
blist = []

for i,j in enumerate(alist):
    if (i+1) % 5 == 0:
        # print(i)
        blist.append(j)
        blists.append(blist)
        blist = []
    else:
        blist.append(j)

print(blists)
print('-'*60)

# 추첨 5*5 2차원 배열
viewlist = [['추첨']*5 for i in range(5)]
c_count = 1 # 도전횟수
a_count = 0 # 정답개수
while True:
    print('\t [5*5 blist 좌표]')
    print('-'*60)
    print('  ',0,1,2,3,4,sep='\t')
    print('-'*60)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(blists[i][j],end='\t')
        print()     

    # viewlist 출력
    print('\t [5*5 viewlist 좌표]')
    print('-'*60)
    print('  ',0,1,2,3,4,sep='\t')
    print('-'*60)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(viewlist[i][j],end='\t')
        print() 
    print('-'*60)

    # 좌표 입력 후 확인
    print('현재 도전횟수 : {}번'.format(c_count))
    x= int(input('좌표를 입력하세요. > '))
    y= int(input('좌표를 입력하세요. > '))
    if blists[x][y] == 1:
        viewlist[x][y] = '당첨'
        a_count += 1
    else:
        viewlist[x][y] = '[꽝!]'
    
    if a_count == 5:
        print('5개 다 맞추셨습니다.')
        break
    
    c_count += 1 
    if c_count == 10:
        print('도전횟수를 전부 사용하셨습니다.')
        print('프로그램을 종료합니다.')
        break
