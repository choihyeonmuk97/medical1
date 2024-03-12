foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","피자":"피클",
         "맥주":"땅콩","삼겹살":"상추"}

# key의 값을 출력
print(foods.keys())
for key in foods:
    print(key,end='  ')
print()

# value 값을 출력
print(foods.values())
for key in foods:
    print(foods[key],end='  ')
print()

# key:value 형태로 출력
print(foods) # items?
for key in foods:
    print()
