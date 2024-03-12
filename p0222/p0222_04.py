# 두 수를 입력받아서 사칙연산을 출력해보세용
# 변수 : n1, n2  
# int() -> 정수로 변환 / float(실수)

n1 = input('원하는 숫자를 입력하세요 >> ')
n1 = int(n1)
n2 = input('원하는 숫자를 입력하세요 >> ')
n2 = int(n2)


print('{}+{}={}'.format(n1,n2,n1+n2))
print('{}-{}={}'.format(n1,n2,n1-n2))
print('{}*{}={}'.format(n1,n2,n1*n2))
print('{}/{}={:.3f}'.format(n1,n2,n1/n2))


