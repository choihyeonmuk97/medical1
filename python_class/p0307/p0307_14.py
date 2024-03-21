import random

# 크기가 10인 리스트를 만드는데, 7개는 0으로, 3개는 1로

# list = [0*7+1*3 for i in range(1) ]
# print(list)

list = [0]*10
for i in range(3):
    list[i] = 1
print(list)

# 크기가 100인 리스트 생성, 10개는 1로

alist = [0]*100
for i in range(10):
    alist[i] = 1
print(alist)
print('-'*60)
random.shuffle(alist)
print(alist)
print('-'*60)


# [ 10*10 ] 2차원 리스트로 변경

blists = []
blist = []
for i,j in enumerate(alist):
    if (i+1) % 10 == 0:
        blist.append(j)
        blists.append(blist)
        blist = []
    else:
        blist.append(j)

print(blists)
print('-'*60)    

# 10*10 리스트 1개 추가
newlist = [['추첨']*10 for _ in range(10)]


cnt = 0
while True:
    print('[10*10 좌표]')
    print('-'*60)    
    # print(list2s)
    print(' ',0,1,2,3,4,5,6,7,8,9,sep='     ')
    print('-'*60)    
    for i,n in enumerate(newlist):
        print(i,end='   ')
        for nn in n:
            print(nn,end='  ')
        print()
    print('-'*60)    
    x = int(input('좌표를 입력하세요. '))
    y = int(input('좌표를 입력하세요. '))
    # list2s : 값을 비교, newlist : 표시
    if blists[x][y] == 1: # 당첨
        newlist[x][y] = '당첨'
        cnt += 1
    else: # 꽝
        newlist[x][y] = '[꽝]'
    
    if cnt == 10:
        print('종료')
        break