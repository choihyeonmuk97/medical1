student = []
# 두명 이상의 학생의
# 이름, 국영수 점수를 입력받아
# 리스트 생성 후, student 리스트에 넣어주세요
stu1 = []
name1 = input('이름을 입력하세요 > ')
kor1 = int(input('점수를 입력하세요 > '))
eng1 = int(input('점수를 입력하세요 > '))
math1 = int(input('점수를 입력하세요 > '))
total1 = (kor1+eng1+math1)
avg1 = total1/3

stu1.append(name1)
stu1.append(kor1)
stu1.append(eng1)
stu1.append(math1)
stu1.append(total1)
stu1.append(avg1)

stu2 = []
name2 = input('이름을 입력하세요 > ')
kor2 = int(input('점수를 입력하세요 > '))
eng2 = int(input('점수를 입력하세요 > '))
math2 = int(input('점수를 입력하세요 > '))
total2 = (kor2+eng2+math2)
avg2 = total2/3

stu2.append(name2)
stu2.append(kor2)
stu2.append(eng2)
stu2.append(math2)
stu2.append(total2)
stu2.append(avg2)

student.append(stu1)
student.append(stu2)

# student 리스트 전체 출력
print(student)