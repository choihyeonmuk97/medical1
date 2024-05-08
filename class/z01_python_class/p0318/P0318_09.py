class Lotto:
    number = 0
    shape = 'circle'
    
    def __init__(self,number):
        self.number = number

# 1~45 까지 숫자 생성

l_list = []

for i in range(45):
    l = Lotto(i+1)
    l_list.append(l.number)

print(l_list)