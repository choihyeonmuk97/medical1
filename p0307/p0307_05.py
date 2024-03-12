import random

# random.random()
print(random.random()) # 0-1 사이의 랜덤한 실수 생성

print(random.randint(0,44)) # 0~3 랜덤한 정수 생성

print(random.randrange(0,3)) # 0~2 랜덤한 숫자(정수?) 생성

list = [1,2,3,4,5,6,7]
print(list) 
random.shuffle(list) # 리스트를 랜덤으로 섞기
print(list) 

print(random.choice(list)) # 리스트에서 1개를 무작위로 추출

print(random.sample(list,4)) # 리스트에서 해당되는 개수만큼 랜덤으로 추출


w_list = ['토마토','바나나','사과','배','수박','메론','복숭아']

print(random.sample(w_list,3))


