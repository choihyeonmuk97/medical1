class Car:
    car_name = ''
    color = ''
    door = 0
    length = 0
    width = 0
    speed = 0

    def up_speed(self,s): # 클래스 내의 함수에서는 self를 사용해야함
        self.speed += s

c1 = Car()
c1.car_name = 'The New Avante'
c1.color = 'white'
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60) # 현재 속도에서 60을 더함
c1.up_speed(40) # speed = 100
# c1.speed = 50 # speed = 50

# 영희 차 1대 생산해서, 색 : green, 나머지 동일, 속도는 100
c2 = Car()
c2.car_name = 'The New Avante'
c2.color = 'white'
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.up_speed(100) # 현재 속도에서 60을 더함

# # 반장님 - 그랜져, 화이트펄, 2500, 1400, 150
c3 = Car()
c3.car_name = 'The All New Grandeur '
c3.color = 'white pearl'
c3.door = 5
c3.length = 2500
c3.width = 1400
c3.up_speed(140) # 현재 속도에서 60을 더함

print('철수 차 :',c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
print('영희 차 :',c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
print('반장님 차 :',c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)

