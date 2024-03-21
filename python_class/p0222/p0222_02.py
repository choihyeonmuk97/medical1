# 변수 사용
# bool, int, float, str
# 변수는 대소문자를 구분한다. (대문자는 주로 클래스에서 사용)
myVar = 10
MyVar = 20
# 변수에서 언더바 사용 가능, 숫자로 시작하면 안됨
number1 = 10
num_1 = 20

# 변수는 예약어(언어)를 사용할 수 없음 :print,if,True,False 등등

# 변수는 마지막으로 입력된 값을 저장함

a = 1
b = 2
a,b = 1,2 # 한 줄로 축약 가능

# 입력 받기 input()

name = input("이름을 입력하세요 ?? ")
print('나의 이름은',name+'입니다.')

# input은 문자열로 인식함
# age = input('나이 ?? ')
# print('나는 내년에 {}살 입니다.'.format(age+1)) -> error 문자로 인식함
# 숫자로 유형변경하는 방법
# 1. age = int(input('나이??'))
# 2. age = int(age)
# 3. print('나는 내년에 {}살 입니다.'.format(int(age)+1)

#숫자 하나를 입력해서 구구단을? (x3까지)

a = int(input('숫자'))*1
b = int(a)*2
c = int(a)*3

print('{}\n{}\n{}'.format(a,b,c))

print('2 * 1 =',a)
print('2 * 2 =',b)
print('2 * 3 =',c)





