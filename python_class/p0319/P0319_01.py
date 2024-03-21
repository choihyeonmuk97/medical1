import random

class Card:
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
    
 
 # 52장 생성
 # spade, diamond, heart, clover
 # 1,2,3,4,5,6,7,8,9,10,11,12,13
kind_list = ['SPADE','DIAMOND','HEART','CLOVER']
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = [] 
ran_list = []

def random_one():
    num = random.randint(0,51)
    print('랜덤카드 1장 :',card_list[num].kind,card_list[num].number)

for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],num_list[j]))
        
for i in range(52):
    print('카드 :',card_list[i].kind,card_list[i].number)
    
# 랜덤으로 1장 뽑기
random_one()
print('-'*50)
# 중복이 되지 않게 랜덤으로 카드 5장 뽑기
ran_list.append(random_one)

if i not in ran_list:    
    for j in range(5):
        random_one()

print('-'*50)
# 1. 0~51 랜덤으로 섞은 후  순차적으로 뽑으면 됨
random.shuffle(card_list)
for i in range(5):
    print('랜덤카드 :',card_list[i].kind,card_list[i].number)

print('-'*50)
# 2. 5장을 랜덤으로 뽑기 (random.sample) 
ran_list = random.sample(card_list,5)
for i in ran_list:
    print('랜덤카드 :',i.kind,i.number)

# 3. 1장 뽑고 기존에 있는 카드와 비교해서 뽑기 
