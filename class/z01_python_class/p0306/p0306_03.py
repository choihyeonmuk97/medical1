import operator

# numbers에 있는 숫자들이 몇번 나왔는지 딕셔너리로 출력
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

for num in numbers:
    if num not in counter:
        counter[num] = 0
    counter[num] += 1

print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0))) # revers=True
print(sorted(counter.items(),key=operator.itemgetter(1))) 


array = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E"]
cnt = {}
for a in array:
    if a not in cnt:
        cnt[a] = 0
    cnt[a] += 1
    
print(cnt)
print(sorted(cnt.items(),key=operator.itemgetter(0))) # revers=True

