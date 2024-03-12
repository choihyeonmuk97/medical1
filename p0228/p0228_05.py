# n1 부터 n2 까지의 합을 구하는데
# n1, n2비교해서 작은수를 n1에 넣기
n1 = int(input('숫자 > '))
n2 = int(input('숫자 > '))
sum = 0
if n1 > n2:  # -> 2.
    n1,n2 = n2,n1 # 숫자 바꾸기
    for i in range(n1,n2+1):   # -> 1.
        sum += i
print('{}부터 {}까지의 합은 {}입니다.'.format(n1,n2,sum))

odd_list = []
# 3. n1~n2까지의 홀수를 저장
for i in range(n1,n2+1):
    if i % 2 == 1:
        print(i,end=' ')
        odd_list.append(i)
print()
print(odd_list)

