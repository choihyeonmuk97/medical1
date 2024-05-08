class Card:
    kind = ''
    number =''
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number

# 클래스 이용하여 52장 카드 생성
kind = ['SPADE','DIAMOND','HEART','CLOVER']
number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
c_list = []

for i in range(4):
    for j in range(13):
        c = Card(kind[i],number[j])
        c_list.append(c)
    
for i in range(52):
    c = c_list[i]
    print(c.kind,c.number)

# 클래스를 쓰는 이유는 보안상의 이유 때문 !!

# kind = ['SPADE','DIAMOND','HEART','CLOVER']
# number = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
# c_list = []

# for i in range(4):
#     for j in range(13):
#         c = [kind[i],number[j]]
#         c_list.append(c)

# for i in range(4):
#     for j in range(13):
#         print(kind[i],number[j])












# c1 = Card('spade','1')
# c1.number='5'
# print(c1.kind,c1.number)

# c2 = Card('heart','A')
# # print(c2.kind,c2.number)
# c2.kind = 'diamond'
# print(c2.kind,c2.number)