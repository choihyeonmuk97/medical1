# 얕은 복사, 깊은 복사
# 변수
a = 1
b = 2
c = a
print('변수 :',a,b,c)
print(id(a))
print(id(b))
print(id(c))

a = 8
print('변수 :',a,b,c)
print(id(a))
print(id(b))
print(id(c))

# 변수의 값이 변하게 되면 변한 변수는 다른 메모리 주소로 옮김
# 기존과 메모리 값이 바뀜을 확인 할 수 있다.

# list의 경우
# 여러가지 데이터가 들어갈 수 있음
# 주소 값이 할당이 된다. (고정)
# 단순 복사는 주소값이 복사가 된다.

aa = [1]
bb = [2]
cc = aa
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))
aa[0] = 10
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))

# 단순 복사가 되었기 때문에 aa의 값을 변경하면 cc 값이 같이 변경 (얕은복사)

# 깊은 복사 
# 독립성 유지
import copy 
aa = [1]
bb = [2]
cc = copy.deepcopy(aa)
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))
aa[0] = 10
print(aa,bb,cc)
print(id(aa))
print(id(bb))
print(id(cc))



