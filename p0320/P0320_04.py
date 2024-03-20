class Student:
    def __init__(self,name,total):
        self.name = name
        self.total = total
    
    def __str__(self):
        return f'이름 : {self.name}, 총점 : {self.total}'

    def __del__(self):
        return '클래스가 소멸될 때 실행'

    def __add__(self,s):
        return self.total+s.total
    
    def __gt__(self,s):
        # print('보다 큰 가를 비교')
        return self.total > s.total
    
    def __eq__(self,s):
        return self.name == s.name and self.total == s.total


s1 = Student('홍길동',100)
s2 = Student('유관순',90)
s3 = Student('이순신',95)
s4 = Student('홍길동',100)

print(s1) # str 함수 우선 호출
print(s1+s2) # 클래스를 더하기 할 때, add 함수 호출

print(s1>s2) # total 값으로 리턴 받아 비교 원래는 비교 불가능.
print(s2>s3) 

print(s1==s4)
print(s1==s2)


a_list = [10,20,30,40]
b_list = [2,3,4,5]
# print(a_list>b_list)