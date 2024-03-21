a = [1,2,3,4,5]
b = a # 얕은 복사
c = [*a] # 전개연산자 : 복사할 때 사용

a[1] = 20 # a의 데이터 값을 변경
print(b) # [1,20,3,4,5] -> b 리스트도 같이 바뀜
print(c) # c 리스트는 변경이 안됨

product = ['새우깡','90g',1200,3]

print('상품명 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년'.
      format(product[0],product[1],product[2],product[3]))
# 같음
print('상품명 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년'
      .format(*product))

