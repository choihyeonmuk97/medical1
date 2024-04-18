# 동전 교환 프로그램

money = 1270
money = input('교환할 돈을 입력하세요 >> ')
money = int(money)
c500, c100, c50, c10 = 0,0,0,0
#500원 동전개수 
c500 = money//500
c100 = (money%500)//100
c50 = ((money%500)%100)//50
c10 = (((money%500)%100)%50)//10

print('투입금액 >> {}'.format(money))
print('500원의 개수 : {}'.format(c500))
print('100원의 개수 : {}'.format(c100))
print('50원의 개수 : {}'.format(c50))
print('10원의 개수 : {}'.format(c10))


