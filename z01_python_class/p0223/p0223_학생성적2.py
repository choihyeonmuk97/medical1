stu1 = [1,'홍길동',100,100,100,300,100.0,1]
stu2 = [2,'유관순',90,90,90,270,90.0,2]

print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1. 학생성적입력')
print('4. 학생성적전체출력')
print('0. 프로그램 종료')
print('-'*35)
choice = int(input('원하는 번호를 입력하세요 >> '))

if choice == 1:
    print('[학생성적입력을 선택하셨습니다.]')
    
    stu3=[]
    stu31 = input('번호를 입력하세요 > ')
    stu32 = input('이름을 입력하세요 > ')
    stu33 = int(input('국어성적을 입력하세요 > '))
    stu34 = int(input('영어성적을 입력하세요 > '))
    stu35 = int(input('수학성적을 입력하세요 > '))
    stu36 = (stu33+stu34+stu35)
    stu37 = float(stu36/3)
    stu38 = input('등수를 입력하세요 > ')
    
    stu3.append(stu31)
    stu3.append(stu32)
    stu3.append(stu33)
    stu3.append(stu34)
    stu3.append(stu35)
    stu3.append(stu36)
    stu3.append(stu37)
    stu3.append(stu38)
    
    print(stu3)
    
elif choice == 4:
    print('[학생성적출력을 선택하셨습니다.]')
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]
))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]
))
elif choice == 0:
    print('프로그램을 종료합니다.')
else:
    print('[잘못선택하셨습니다.]')
