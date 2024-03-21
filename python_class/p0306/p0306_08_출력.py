students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
cnt = len(students)+1 # 학번
    # 전체 출력
while True:
    count = input('학생 전체 출력을 하시겠습니까? (0. 취소) > ')
    if count == '0':
        break
    print('\t\t  [학생 성적 출력]')
    print('-'*60)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균')
    print('-'*60)
    for stu in students: # stu = dict
        for s in stu: # s = key
            print(stu[s],end='\t') # stu[s] = value
        print()
    print('-'*60)
    
