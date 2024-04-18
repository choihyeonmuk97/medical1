# Car 클래스 선언
# carCount 클래스 변수
# carNO에 carCount 숫자를 이용하여 carNo 넣으세요
# 변수 : carNo, color='white', door=5, tire=4, speed
# up_speed 함수 호출 10씩 증가
# down_speed -> -10씩 감소

class Car:
    carCount = 0 # 클래스
    carNo = 0 # 인스턴스
    
    def __init__(self,color='',door=5,tire=4,speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        
        Car.carCount += 1
        self.carNo = Car.carCount

    def up_speed(self,s=10):
        self.speed += s
        
    def down_speed(self,s=10):
        self.speed -= s    
            
    def c_print(self):
        print('번호 :',self.carNo,'색상 :',self.color,'도어 :',self.door,
              '타이어 :',self.tire,'속도 :',self.speed,sep=' ')

car_list = []
# c1 - 1,white,5,4,0 -> speed 30이 되도록
c1 = Car('white',5,4,0)
c1.up_speed() 
c1.up_speed() 
c1.up_speed() 
c1.c_print()

# c2 - 2,red,5,4,0 -> speed 100
c2 = Car('red',5,4,0)
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.c_print()

# c3 - 3,silver,5,4,0 -> speed 70
c3 = Car('silver',5,4,0)
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.c_print()

# car_list에 추가하고
# car_list.append(c1.c_print)
# car_list.append(c2.c_print)
# car_list.append(c3.c_print)
car_list = [c1,c2,c3]

# car_list를 모두 출력
for i in range(3):
    c = car_list[i]
    print(c.carNo,c.color,c.door,c.tire,c.speed)

