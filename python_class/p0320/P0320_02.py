class Car:
    count = 0
    
    def __init__(self,color='white',door=5,tire=4,speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed

    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed -= 10
        
    def stop_speed(self):
        self.speed -= 10
    
    
# 클래스 상속 / 부모 -> Car
class Amb_car(Car):
    # Car클래스의 모든 것을 가져옴        
    def up_speed(self): # 자식 클래스에서 오버라이딩 : 재 정의
        self.speed += 20
        
    def up_speed2(self): # 기존 부모의 함수를 다시 호출
        return super().up_speed() # 부모의 요소를 가져올때 super()
     
    def siren(self):
        print("싸이렌이 울림")


class FireTruck(Car):
       
    def water(self):
        print('분수')


a1 = Amb_car('white')
print('현재속도 :',a1.speed)
a1.up_speed() # 자식의 오버라이딩 된 함수 호출
print('현재속도 :',a1.speed)
a1.up_speed2()
print('현재속도 :',a1.speed)
a1.stop_speed()
print('현재속도 :',a1.speed)
print(a1.color)