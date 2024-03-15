import stu_file

# 파일 가져오기
students = stu_file.stu_open()

s_title = ['','국어','영어','수학']

# 메인화면표출 함수
def stu_screen():
    print('-'*60)
    print('\t\t  [학생성적프로그램]')
    print('-'*60)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7. 학생성적 파일저장')
    print('0. 프로그램 종료')
    print('-'*60)
    choice = input('원하는 번호를 입력하세요 > ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
    choice = int(choice)
    print('-'*60)
    return(choice)

# 학생성적입력 함수
def stu_inp(cnt):
    while True:
        name = input(f'{len(students)+1}번째 이름을 입력하세요.(0. 취소) > ')
        if name == '0':
            print('학생 입력을 취소합니다.')
            break
        student = {}
        student["stuNo"] = cnt
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

# 학생성적상단출력 함수
def stu_top():
    print('\t\t  [학생 성적 출력]')
    print('-'*60)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*60)

# 학생성적전체출력 함수
def stu_all(students):
    stu_top()
    for stu in students: # stu = dict
        for s in stu: # s = key
            print(stu[s],end='\t') # stu[s] = value
        print()
    print('-'*60)

# 학생성적검색 함수
def stu_search():
    # 학생검색 -> 이름으로 검색을 해서 해당하는 학생이 있으면 해당학생 성적출력
    # 1명 출력
    search_students = []
    print("[ 학생성적 검색 ]")
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
            search_students.append(students[chk]) # 리스트에 추가
            stu_all(search_students)

# 학생성적수정(과목) 함수
def stu_sub_update(s_input,chk,s_1):
    print(f'{s_title[s_input]}점수를 수정합니다.')
    print(f"{s_title[s_input]} 점수 : {students[chk][s_1]}",)
    print('-'*60)
    score = int(input(f'수정할 {s_title[s_input]}점수를 입력하세요 : '))
    students[chk][s_1] = score
    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    students[chk]["avg"] = float('{:.2f}'.format(students[chk]["total"]/3))
    print(f"{score}점으로 수정되었습니다.")
    print(students[chk])

# 학생성적수정(전체) 함수
def stu_all_update():
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
                    stu_sub_update(s_input,chk,s_1)
                    
                elif s_input == 2:
                    s_1 = 'eng'
                    stu_sub_update(s_input,chk,s_1)
                    
                elif s_input == 3:
                    s_1 = 'math'
                    stu_sub_update(s_input,chk,s_1)

# 등수처리 함수
def stu_rank():
    for i,s_dic in enumerate(students):
        rank_cnt = 1 # 등수 처리 변수
        for i_dic in students:
            if s_dic["total"] < i_dic["total"]: # 두 수를 비교
                rank_cnt += 1 # 현재학생(s_dic)의 합계보다 크면 1 증가
        s_dic["rank"] = rank_cnt
    
    print('등수처리가 완료되었습니다.')
    print(students)

# 학생성적삭제 함수
def stu_del():
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

# 학생성적 파일열기
def stu_open():
    students = []
    with open('stu.txt','r',encoding='utf8') as f :
        while True:
            txt = f.readline()
            if txt == '': break
            t_list = txt.split(',')
            s_dic = {
                'stuNo':int(t_list[0]),'name':t_list[1],
                'kor':int(t_list[2]),'eng':int(t_list[3]),'math':int(t_list[4]),
                'total':int(t_list[5]),'avg':float(t_list[6]),'rank':int(t_list[7])
            }
            students.append(s_dic)
    
    return students


# 파일 저장
def stu_save(students):
    with open('stu.txt','w',encoding='utf8') as f :
        for s in students:
            stuNo = s["stuNo"]
            name = s["name"]
            kor = s["kor"]
            eng = s["eng"]
            math = s["math"]
            total = s["total"]
            avg = s["avg"]
            rank = s["rank"]
            f.write(f"{stuNo},{name},{kor},{eng},{math},{total},{avg},{rank}\n")
    print("파일에 저장되었습니다.")
    print()
    


cnt = len(students)+1 # 학번 사용
while True:
    choice = stu_screen()
    
    # 1. 학생성적입력 프로그램
    if choice == 1:
        stu_inp(cnt)
        
    # 2. 학생성적출력 프로그램
    elif choice == 2:
        stu_all(students)    
    
    # 3. 학생 검색
    elif choice == 3:
        stu_search()
    
    # 4. 성적 수정
    elif choice == 4:
        stu_all_update()
    
    # 5. 등수처리
    elif choice == 5:
        stu_rank()           

    
    # 6. 성적 삭제
    elif choice == 6:
        stu_del()

    # 7. 파일 저장
    elif choice == 7:
        stu_file.stu_save(students)

    # 0 . 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break 

