# 클래스 : 사용자 정의 변수 - 함수도 포함
# 클래스의 첫글자는 대문자 사용
# 클래스 = 설계도
class Car:
    color = 'white'
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp


# 객체 선언을 할 때 마다 제품?이 한개씩 생산됨 => c1 != c2
c1 = Car() # 클래스 객체선언 -> Car 클래스에 있는 모든 변수를 사용.
print('색상 :',c1.color)
c1.color = 'red'
print('변경 후 색상 :',c1.color)

c2 = Car()
print('색상 :',c2.color)




