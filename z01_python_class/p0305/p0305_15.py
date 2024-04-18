import operator

fruits = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']
counter = {}

for fruit in fruits:
    if fruit not in counter: # counter딕셔너리에 키 값이 없으면
        counter[fruit] = 0 # 딕셔너리에 추가
    counter[fruit] += 1 # 딕셔너리 1을 증가

# 많이 나온 숫자로 오름차순 정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))
print(fruits)

