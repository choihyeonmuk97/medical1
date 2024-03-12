# 반복문 while
''' 
while 조건식 : 참일때만!!!!!!!
    실행할 문장

변수 = 시작값 ex) i = 0
while 변수 < 끝값 : 이 조건이 참일 때
    반복구문
    변수 = 변수 + 증가값 # i = i + 1

'''

# for 
for i in range(3):
    print('for : 안녕하세요')

# while
i = 0
while i < 3:
    print('while : 안녕하세요')
    i = i + 1

# for 0~10
for i in range(0,11):
    print(i,end=' ')
print()

# while 0~10 
i = 0
while i < 11:
    print(i,end=' ')
    i = i + 1
print()

# while 
# 1~10 사이의 3의 배수를 출력
i = 0
while i < 10:
    i = i + 1
    if i % 3 == 0 :
        print(i, end=' ')
print()

# 1~100 사이 홀수
i = 0
while i < 100:
    i = i + 1
    if i % 2 == 1:
        print(i,end=' ')
print()

# 1~100 까지 합
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum,end='')
print()

# while 조건문이 참인경우 반복
# 때문에 while True는 무조건 참이기 때문에 무한반복!!
# 이땐 crtl + c를 눌러 강제 종료

# while을 사용할 때 조건문을 잘 만드는게 중요함!

# break,continue
# break 반복문을 빠져나와 다음단계 수행
n = 0
while n < 100 :
    print(n, end=' ')
    if n == 4:
        break
    n = n + 1
    print('---------')
print()

# breakletter = input('중단할 문자를 입력하세요 > ')
# for letter in 'python':
#     if letter == breakletter:
#         break
#     print(letter)

while True:
    n = input('숫자 > ')
    print(n)
    if n == '0':
        print('종료')
        break
print('종료되었습니다')

        