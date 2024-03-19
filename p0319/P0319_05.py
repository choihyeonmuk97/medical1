# 검색어가 포함이 되어 있는 모두를 검색하는 방법
name = ['홍길동','유관순','이순신','김구','강감찬','홍길순','홍길자']

while True:
    search = input('이름? ')
    search_list = [] # 찾은 사람의 위치 저장
    cnt = 0 
    # 검색어로 검색
    for n in name:
        if n.find(search) != -1: # 검색어가 포함이 되어 있는지 확인 // != -1 -> 있다
        # if search in name : 도 가능    
            # print('찾았다. 위치 :',cnt)
            search_list.append(cnt)
        cnt += 1

    # 검색된 사람들 출력
    if len(search_list) == 0:
        print('없다.')
    else :
        print(f'{search}(으)로 검색된 사람 :',end=' ')
        for i in search_list:
            print(name[i],end=' ')
        print()






''' 
*정확한 이름으로 찾는 방법

name = ['홍길동','유관순','이순신','김구','강감찬','홍길순','홍길자']

while True:
    search = input('이름? ')
    cnt = 0 
    for n in name:
        if search == n:
            print('찾았다. 위치 :',cnt)
            break
        cnt += 1
        
    if cnt >= len(name):
        print('없다.')
'''