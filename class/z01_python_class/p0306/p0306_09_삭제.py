students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt = len(students)+1 # 학번
    # 전체 출력
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
