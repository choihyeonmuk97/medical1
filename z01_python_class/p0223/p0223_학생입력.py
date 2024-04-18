# 학생성적입력
# 변수를 사용

stu_name = input('이름을 입력하세요 >> ')
kor = int(input('국어점수를 입력하세요 >> '))
eng = int(input('영어점수를 입력하세요 >> '))
math = int(input('수학점수를 입력하세요 >> '))

# 입력을 받아서 총점과 평균을 계산하고 출력

total = (kor+eng+math)
avg = total/3


print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print(' {}\t{}\t{}  \t{} \t{}  \t{} \t{:.2f} \t{}'.format(
    1,stu_name,kor,eng,math,total,avg,1))

stu = [1,'홍길동',100,100,100,300,100.0,1]
stu1 = [1,stu_name,kor,eng,math,total,avg,1]

print(stu)
print(stu1)
