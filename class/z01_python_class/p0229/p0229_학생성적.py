students = []
cnt = 0
while True:
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('5. 학생검색출력')
    print('6. 등수처리')
    print('0. 프로그램종료')
    print('-'*35)
    choice = input('원하는 번호를 입력하세요 > ')
    print('입력하신 번호는 {}입니다'.format(choice))
    
    if choice == '1':
        print('[학생성적입력]')
        stu_no = int(input('번호를 입력하세요 > '))
        name = input('이름을 입력하세요 > ')
        kor = int(input('국어성적을 입력하세요 > '))
        eng = int(input('영어성적을 입력하세요 > '))
        math = int(input('수학성적을 입력하세요 > '))
        total = (kor+eng+math)
        avg = total/3
        
        stu=[stu_no,name,kor,eng,math,total,avg,0]
        students.append(stu)
    
    elif choice == '2':
        print('[학생성적수정]')
        rename = input('수정할 학생의 이름을 입력하세요 > ')
        for i,stu in enumerate(students):
            if rename in stu:
                print(rename,'님을 선택하셨습니다.')
                ch_num = input('수정하고 싶은 과목을 선택하세요 (1. 국어, 2. 영어, 3. 수학)')
                if ch_num == '1':
                    print(rename,'님의 국어점수를 수정합니다.')
                    print(rename,'님의 점수는',students[i][2],'점 입니다.')
                    kor_score = input('수정할 점수를 입력하세요 > ')
                    kor_score = int(kor_score)
                    students[i][2] = kor_score
                    students[i][5] = (kor_score+students[i][3]+students[i][4])
                    students[i][6] = students[i][5]/3
                    print('점수가',students[i][2],'점으로 수정되었습니다.')
                if ch_num == '2':
                    print(rename,'님의 영어점수를 수정합니다.')
                    print(rename,'님의 점수는',students[i][3],'점 입니다.')
                    eng_score = int(input('수정할 점수를 입력하세요 > '))
                    students[i][3] = eng_score
                    students[i][5] = (eng_score+students[i][2]+students[i][4])
                    students[i][6] = students[i][5]/3
                    print('점수가',students[i][3],'점으로 수정되었습니다.')
                if ch_num == '3':
                    pass
        
    elif choice == '3':
        print('[학생성적삭제]')
        delname = input('이름을 입력하세요 > ')
        for j, stu in enumerate(students):
            if delname in stu:
                del(students[j])
                print('{} 님이 삭제되었습니다.'.format(delname))
                
            print(students)

    elif choice == '4':
        print('\t[학생 성적 전체 출력]')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for i in range(len(students)):
            print(' {}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format
                  (students[i][0],students[i][1],students[i][2],students[i][3],
                   students[i][4],students[i][5],students[i][6],students[i][7]))
        
    elif choice == '5':
        print('[학생성적검색출력]')
        searchname = input('이름을 입력하세요 > ')
        for i, stu in enumerate(students):
            if searchname in stu:
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
                print(' {}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format
                  (students[i][0],students[i][1],students[i][2],students[i][3],
                   students[i][4],students[i][5],students[i][6],students[i][7]))

    elif choice == '6':
        pass

    elif choice == '0':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못입력하였습니다.')