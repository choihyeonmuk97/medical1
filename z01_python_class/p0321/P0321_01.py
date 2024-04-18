class Student:
    kor = 0
    
    def __init__(self,name):
        self.name = name

class Lotto:
    pass

s = Student('홍길동')

print(s.name)

# isinstance() : 어떤 클래스에서 나왔는지 확인
if isinstance(s,Student):
    print('네')
    
if type(s) == Student:
    print('ㅇㅇ')


