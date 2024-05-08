# 변수 : bool, int, float, string
# input() 문자열로 입력 받음

'''
if - elif-else
if 조건문 1:
    실행문1
elif 조건문 2:
    실행문2
else:
    실행문3

elif, else 생략 가능, if 조건을 건너 뛸때 pass 사용
'''

n = 1 # int(input('숫자 > '))
if n >= 0:
    print('양수')
    if n % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('음수')   

'''
반복문
for 변수 in 반복가능한데이터 :
    실행문
'''
# 순차적으로 커질때는 range를 사용
for i in range(0,3,1): # range(시작값, 끝값+1, 증감값)
    print('hi')
    
for i in range(5): # i = 0 1 2 3 4
    print(1)
    
for i in range(1,11):
    print(i)
print('-'*35)

a = 10
b = 'hi'
# a,b를 5번 반복
for i in range(5): 
    print(i)
    a = a + 1 # a += 1
    print(a)
    print(b)  

# 입력 : 이름, 점수 (5명)
# 60점 이상이면 합격, 미만이면 불합격

for i in range(5):
    name = input('이름을 입력하세요 > ')
    score = int(input('점수를 입력하세요 > '))
    if score >= 60:
        print('{}님 합격입니다.'.format(name))
    else:
        print('{}님 불합격입니다.'.format(name))
 
