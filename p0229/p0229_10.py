# str1 = '10'
# print(str1.isdigit()) # True
# str2 = 'a'
# print(str2.isdigit()) # False


# while True:
#     n = input('원하는 번호를 입력해주세요 > ') # 문자열

#     if n.isdigit(): # 숫자지만 문자열 ex) '0' "1"
#         n = int(n)
#     else:
#         print('문자가 입력되었습니다. 다시 입력해주세요')
#     if n == 0:
#         print('숫자 0이 입력되었습니다')

# 이름을 검색해보고 삭제
students = [[1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],
            [4,'김유신',70],[5,'김구',95]]
while True:
    print('1. 학생 검색')
    print('2. 학생 삭제')
    print('3. 프로그램 종료')
    ch = input('원하는 번호를 입력하세요 > ')
    if ch.isdigit(): # 입력한게 숫자면 True
        ch = int(ch)
    if ch == 1:
        searchname = input('학생의 이름을 입력하세요 > ')
        chk = 0
        for stu in students: 
            if searchname in stu:
                print('{}학생이 존재합니다.'.format(searchname))
                print(stu)
                chk = 1
        if chk  == 0:
            print('검색한 학생이 존재하지 않습니다.')
            
    elif ch == 2:
        delname = input('삭제할 학생의 이름을 입력하세요 > ')
         
        cnnk = 0
        for i, stu in enumerate(students):
            if delname in stu:
                del(students[i])
                cnnk = 1 # 등호 하나는 대입, 두개는 같은지 비교 
                print('학생이 삭제되었습니다.')
        print(students)
        if cnnk == 0:
            print('학생이 존재하지 않습니다.')

    elif ch == 3:
        print('프로그램 종료')
        break    
    else:
        print('잘못입력하였습니다.')
        
        
        
