# 변수
# int 형
# 10진법 : 정수 1,2,3,.... -1,-2,-3..
num1 = 10
print(num1)
num2 = -100
print(num2)

# 2진법 : 0b로 시작함
num3 = 0b101010
print(num3)
# 32+8+2

# 8진법 : 0o로 시작함
num4 = 0o52 #40+2 (5x8^1 + 2x8^0)
print(num4)

# 16진법 : 0x
# 1,2,3,4,5,6,7,8,9,a,b,c,d,e,f 의 수로 표현됨 
num5 = 0x2a
print(num5)

# float 형 : 실수(소수점을 포함하고 있는 수)
num6 = 3.14
print(num6)
print('%f'%num6)
num7 = 2*3.14*5
print(num7)

# complex 형 : 실수 + 허수
# 3+2i -> 파이썬에서는 i 대신 j를 사용한다
comp1 = 3+4j
print(comp1)
print(comp1.real)
print(comp1.imag)

# boolean 형 : True or False
bool1 = True
bool2 = False
print('bool1 :',bool1)
print('bool2 :',bool2)
bool3 = (1==2)
print(bool3)
bool4 = (0x2a == 42)
print('bool4 :',bool4)

# String 형
str1 = '안녕하세요'
str2 = 'hello'
print(str1)
print(str2)

# 그 외에 lisr, tuple, dict, set 등이 있음

