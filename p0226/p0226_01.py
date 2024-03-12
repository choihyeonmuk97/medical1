# 변수
a = False # boolean
b = 123
c = 1.3456
d = '문자'
e = [1,2,3]

# 출력
print('hello')
print(123*456)
str1 = 'hi'
print(str1)
print('{0:s} : {1:d} / {2:d} = {3:f}'.format('수식',7,3,7/3))
print('{} : {} / {} = {:.3f}'.format('수식',7,3,7/3)) # 중괄호 안 생략 가능

# 관계연산자 : 조건문, 반복문
# >, >=, <, <=, ==, !=
print (3>5) # False
n1 = 10
n2 = 8
print(n1 != n2) # True

# 논리연산자 : and : 모두 T -> T, or : 하나라도 T -> T, not : T -> F, F -> T
a , b = 10 , 9
print('and 연산자')
if a == 10 and b == 9:
    print('참 and 참 = 참')
else :
    print('참 and 참 = 거짓')

if a == 10 and b != 9:
    print('참 and 거짓 = 참')
else:
    print('참 and 거짓 = 참')

# 조건문 if
# if - elif - else
print("-"*25)

# 실행문을 비우고 싶을 때 : pass
if 1 == 1:
    pass
else:
    print('else 실행')
    
print("-"*25)

# 중첩 if : if 안에 if 사용
num = 5 
if num >= 0:
    if num == 0:
        print('0')
    else:
        print('양수')
else:
    print('음수')
