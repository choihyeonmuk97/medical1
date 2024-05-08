print("안녕하세요 제 이름은 홍길동입니다.")
print('저는 21살입니다.')

# 홍길동 대신 이순신으로 21대신 30으로 바꾸고 싶은 경우
print("안녕하세요 제 이름은 이순신입니다.")
print('저는 30살입니다.')

print('안녕하세요 제 이름은','홍길동','입니다.')
print('저는',21,'살 입니다.')

name = '이순신'
age = 30
print('안녕하세요 제 이름은',name,'입니다.')
print('저는',age,'살 입니다')

# 변수 입력
str1 = "hello"
print(str1)
var1 = 2
print(var1)
str2 = 'world'
print(str1, str2)
print(str1+str2)
print(str1+" "+str2)

var4 = 100
var3 = var4 # var4 = 100이라서 var3은 100이 됨
var2 = var3 # var2 = 100
var1 = var2 # var1 = 100
print('var1 :' , var1)
var4 = 200
print('var4 :', var4)
print('var1 :', var1)

# 변수를 이용하기
# 변수명 : fruit
# '포도', '딸기', '수박'순으로 입력
# 출력문장 > 나는 포도를 좋아합니다.

fruit1 = '포도'
fruit2 = '딸기'
fruit3 = '수박'

print('나는',fruit1+'를 좋아합니다.')
print('나는',fruit2+'를 좋아합니다.')
print('나는',fruit3+'을 좋아합니다.')

print('{} {}{}'.format('나는',fruit1,'를 좋아합니다.'))
print('%s'%'나는',fruit2+'를 좋아합니다.')

# 변수명 : city
# 출력문장 > 나는 서울시에 살고 있습니다.

city = '인천시'
print('나는',city+'에 살고 있습니다.')
print('{} {}{}'.format('나는',city,'에 살고 있습니다.'))

# 변수명 : animal
# 출력문장 > (판다)가 제일 좋아요

animal = '판다'
print('%s'%animal+'가 제일 좋아요')
print('{}{}'.format(animal,'가 제일 좋아요'))
print(animal+'가 제일 좋아요')

