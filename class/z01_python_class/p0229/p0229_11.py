fruits = ['딸기','사과','자몽','포도','수박','자몽']

# 만약에 자몽을 삭제
# 리스트명.remove('요소명') -> 앞쪽 요소 부터 삭제
# del(리스트명[번호]) -> 정확한 위치의 요소를 삭제하고 싶을때 
del(fruits[5])
print(fruits)

for i, f in enumerate(fruits): # enumerate : index 표현
    print('{}는 {}번째에 있습니다.'.format(f,i))

