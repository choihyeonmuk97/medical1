fruits = ['사과','복숭아','딸기','포도','배']
# 한라봉을 추가하고 싶을 때
print('추가전 리스트 : ', fruits)
# 리스트에 요소 추가하기
fruits.append('한라봉')
print('추가전 리스트 : ', fruits)

if '딸기' in fruits:
    print('딸기가 있습니다.')
else :
    print('딸기가 없습니다.')

temp = []
print(temp)
temp.append(1)
print(temp)
temp.append(2)
print(temp)
temp.append('홍길동')
print(temp)

# 과일 리스트에 '체리' 추가
fruits.append('체리')
print(fruits)

# 리스트에서 제거 : .remove
fruits.remove('사과')
print(fruits)

# 변수
a = 2
b = 3
c = a+b
print('{}+{}={}'.format(a,b,c))

l1 = [1,2,3,4,5] # 리스트를 사용해서 2+3=5 출력
print('{}+{}={}'.format(l1[1],l1[2],l1[4]))

# l1에 있는 숫자들의 합을 구해보세요
result = l1[0]+l1[1]+l1[2]+l1[3]+l1[4]
print(result)


