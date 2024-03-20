class Car:
    count = 0 # 클래스 변수 : 클래스 내 에서 공통적으로 사용됨
    
    def __init__(self,color='black',speed=0): # 생성자 안에 변수 선언 : 인스턴스 변수
        self.color = color 
        self.speed = speed
        # Car.count = 0

c1 = Car() # 객체(인스턴스) 선언
c1.color = 'white'
print(c1.color)
print(c1.speed)

Car.count = 10
print(c1.count)

c2 = Car()
c2.color = 'red'
print(c2.count)
Car.count = 200
print(c1.count)
print(c2.count)
c2.door = 4
print(c2.door) # 찍힌다 가급적 자제


