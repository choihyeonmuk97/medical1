import random
#from random import *

# shape_list = ['SPADE','DIAMOND','HEART','CLOVER']



num_list = [0]*13
for i in range(13):
    num_list[i] = i+1

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# 랜덤으로 2개 숫자를 뽑아서 출력

ran_num = random.sample(num_list,k=2)
print(ran_num)

# 랜덤숫자 : ? -> ?번방에 있습니다.
# 랜덤숫자 : ? -> ?번방에 있습니다.
print(f'랜덤숫자 : {ran_num[0]} -> {num_list[ran_num[0]-1]}방에 있습니다.')
print(f'랜덤숫자 : {ran_num[1]} -> {num_list[ran_num[1]-1]}방에 있습니다.')

# 큰수 : ?, 작은수 : ?
if ran_num[0] > ran_num[1]:
    print(f'큰 수 : {ran_num[0]}, 작은 수 : {ran_num[1]}')
else:
    print(f'큰 수 : {ran_num[1]}, 작은 수 : {ran_num[0]}')
    




# print(num_list)
# num_list[0] = 'A'
# num_list[10] = 'J'
# num_list[11] = 'Q'
# num_list[12] = 'K'