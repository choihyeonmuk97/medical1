class Car:
    
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed # 캡슐화(접근 제한) : class 내부에서만 접근이 가능하게 함
    
    def up_speed(self,smartKey):
        if smartKey == '0x1100':
            self.__speed += 10
        else:
            print('스마트키가 없습니다.')
        
    def down_speed(self):
        self.__speed -= 10

    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed += speed
    
    
c1 = Car('white',5,4,0)
c1.up_speed('0x1100')
c1.up_speed('0x1111')
c1.set_speed(500)

print(c1.get_speed()) # 함수 외에는 클래스 변수로의 직접적인 접근을 막음