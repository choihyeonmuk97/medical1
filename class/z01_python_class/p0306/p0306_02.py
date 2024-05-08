import operator

fruits = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {} # 딕셔너리 생성

for f in fruits:
    if f not in counter:
        counter[f] = 0 # 딕셔너리 키가 없을 경우 추가
    counter[f] += 1 # 키의 value 값 1 증가

print(counter) 

# 딕셔너리 정렬 key값 순으로 정렬 (순차)
print(sorted(counter.items(),key=operator.itemgetter(0)))

# 역순 정렬
print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))

# value 순으로 정렬 (순차)
print(sorted(counter.items(),key=operator.itemgetter(1)))

# 역순 정렬
print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))