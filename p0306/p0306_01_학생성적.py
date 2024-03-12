students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt = len(students)+1 # 학번사용

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
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
        continue # 반복문 계속(다시) 실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1:
        while True:
            name = input(f'{len(students)+1}번째 이름을 입력하세요.(0. 취소) > ')
            if name == '0':
                print('학생 입력을 취소합니다.')
                break
            student = {}
            student["stuNo"] = "S"+"{:03d}".format(cnt)
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
            student["avg"] = float("{:.2f}".format(avg))
            students.append(student)
            # list 추가
            cnt += 1
            print('입력데이터 : ',student) # dict
        print(students)
        
    # 2. 학생성적출력 프로그램
    elif choice == 2:
        count = input('학생 전체 출력을 하시겠습니까? (1. 확인 0. 취소) > ')
        if count == '0':
            break
        print('\t\t  [학생 성적 출력]')
        print('-'*60)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for stu in students: # stu = dict
            for s in stu: # s = key
                print(stu[s],end='\t') # stu[s] = value
            print()
        print('-'*60)
    
    # 학생 검색
    elif choice == 3:
        while True:
            search = input('검색할 학생의 이름을 입력하세요.(0. 취소) > ')
            chk = 0
            if search == '0':
               print('취소하셨습니다.')
               break
            for s_dic in students:
               if s_dic['name'] == search:
                   break
               chk += 1
            if chk == len(students):
                print(f'{search} 학생이 없습니다. 다시 입력하세요.')
            else:
                print(f'{search} 학생의 성적을 출력합니다.')
                print(students[chk])
                 
                
    
    # 성적 수정
    elif choice == 4:
        while True:
            search = input('학생의 이름을 입력하세요.(0. 취소) > ')
            chk = 0
            if search == '0':
                print('취소하셨습니다.')
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
            
            if chk == len(students):
                print(f'{search} 학생이 없습니다. 다시 입력하세요')
            else:
                print(f'{search} 학생을 찾았습니다.')
                while True:
                    s_input = int(input('수정할 과목을 선택하세요. > 1. 국어 2. 영어 3. 수학 0. 취소 > '))
                    if s_input == 0:
                        print('취소하셨습니다.')
                        break
                    if s_input == 1:
                        s_1 = 'kor'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print(f"{s_title[s_input]} 점수 : {students[chk][s_1]}",)
                        print('-'*50)
                        score = int(input(f'수정할 {s_title[s_input]}점수를 입력하세요 : '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f"{score}점으로 수정되었습니다.")
                        print(students[chk])
                        
                    elif s_input == 2:
                        s_1 = 'eng'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print(f"{s_title[s_input]} 점수 : {students[chk][s_1]}",)
                        print('-'*50)
                        score = int(input(f'수정할 {s_title[s_input]}점수를 입력하세요 : '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f"{score}점으로 수정되었습니다.")
                        print(students[chk])
                        
                    elif s_input == 3:
                        s_1 = 'math'
                        print(f'{s_title[s_input]}점수를 수정합니다.')
                        print(f"{s_title[s_input]} 점수 : {students[chk][s_1]}",)
                        print('-'*50)
                        score = int(input(f'수정할 {s_title[s_input]}점수를 입력하세요 : '))
                        students[chk][s_1] = score
                        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                        students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
                        print(f"{score}점으로 수정되었습니다.")
                        print(students[chk])
    
    # 등수
    elif choice == 5:
        for i,s_dic in enumerate(students):
            rank_cnt = 1 # 등수 처리 변수
            for i_dic in students:
                if s_dic["total"] < i_dic["total"]: # 두 수를 비교
                    rank_cnt += 1 # 현재학생(s_dic)의 합계보다 크면 1 증가
            s_dic["rank"] = rank_cnt
        
        print('등수처리가 완료되었습니다.')
        print(students)            

    
    # 성적 삭제
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
                print(f'{search} 학생이 없습니다. 다시 입력하세요')
            else:
                print(f'{search} 학생을 찾았습니다.')
                s_input = input(f'{search} 학생 성적을 삭제하겠습니까? 1.삭제 0. 취소 > ')
                # 삭제
                if s_input == '0':
                    print('취소하셨습니다.')
                    break  
                else:
                    del students[chk]
                    print(f'{search} 학생성적이 삭제되었습니다.')
                    print(students)

    # 0 . 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break 

