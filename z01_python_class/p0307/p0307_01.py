student = {'stuNo':1,'stuName':'홍길동','kor':100}
student['eng'] = 100 # 딕셔너리에 없는 값을 추가하기
student['kor'] = 50 # 딕셔너리 값 수정
del student['stuName'] # 딕셔너리 삭제
print(student)

print(student.keys()) # 키 값만 출력 ,리스트로 원할 경우 형 변환 필요
print(student.values()) # value 값만 출력
print(student.items()) # key, value 튜플형태로 추출, 튜플은 수정,삭제 불가



# list = [1,2,3]
# list.append(4)
# print(list)
# del list[0]
# print(list)
# list[0] = 100
# print(list)