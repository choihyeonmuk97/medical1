class Car:
    car_name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0

    # 생성자
    def __init__(self,car_name='',color='',door=5,length=1000,width=1000,speed=0): 
        self.car_name = car_name
        self.color = color
        self.door = door
        self.length = length
        self.width = width
        self.speed = speed
        
    def up_speed(self,s): # 클래스 내의 함수에서는 self를 사용해야함
        self.speed += s

# 생성자를 사용한 객체(=인스턴스) 선언
c1 = Car('The New Avante','white',5,2000,1000,60) 
print('철수 차 :',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2 = Car('The New Avante','green',5,2000,1000,100)
print('영희 차 :',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

c3 = Car('The All New Grandeur','white pearl',5,2500,1400,150)
print('반장님 차 :',c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)


# ↓ 기본 변수?를 사용한 객체 선언 ↓
c4 = Car()
c4.car_name = 'The New Avante'
c4.color = 'white'
c4.door = 5
c4.length = 2000
c4.width = 1000
print('기본 :',c4.car_name,c4.color,c4.door,c4.length,c4.width,c4.speed)


# 영희 차 1대 생산해서, 색 : green, 나머지 동일, 속도는 100
# c2 = Car()
# c2.car_name = 'The New Avante'
# c2.color = 'white'
# c2.door = 5
# c2.length = 2000
# c2.width = 1000
# c2.up_speed(100) # 현재 속도에서 60을 더함

# # 반장님 - 그랜져, 화이트펄, 2500, 1400, 150
# c3 = Car()
# c3.car_name = 'The All New Grandeur '
# c3.color = 'white pearl'
# c3.door = 5
# c3.length = 2500
# c3.width = 1400
# c3.up_speed(150) # 현재 속도에서 60을 더함

# print('철수 차 :',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
# print('영희 차 :',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

