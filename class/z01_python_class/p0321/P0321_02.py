class Student:
    # name = ''
    # total= 0
    
    def __init__(self,name,total):
        self.name = name
        self.__total = total # 클래스 내부에서만 접근이 가능
    
    def __str__(self):
        return f'이름 : {self.name}, 합계 : {self.__total}'

    def set_total(self,total,log_id):
        if log_id == "admin":
            self.__total = total    
        else:
            print('관리자만 수정가능합니다.')
    
    def get_total(self):
        return self.__total
    
    # def __gt__(self,s):
    #     return self.total>s.total


s1 = Student('홍길동',95)
s2 = Student('유관순',100)

s1.set_total(400,'admin') 
s1.total = 300 # -> __(캡슐화)로 접근을 막음

print(s1.get_total())
print(s1)
print(s2)

# print(s1 > s2)
