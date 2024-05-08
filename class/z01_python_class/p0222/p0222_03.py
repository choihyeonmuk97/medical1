#숫자 하나를 입력해서 구구단을? (x3까지)

a = int(input('숫자'))*1
b = int(a)*2
c = int(a)*3

print('{}\n{}\n{}'.format(a,b,c))

num = input('원하는 단을 입력하세요 >> ')
num = int(num)

print('{}*{}={}'.format(num,1,num*1))
print('{}*{}={}'.format(num,2,num*2))
print('{}*{}={}'.format(num,3,num*3))
