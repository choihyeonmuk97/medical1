# 1. 숫자 두개를 입력받아서 나누기값, 몫값, 나머지값 출력
n1 = int(input('첫번째 숫자를 입력하세요 >> '))
n2 = int(input('두번째 숫자를 입력하세요 >> '))

res1 = n1/n2
res2 = n1//n2
res3 = n1%n2

print('두 수의 나눈 값은 {:.0f}입니다.'.format(res1))
print('나눗셈을 한 몫값은 {}입니다.'.format(res2))
print('나누고 난 나머지 값은 {}입니다.'.format(res3))

# 2. 3개의 수의 합을 구하세요
s1, s2, s3 = '100','100.123','99.9'

print(int(s1)+float(s2)+float(s3))
print('3개의 숫자의 합은 {:.2f}입니다.'.format(int(s1)+float(s2)+float(s3)))


