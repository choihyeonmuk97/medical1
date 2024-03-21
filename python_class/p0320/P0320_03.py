class Car:
    value = '부모의 값 1'
    
    def car_func(self):
        print('부모의 값을 출력합니다.')
        
class Amb(Car):
    value = '자식의 값 2'
    def car_func(self):
        print('[자식클래스에서 부모의 값을 출력]')
        super().car_func() # 부모의 값을 출력할 때 super()
        print('부모 클래스의 값 :',super().value)
        print('자식 클래스의 값 :',self.value)


a1 = Amb()
a1.car_func()