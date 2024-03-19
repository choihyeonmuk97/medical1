stu = [
    ['홍길동',100],['유관순',98],['이순신',95],['김구',50],['강감찬',99],['홍길순',80],['홍길자',70],
]

# 이름으로 검색해서 홍이 들어가는 사람을 모두 검색해서 출력
# 이름으로 검색해서 신이 들어가는 사람을 모두 검색해서 출력

while True:
    print('[ 학생성적검색 ]')
    print('1. 이름으로 검색')
    print('2. 점수 검색')
    choice = int(input('번호입력 : '))
    
    if choice == 1:
        search = input('이름검색 : ')
        search_list = []
        cnt = 0
        for s in stu:
            if search in s[0]:
                search_list.append(cnt)
            cnt += 1
        
        if len(search_list) == 0:
            print('없다.')
        else:
            print(f'{search}(으)로 검색된 사람 :',end=' ')
            for i in search_list:
                print(stu[i][0],end=' ')
            print()

    elif choice == 2:
        score = int(input('몇 점 이상 입력 : '))
        # 80 -> 80점 이상만 입력
        score_list = []
        cnt = 0 
        for s in stu:
            if score <= s[1]:
                score_list.append(cnt)
            cnt += 1
        
        if len(score_list) == 0:
            print('없다.')
        else:
            print(f'{score}점 이상인 사람 :')
            for i in score_list:
                print(stu[i][0],':',stu[i][1])
            print()



       