print('Hello Python')
print('Hello!'*3)
print('혼자 공부하다 모르면 동영상 강의를 참고하세요!')

# 참 / 거짓
print( 5 > 10 ) # False
print( 5 < 10 ) # True
print(True)
print(False)
# print(true) 대소문자 구별
print(not True) # False
print(not (5>10)) # True
# '', "" 안에 있는 것은 문자열이다.
print(0*10) # 0
print('0'*10)

print(100) # 숫자
print('100') # 문자

print("100+100")
print(100+100)

print('숫자는 %d'%300) # %d : 정수
print('%d' % 200)
print('%d+%d=%d'%(2,3,2+3))
# 서로 (대응하는)짝이 맞지 않으면 오류를 발생시킨다.
# print('%d'%(100,200)) Error
# print('%d %d'%(10)) Error

print('%d*%d=%d'%(2,1,2))
print('%d+%d=%d'%(2+3,1+2,8))

# 깔끔한 출력
print('%d'%123)
print('%7d'%123) # 7자리 숫자를 보여줌. 빈 공백으로 채움
print('%05d'%123) # 5자리 숫자, 빈 공백은 0으로 채움

# %f : 실수
print('%d'%123.45)
print('%f'%123.45)

print('%7.1f'%123.45) # 소숫점을 포함해서 총 7자리 출력, 소숫점 이하 반올림
print('%07.3f'%123.45)

print('%f'%12.3456)
print('%.2f'%12.3456)

# 문자열은 %s를 사용
print('%s'%'반갑습니다')

# 문자(한 개)는 %c  (잘 사용하지 않음)
print('%c'%'a')
print('%s'%'a') 

print('%.2f'%758.12345678)

print('%010.2f'%25.05)

print('%d'%150.15) # 정수
print('%f'%150.15) # 실수
print('%s'%'150.15') # 문자열

print('%s'% "*"*10)
print('*'*10)

