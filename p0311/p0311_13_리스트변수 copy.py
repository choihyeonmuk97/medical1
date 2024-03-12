# 함수 선언
def stu_update(student): # 지역 변수 -> 리스트의 주소값이 저장됨
    student[0] = 2
    student[1] ='유관순'
    student[5] = student[2]+student[3]+student[4]
    student[6] = student[5]/3

# 프로그램 구현
student=[1,'홍길동',100,100,100,0,0] # 2개 이상의 변수


# 함수 호출
stu_update(student) # 전역 변수

print('학생1 : ',student)


