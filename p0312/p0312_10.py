import random

card_list = []
shape_list = ['SPADE','DIAMOND','HEART','CLOVER']
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
    # print(num_list)
num_list[0] = 'A'
num_list[10] = 'J'
num_list[11] = 'Q'
num_list[12] = 'K'

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류 -> shapelist
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K  13장 numlist
# 카드 총 갯수 : 52장 cardlist

card_list = [[0]*2 for i in range(52)] 
cnt = 0
for i in shape_list:
    for j in range(13):
       card_list[cnt] = {"shape":i,"num":num_list[j]} 
       cnt += 1 
    print(card_list)

def card_creat():
    pass

def card_shuffle():
    random.shuffle(card_list)

def card_share():
    pass

def card_print():
    pass

while True:
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드5장 나눠주기')
    print('4. 카드5장 확인하기')
    print('0. 종료')
    print('-'*40)
    choice = int(input('원하는 번호를 입력하세요. > '))

    if choice == 1:
        card_creat()
        
    elif choice == 2:
        card_shuffle()
        
    elif choice == 3:
        card_share()

    elif choice == 4:
        card_print()

    elif choice == 0:
        print('프로그램 종료')
        break
    
    