import random

#from random import *

print(random.random())  # 0.00000...~0.999999... float 결과값 리턴

print(random.uniform(10,20)) # 10~20 사이 랜덤 float 결과값 리턴

print(random.randrange(1,3)) # 1~2 까지의 랜덤숫자 리턴

print(random.randint(1,10)) # 범위 내에서 랜덤 int(정수)를 선택

print(random.choice([1,2,3,4,5])) # 리스트 내에서 1개 랜덤으로 선택

print(random.sample([1,2,3,4,5],k=3)) # 리스트 내에서 n개 랜덤으로 선택

a_list = [1,2,3,4,5]
random.shuffle(a_list) # 리스트의 요소를 랜덤으로 섞어서 저장 (파괴)
print(a_list)



# import math

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))

