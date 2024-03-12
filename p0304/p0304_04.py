students = [['홍길동',100,100,99,299,99.97],
            ['유관순',100,100,99,299,99.97],
            ['이순신',100,100,99,299,99.97]]

# 찾는 학생의 이름 입력

# 찾고자 하는 학생찾기
chK = 0 # 찾는 정보 확인
while True:
    search = input('검색하고 싶은 학생을 입력하세요.(0. 취소) > ')
    if search == '0':
        break
    for stu in students:
        if search in stu:
            chk = 1 # 정보를 찾았을 때 정보를 1로 변경
            break
        
        if chk == 1:
            print('{} 학생정보를 찾았습니다'.format(search))
        else:
            print('찾는 학생이 없습니다.')


