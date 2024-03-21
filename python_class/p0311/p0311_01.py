students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]

subject = ['순번','학번','이름','국어','영어','수학','총점','평균','등수']
s_title = ['','국어','영어','수학']
count = len(students)+1 # 학번

while True:
    print('-'*60)
    print('\t\t\t[학생성적프로그램]')
    print('-'*60)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*60)
    choice = input('원하는 번호를 입력하세요 > ')
    print('-'*60)
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
        continue
    choice = int(choice)

    if choice == 1:
        while True:
            print('[학생성적입력]')
            print('-'*60)
            name = input(f'{len(students)+1}번째 이름을 입력하세요.(0. 취소) > ')
            if name == '0':
                print('취소하셨습니다.')
                break
            student = {}
            student["stuNo"] = 'S'+'{:03d}'.format(count)
            student["name"] = name # 딕셔너리 추가
            kor = int(input('국어점수를 입력하세요. > '))
            student["kor"] = kor
            eng = int(input('영어점수를 입력하세요. > '))
            student["eng"] = eng
            math = int(input('수학점수를 입력하세요. > '))
            student["math"] = math
            total = kor+eng+math
            student["total"] = total
            avg = total/3
            student["avg"] = float('{:.2f}'.format(avg))
            students.append(student)
            count += 1
            print('입력데이터 : ',student)
        print(students)            
            
    elif choice == 2:
        cnt = input('학생들의 성적을 출력합니다.(0. 취소) ')
        if cnt == '0' :
            print('취소하셨습니다.')
            break
        print('\t\t  [학생성적전체출력]')
        print('-'*60)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for stu in students:
            for s in stu: # dict
                print(stu[s],end='\t')
            print()
        
    
    elif choice == 3:
        while True:
            s_name = input('검색할 학생의 이름을 입력하세요.(0. 취소) > ')
            chk = 0
            if s_name == '0':
                print('취소하셨습니다.')
                break
            for s_dic in students:
                if s_dic["name"] == s_name:
                    break
                chk += 1
            
            if chk == len(students):
                print(f'{s_name} 학생이 없습니다. 다시 입력하세요.')
            else :
                print(f'{s_name} 학생의 성적을 출력합니다.')
                print(students[chk])
    
    elif choice == 4:
        while True:
            search = input('수정할 학생의 이름을 입력하세요.(0. 취소) > ')
            chk = 0
            if search == '0':
                print('취소하셨습니다.')
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
            
            if chk == len(students):
                print(f'{search} 학생이 없습니다. 다시 입력하세요.')
            else:
                print(f'{search} 학생을 찾았습니다.')
                while True:
                    s_input = int(input('수정할 과목을 선택하세요.(1.국어 2.영어 3.수학 0.취소) > '))
                    if s_input == 0:
                        print('취소하셨습니다.')
                        break
                    
                    if s_input == 1:
                        s_1 = 'kor'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print('현재점수 : {}'.format(students[chk][s_1]))
                        print('-'*60)
                        score = int(input(f'수정할 {s_title[s_input]}의 점수를 입력하세요. > '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f'{students[chk][s_1]}점으로 수정되었습니다.')
                        print('-'*60)
                        print(students[chk])
                        
                    elif s_input == 2:
                        s_1 = 'eng'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print('현재점수 : {}'.format(students[chk][s_1]))
                        print('-'*60)
                        score = int(input(f'수정할 {s_title[s_input]}의 점수를 입력하세요. > '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f'{score}점으로 수정되었습니다.')
                        print('-'*60)
                        print(students[chk])

                    elif s_input == 3:
                        s_1 = 'math'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print('현재 점수 : {}'.format(students[chk][s_1]))
                        print('-'*60)
                        score = int(input(f'수정할 {s_title[s_input]}의 점수를 입력하세요. > '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f'{score}점으로 수정되었습니다.')
                        print('-'*60)
                        print(students[chk])
    
    elif choice == 5:
        n = input('등수처리를 실행하시겠습니까? (0. 취소)')
        if n == '0':
            print('취소하셨습니다.')
            break
        for i, s_dic in enumerate(students):
            rank_cnt = 1
            for i_dic in students:
                if s_dic["total"] < i_dic["total"]:
                    rank_cnt += 1
            s_dic["rank"] = rank_cnt
        
        print(students)
    
    elif choice == 6:
        while True:
            search = input('삭제하려는 학생의 이름을 입력하세요.(0. 취소) > ')
            chk = 0
            if search == '0':
                print('취소하셨습니다.')
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
            
            if chk >= len(students):
                print(f'{search} 학생이 없습니다. 다시 입력하세요.')
            else:
                print(f'{search} 학생을 찾았습니다.')
                s_input = input(f'{search} 학생의 성적을 삭제하시겠습니까? (1.삭제 0.취소) ')
                if s_input == '0':
                    print('취소하셨습니다.')
                    break
                else:
                    del students[chk]
                    print(f'{search} 학생의 성적이 삭제되었습니다.')
                    print('-'*60)
                    print(students)
    
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break
    