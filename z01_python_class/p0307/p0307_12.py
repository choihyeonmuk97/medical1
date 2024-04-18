# 공간을 만들어 놓고 for문 사용

list=[0]* 10
for i in range(10):
    list[i] = i+1
print(list)

# 컴프리헨션을 사용하여 리스트 생셩
list1 = [i+1 for i in range(10)]
print(list1)


