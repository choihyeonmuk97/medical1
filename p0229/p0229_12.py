
member = []
i = 0
# 이름을 입력받아 [1,'홍길동'] [2,'유관순] [3,'이순신']
while True:
    print('-'*25)
    print('1. 입력')
    print('2. 전체출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch= input('원하는 번호를 선택하세요 > ')
    print('-'*25)
    if ch.isdigit():
        ch = int(ch)
    
    if ch == 1:
        print('입력')
        name = input('이름을 입력하세요 > ')
        i = i + 1
        m = [i, name]
        member.append(m)
    
    elif ch == 2:
        print('전체출력')
        print('번호\t이름')
        for i in range(len(member)):
            print(' {}\t{}'.format(member[i][0],member[i][1]))

    elif ch == 3:
        print('검색출력')
        searchname = input('이름을 검색하세요 > ')
        print('번호\t이름')
        for i,m in enumerate(member):
            if searchname in m:
                print(' {}\t{}'.format(member[i][0],member[i][1]))
                
        
    elif ch == 4:
        print('검색삭제')
        delname = input('이름을 입력하세요 > ')
        for i,m in enumerate(member):
            if delname in m:
                del(member[i])
                print('{}님이 삭제되었습니다.'.format(delname))
   
        print(member)
    
    elif ch == 5:
        print('수정')
        rename = input('수정하고 싶은 학생의 이름 > ')
        
        for i,m in enumerate(member):
            if rename in m:
                print(rename,'님을 선택하셨습니다.')
                ch_num = input('수정하고 싶은 항목을 선택하세요(1. 번호수정, 2.이름수정)')
                if ch_num == '1':
                    print(rename,'님의 번호 수정을 선택하셨습니다.')
                    print(rename,'님의 번호는',member[i][0],'입니다.')
                    stu_num = input('새로운 번호를 입력해주세요 > ')
                    stu_num = int(stu_num)
                    member[i][0] = stu_num
                    
                elif ch_num == '2':
                    print(rename,'님의 이름 수정을 선택하셨습니다.')
                    print(rename,'님의 이름은',member[i][1],'입니다.')
                    stu_name = input('새로운 이름을 입력해주세요 > ')
                    member[i][1] = stu_name
                    
                else:
                    print('잘못입력하셨습니다.')            

    elif ch == 0:
        print('종료')
        break
    else:
        print('다시입력하세요')
    
    