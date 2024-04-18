# 리스트를 이용

fruits = ['딸기','사과','배','수박','귤']
# 귤을 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])

# 리스트에 요소 추가 .append
fruits.append('포도')
print(fruits)

# 리스트 요소 삭제 .remove
fruits.remove('딸기')
print(fruits)

# 요소 정해서 삭제 del()
del(fruits[3])
print(fruits)

if '한라봉' in fruits:
    print('있음')
else :
    print('없음') # 생략가능
    
for f in fruits:   # 요소 하나하나 출력
    print(f)

for i in range(len(fruits)):
    print(fruits[i])

num = [[10,20,30],[100,200,300],[1,2,3]]
for n in num:
    print(n)
    
for n in num: # 요소 in 요소
    for a in n:
        print(a)

for i in range(len(num)):
    print(num[i])
    
for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j])

# 리스트에 숫자 넣을 때 한줄로 표현 (이중, 중첩 다 가능)

a = [i for i in range(1,11)]
a = [0 for _ in range(10)]
print(a)

b = [i*j for i in range(1,3) for j in range(1,3)]
print(b)

c = [i for i in range(100) if i % 2 == 0]
print(c)

d = [i for i in range(1,11)]
e = [i+1 for i in d]
print(e)

name = ['홍길동','유관순','이순신','강감찬','김구']
# 출력 : 1. 홍길동 2. 유관순 3. 이순신 .........
for i in range(len(name)):
    print('{}. {}'.format(i+1,name[i]))

# 변수 1개 더 필요
n = 0
for i in name:
    n += 1
    print('{}. {}'.format(n,i))

# enumerate 함수
# index를 넣고 싶을때 사용
for i, n in enumerate(name): # index : 0부터 시작
    print('{}. {}'.format(i+1,n))

for i, n in enumerate(name, start=1): # index : 1부터 시작
    print('{}. {}'.format(i,n))



