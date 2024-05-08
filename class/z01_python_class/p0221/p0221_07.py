print(200+100)
print(200-100)
print(200*100)
print(200/100)

# 1. 200 -> 50으로 바꿔서 출력?
print(50+100)
print(50-100)
print(50*100)
print(50/100)

# 2. 100 -> 10
print(50+10)
print(50-10)
print(50*10)
print(50/10)

# 3. 10 -> 30
print(50+30)
print(50-30)
print(50*30)
print(50/30)

# 4. 50 -> 20
print(20+30)
print(20-30)
print(20*30)
print(20/30)


# 변수를 사용하면 편하다
a = 100
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print('-'*20)

# 함수를 사용하여 사칙연산 계산
def cal(a,b) :
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

cal(100,5)
print('-'*20)
cal(50,2)

# 10-5=5
num1 = 10
num2 = 5
print(str(num1)+'-'+str(num2)+'='+str(num1-num2))
print(num1,'-',num2,'=',num1-num2)
print('%d-%d=%d'%(num1,num2,num1-num2))
print('{}-{}={}'.format(num1,num2,num1-num2))

