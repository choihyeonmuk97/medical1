'''
변수명 : stu_no, stu_name, kor, eng, math, total, avg, rank
출력 :
번호     이름   국어   영어   수학   합계   평균   등수
 1      홍길동  100    100    100   300  100.00   1
'''

stu_no = input('번호를 입력하세요 >> ')
stu_name = input('성명을 입력하세요 >> ')
kor = input('점수')
eng = input('점수')
math = input('점수')

a = kor
b = eng
c = math
total = ((int(a)+int(b)+int(c)))
avg = ((int(a)+int(b)+int(c))/3)

print('번호 \t 이름 국어 영어 수학 합계 평균')
print(' {}\t {},{},{},{},{},{:.2f}'.format(stu_no,stu_name,kor,eng,math,total,avg) )




 