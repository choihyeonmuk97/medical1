numL = []

# 0~5까지 넣어보세요
numL.append(0)
numL.append(1)
numL.append(2)
numL.append(3)
numL.append(4)
numL.append(5)
print(numL)

# for을 이용하여 0 ~ 5 까지 숫자 넣기
num = []
for i in range(6):
    num.append(i)
    
print('num[] = ',num)

aa = [1,2,3,4]
# index
for i in aa :
    print(i)
    
for i in range(0,4):
    print(aa[i])

f = ['사과','복숭아','딸기','포도','자몽']
for i in f:
    print(i)
for i in range(len(f)):
    print(f[i])
    
c = ['미국','영국','호주','캐나다','일본','중국']
# for
for i in c:
    print(i)
for i in range(len(c)):
    print(c[i])
        
# 1에서 100까지 들어가는 numL = []를 만들고 출력
numL = []
for i in range(100):
    numL.append(i+1)
    
print(numL)

for i in range(100):
    print(numL[i])

# 반복문 안에 if문 사용
for i in range(10):
    print(i) # 0~9까지 출력
    if i == 9:
        print('9입니다.')
        
lan = ['영어','스페인어','일본어','중국어']
for i in lan:
    if i == '영어':
        print('영어입니다.')
    else :
        print('다른 언어입니다')
        
# 2의 배수만 출력 (1~100 사이)
for i in range(100):
    if (i+1) % 2 == 0:
        print(i+1,end =' ')
print()
for i in range(2,102,2):
    print(i,end = ' ')
print()
# 7의 배수만 출력
for i in range(100):
    if (i+1) % 7 == 0:
        print(i+1,end=' ')
print()
for i in range(7,101,7):
    print(i, end=' ')
print()
    
aa = [100,90,86,79,72,52,98,94]
# 80점 이상만 합격 (합격이 5번 출력)
for i in aa:
    if i >= 80:
        print('합격')

f = ['사과','복숭아','딸기','포도','자몽']
# 딸기가 있으면 딸기, 다른과일은 다른과일
for i in f:
    if i == '딸기':
        print('딸기')
    elif i == '사과':
        print('사과')
    elif i == '복숭아':
        print('복숭아')
    elif i == '포도':
        print('포도')
    elif i == '자몽':
        print('자몽')
    else:
        print('다른과일입니다')
        
num = [1,2,5,7,9,10,23,43]
# 짝수면 짝수 홀수면 홀수
for i in num:
    if i % 2 == 0:
        print(i,'짝수', end=' ')
    elif i % 2 != 0:
        print(i,'홀수', end=' ')  
print()

for i in range(len(num)):
    # print(num[i])
    if num[i] % 2 == 0:
        print(num[i],'짝수')
    else :
        print(num[i],'홀수')
      
