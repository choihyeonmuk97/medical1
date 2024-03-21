# 반복문
# 안녕하세요 다섯번
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
'''
for 변수 in 반복가능한데이터 :
    수행할 문장
'''
# 순차적으로 커질 때 range 사용
for i in range(0,5,1): # range(시작값, 끝값+1, 증가값)
    print(i,'안녕')      # i 가 0,1,2,3,4

for i in range(0,3): # 증가값이 1인경우 생략가능    
    print(i,'hi')

for i in range(4): # n번 반복할 경우 range(n)을 사용할 수 있음
    print('hello')

for _ in range(2): # i를 사용하지 않을 경우 _ 사용할 수 있음
    print('반갑습니다')

# for i in range(1): # 5번 반복
#     num = int(input('숫자를 입력하세요 > '))
#     print('입력하신 숫자는 : {}'.format(num))

# i, j 카운터 변수 
# 카운터 변수는 반복 실행 될때마다 현재 실행 횟수에 해당하는 숫자가 들어감
# 가장 처음은 실행한 적이 없으므로 0이 된다.

for i in range(3):
    print(i) # 0,1,2

str1 = '안녕하세요'
for i in str1:
    print(i)

print('-'*35)
# 1~15 까지
for i in range(1,16,1):
    print(i)

# 10을 4번 반복해서
for i in range(4):
    print(10)

# helloworld를 6번 반복
for i in range(6):
    print('helloworld') # 출력값에 i를 붙일경우 +1을하면 1 hello ~ 6 hello

# 1~100 사이의 2의 배수
for i in range(2,100,2):
    print(i, end=" ") # end =  줄 바꿈 없이 출력

print()
# 1~100 5의 배수
for i in range(5,100,5):
    print(i,end=' ')



