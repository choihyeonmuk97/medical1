class Card: # 4개의 변수 : kind, number, width, height
    width = 0 # 클래스 변수 : 모든 클래스에서 공통으로 사용하는 변수
    height = 0 # 클래스 변수

    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200


# 52장의 카드 생성
shape = ['SPADE','DIAMOND','HEART','CLOVER']
number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card_list = []

for i in range(4):
    for j in range(13):
        c = Card(shape[i],number[j]) # 객체 선언
        card_list.append(c)

for i in range(52):
    c = card_list[i] # Card 객체
    print(c.kind,c.number)


card_list = []
for i in range(13):
    card_list.append(Card('spade',i+1))
    
# card_list.append(Card("spade",'A'))
# card_list.append(Card("spade",'2'))
# card_list.append(Card("spade",'3'))
# card_list.append(Card("spade",'4'))
#...
# card_list.append(Card("spade",'10'))
# card_list.append(Card("spade",'J'))
# card_list.append(Card("spade",'Q'))
# card_list.append(Card("spade",'K'))

print('리스트 개수 :',len(card_list))

for i in range(13):
    print('리스트 :',card_list[i].kind,card_list[i].number)

# print('리스트 :',card_list[0].kind,card_list[0].number)
# ...
# print('리스트 :',card_list[12].kind,card_list[12].number)