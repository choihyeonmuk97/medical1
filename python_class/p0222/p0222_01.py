# 변수, 함수 (21일 복습)

a = 1 # 변수
# a() # 함수 (괄호가 들어감)
# print() 파이썬에서 기본적으로 제공

print('hello world') # 문자 출력
print(20) # 숫자
print(100+200) # 사칙연산 가능
print('10',20) # 따옴표가 들어가면 문자열
# print('10'+10) -> Error : + 는 같은 타입만 연결이 가능함
print(int('10')+10) # 가능 (강제로 유형(숫자로) 변경)
print('10'+str(10)) # 가능 (숫자 -> 문자열)

print('-'*20)

# %d 정수, %f 실수, %s 문자열
print('%d, %d'%(5,2))
print('%d, %.2f, %s'%(2,3.14,'abc'))

# 총 10자리 빈칸은 0으로 채우고 소수점은 3자리까지 출력
print('%010.3f'%25.05)

print('%10s'%'python')

# .format 함수 {글자 수 : 정수 및 실수표현 (%사용안함)}
print('{:.1f} {} {}'.format(758.12,50,'string'))

# 줄바꾸기 \n
print('파이썬 수업을 진행합니다.\n파이썬 기본편입니다.')
print('파이썬 수업을 진행합니다.\
    파이썬 기본편입니다.')
# 들여쓰기? \t
print('파이썬 수업을 진행합니다.\t파이썬 기본편입니다.')

# print의 ",'의 사용
print("산에 올라가면 '야호'라고 한다")
print('산에 올라가면 "야호"라고 한다')
print("산에 올라가면 \"야호\"라고 한다")



