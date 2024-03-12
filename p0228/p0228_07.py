from random import *

n1 = [0,1,2,3,4,5]
# 0의 위치와 3의 위치를 바꾸고 싶다
n1[0],n1[3]=n1[3],n1[0]
print(n1)
# 2 <-> 5
n1[2],n1[5]=n1[5],n1[2]
print(n1)

con = ['미국','영국','일본','중국','스페인']
# 영 <-> 중
con[1],con[3] = con[3],con[1]
print(con)

n1 = [1,2,3,4,5,6,7,8,9,10]

for i in range(3):
    tmp = randint(0,9)
    n1[0],n1[tmp] = n1[tmp],n1[0]
    print(tmp)
    print(n1)
