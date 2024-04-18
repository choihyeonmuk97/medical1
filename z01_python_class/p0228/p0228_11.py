num = [100,200,300,400]
# for 문을 사용해서 하나씩 출력해보세요
for i in range(len(num)):
    print(num[i],end=' ')
print()

for i in num:
    print(i,end=' ')
print()

numlist = [[1,2],[3,4],[5,6]]
for n in numlist:
    for a in n:
        print(a,end=' ')
    print()
    
for i in range(len(numlist)):
    for j in range(len(numlist[i])):
        print(numlist[i][j],end=' ')
        
print() 


f=[['딸기',100,1000],['수박,100,500'],['사과',100,1200],['귤',100,300]]

#요소 하나하나       
for a in f:
    for b in a:
        print(b,end=' ')
    print()

for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j],end=' ')
    print()

score = [90,80,70,100,95,85,100]
total = []
# 점수의 총 합
sum1 = 0
for i in range(len(score)):
    sum1 = sum1 + score[i]
# print(sum1)
total.append(sum1)
print(total)

# sum2 = 0
# for n in score:     ->  리스트명으로 했을때
#     sum2 += n         
# total.append(sum2)
# print(total)