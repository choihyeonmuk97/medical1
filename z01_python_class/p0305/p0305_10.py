# 학번 1000, 이름 홍길동 학과 컴공
# 딕셔너리
student = {"학번":1000,"이름":"홍길동","학과":"컴퓨터공학과"}
for key in student:
    print(key,student[key])

# 연락처 010-1111-1111 추가
student["연락처"] = "010-1111-1111"
print(student)

# 수정
student["이름"] = "유관순"
print(student)

# 컴공 -> 화학과
student["학과"] = "화학과"
print(student)

    
# student['키값']
# student.get('키값')

for i in student.keys():
    print(i)
print(type(student.keys())) # class 타입
print(student.keys()) # .keys() 딕셔너리의 모든 key(키)를 출력
print(list(student.keys())) # list 타입으로 형변환
print('-'*50)

# .values() : 딕셔너리의 모든 value(값)를 출력
print(student.values()) # class 타입
print(list(student.values())) # list 타입으로 형변환

for i in student.values():
    print(i)

# items() 튜플 형태 데이터를 리턴 / 튜플 수정 삭제 불가
print(student.items())

if '이름' in student:
    print('키값이 있습니다.')
else:
    print('키값이 없습니다.')