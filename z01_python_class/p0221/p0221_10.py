# 변수 3개를 만들어서 name, city, fruit

name = '홍길동'
print('저의 이름은',name+'입니다.')
print('저의 이름은 %s입니다.'%name)
print('저의 이름은 {}입니다.'.format(name))

city = '인천'
print('저는 %s시에서 태어났습니다.'%city)
print('저는',city+'시에서 태어났습니다.')
print('저는 {}시에서 태어났습니다.'.format(city))

fruit = '딸기'
print('저는 %s를 좋아합니다.'%fruit)
print('저는',fruit+'를 좋아합니다.')
print('저는 {}를 좋아합니다.'.format(fruit))

# input으로 출력하기

a = input('이름을 입력하세요')
b = input('도시명을 입력하세요')
c = input('단어를 입력하세요')

print('저의 이름은 %s입니다.'%a)
print('저는 %s시에서 태어났습니다.'%b)
print('저는 %s를 좋아합니다.'%c)

