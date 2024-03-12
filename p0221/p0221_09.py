# 사칙연산 출력
# ex)30, 6을 입력하여
n1 = input('첫번째 수 : ') # 출력 시 int를 쓰지 않고 input 앞에 int를 붙여도 됨
n2 = input('두번째 수 : ') # 그러면 변수 사용하여 출력한 방식으로도 가능(미리 형 변환이 되었기 때문)

print('두 수의 합 :',int(n1)+int(n2))
print('두 수의 차 :',int(n1)-int(n2))
print('두 수의 곱 :',int(n1)*int(n2))
print('두 수의 나눔 :',int(n1)/int(n2))

print('30+6=',int(n1)+int(n2))
print('30-6=',int(n1)-int(n2))
print('30*6=',int(n1)*int(n2))
print('30/6=',int(n1)/int(n2))

print('-'*20)


# 변수 사용하여 수식 출력
a = 30
b = 6
print(str(a)+'+'+str(b)+'='+str(a+b))
print('%d-%d=%d'%(a,b,a-b))
print('{}*{}={}'.format(a,b,a*b))
print(a,'/',b,'=',a/b)

