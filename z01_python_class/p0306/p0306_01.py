import operator

fruits = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {} # 딕셔너리 생성

# 딕셔너리 추가

counter["복숭아"] = 5 # 추가
counter["바나나"] = 4 # 추가
counter["바나나"] = 1 # 수정

# 딕셔너리에 없는 키값을 출력하면 에러가 나기 때문에 확인을 해야함
if "딸기" not in counter:
    counter["딸기"] = 0 # 키를 생성
else:
    print(counter["딸기"]) # 키의 value값을 출력

# 딕셔너리 삭제
del counter["복숭아"]

print(counter)

print(counter.keys()) # class type
print(counter.values())
print(counter.items())

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list)) # a_list.sort() 와 같음


