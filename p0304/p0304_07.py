students = [[1,'홍길동',100,100,99,299,99.67,1],
            [2,'유관순',99,99,98,296,98.67,1],
            [3,'이순신',80,80,81,241,80.33,1],
            [4,'김구',100,100,90,290,96.67,1],
            [5,'김유신',90,70,50,210,70.0,1],
            [6,'강감찬',100,100,100,300,100.0,1]]


# 등수처리 프로그램
while True:
    choice = input('등수처리를 실행하시겠습니까?(1.실행 0. 취소)')
    if choice == '0':
        print('등수처리를 취소하였습니다.')
        break
    else:
        # 등수처리 진행
        for i_stu in students:
            no = 1
            for j_stu in students:
                # 각각의 총합 비교
                if i_stu[5] < j_stu[5] :
                    no += 1 # 비교대상 총합이 더 크면 1증가
            i_stu[7] = no # 등수위치에 no 저장
    print('등수처리가 완료 되었습니다.')
    print('-'*50)
    print('[등수 확인]')
    print(students)
     
                
