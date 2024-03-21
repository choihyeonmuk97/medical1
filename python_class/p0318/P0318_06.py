class Student:
    # stuNo = 0
    # stu_name = ''
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    
    def __init__(self,stuNo=0,stu_name='',kor=0,eng=0,
                 math=0,total=0,avg=0,rank=0):
        self.stuNo = stuNo
        self.stu_name = stu_name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float('{:.2f}'.format(self.total / 3))
        self.rank = 0
    
# 1,홍길동,100,100,99,299,99.67,1 -> 기본생성자

s1 = Student()
s1.stuNo = 1
s1.stu_name = '홍길동'
s1.kor = 100
s1.eng = 100
s1.math = 99
s1.total = s1.kor+s1.eng+s1.math
s1.avg = float('{:.2f}'.format(s1.total/3))
s1.rank = 1

print(f'{s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}')

# 2,유관순,99,99,98,296,98.67,2 -> 전체 생성자
s2 = Student(2,'유관순',99,99,98)
print(f'{s2.stuNo},{s2.stu_name},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}')

# 3,이순신,80,80,81,241,80.33,3
s3 = Student(3,'이순신',80,80,81)
print(f'{s3.stuNo},{s3.stu_name},{s3.kor},{s3.eng},{s3.math},{s3.total},{s3.avg},{s3.rank}')

# 3명의 학생을 리스트에 추가
stu_list = [s1,s2,s3]
