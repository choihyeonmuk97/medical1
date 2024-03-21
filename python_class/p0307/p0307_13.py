list = [1,2,3]
# alist = list -> 얕은 복사 (공간을 같이 씀(주소가 같다))
alist = [*list]   # 깊은 복사
alist = [list[:]]

list[0] = 100

print(alist)

a = 100
b = a
a = 10
print(b) # 100

