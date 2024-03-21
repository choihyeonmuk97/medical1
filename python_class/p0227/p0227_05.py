# 0~20 사이 5의 배수로 이루어진 리스트
num = []
for i in range(0,21,5):
    # print(i)
    num.append(i)
print(num)

print()

num = []
for i in range(21):
    if i % 5 == 0:
        #print(i)
        num.append(i)
print(num)

lan = ['c','python','java','jquery','css']
# 1. 하나씩 출력해보기
for i in range(len(lan)):
    print(lan[i])

for i in lan:
    print(i)
  

# 2. 카운터 변수 i 사용해서 // format 생활화 //
#   1.c, 2.python ... 이런식으로 출력 (줄바꿈도)
for i in range(len(lan)):
    #print(i+1,'.',lan[i])
    print('{}. {}'.format(i+1,lan[i])) # = format(i,lan[i-1]) 

num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수 음수면 음수
# 1: 양수
# -1: 음수

for i in num:
    if i > 0 :
        print('{} : 양수'.format(i))
        # print('양수')
    else:
        print('{} : 음수'.format(i))

for i in range(len(num)):
    # print(num[i])
    if num[i] > 0 :
        print('{} : 양수'.format(num[i]))
    else:
        print('{} : 음수'.format(num[i]))

