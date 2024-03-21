# 이번엔 지폐교환기

money = input('투입한 금액 : ')
money = int(money)

p50000 = money//50000
p10000 = (money%50000)//10000
p5000 = ((money%50000)%10000)//5000
p1000 = (((money%50000)%10000)%5000)//1000

print('투입금액 : {:,}'.format(money))
print('5만원 권 : {:,}장'.format(p50000))
print('1만원 권 : {}장'.format(p10000))
print('5천원 권 : {}장'.format(p5000))
print('1천원 권 : {}장'.format(p1000))
