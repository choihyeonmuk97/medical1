class Student:
    stuCount = 0
    stuNo = 0
    
    def __init__(self,name='',kor=0,eng=0,math=0):
        self.name = name
        if kor > 100:
            self.kor = 100
        else:
            self.kor = kor
        
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float('{:.2f}'.format(self.total / 3))
        self.rank = 0
        
        Student.stuCount += 1 # 클래스 변수 선언 -> 클래스명.변수명
        self.stuNo = Student.stuCount
        
    def s_print(self):
        print(self.stuNo,self.name,self.kor,self.eng,self.math,
              self.total,self.avg,self.rank,sep=', ')

    def __str__(self): # __str__가 있을경우 가장 먼저 호출함
        return f'{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'
        
# 홍길동의 성적 넣기

s1 = Student('홍길동',100,100,99)
#print(f'{s1.stuNo},{s1.name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}')
s1.s_print()
print(s1) # __str__ 함수 시 str type으로 리턴 받아 출력됨

s2 = Student('유관순',99,99,98)
#print(f'{s2.stuNo},{s2.name},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}')
s2.s_print()
print(s2)

print(s1)
