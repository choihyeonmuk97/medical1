student = [[1,'홍길동',100,100,100,300,100.0,1],
           [2,'유관순',90,90,90,270,90.0,2]]

print('-'*35)
print('\t[학생성적프로그램]')
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('-'*35)
ch = int(input('원하는 번호를 입력하세요 > '))

if ch == 1:
    print('[학생 성적 입력]')
    stu_no = int(input('학생번호를 입력하세요 > '))
    name = input('이름을 입력하세요 > ')
    kor = (int(input('국어점수를 입력하세요 > ')))
    eng = (int(input('영어점수를 입력하세요 > ')))
    math = (int(input('수학점수를 입력하세요 > ')))
    total = (kor+eng+math)
    avg = total/3
    
    stu3 = [stu_no,name,kor,eng,math,total,avg,3]
    student.append(stu3)
    print(student)

elif ch == 4:
    
    student = [[1,'홍길동',100,100,100,300,100.0,1],
           [2,'유관순',90,90,90,270,90.0,2]]
    stu_no = 3
    name = '이순신'
    kor = 80
    eng = 80
    math = 80
    total = (kor+eng+math)
    avg = total/3
    
    stu3 = [stu_no,name,kor,eng,math,total,avg,3]
    student.append(stu3)
    
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[0][0],student[0][1],student[0][2],student[0][3],
          student[0][4],student[0][5],student[0][6],student[0][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[1][0],student[1][1],student[1][2],student[1][3],
          student[1][4],student[1][5],student[1][6],student[1][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[2][0],student[2][1],student[2][2],student[2][3],
          student[2][4],student[2][5],student[2][6],student[2][7]))
else:
    print('잘못입력하였습니다.')
