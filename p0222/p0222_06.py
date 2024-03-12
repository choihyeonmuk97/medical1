# 산술 연산자
# + - * /
a = 4
b = 2
result = a + b
result = a - b
result = a * b
result = a / b

print(result)

result = a//b # 나눗셈의 몫 4//2 -> 몫 : 2 나머지 : 0
print(result)
result = a%b  # 나머지
print(result)
result = a**b # 제곱
print(result)

c = 10
d = 20
c,d = 100,200

# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 -> 덧셈, 뺄셈 순
# 괄호가 있는 경우 괄호 안 먼저 계산
# 괄호가 없을 경우 왼쪽->오른쪽 방향으로 계산
# 괄호 사용을 추천

# 다른 자료형으로 연산
str1 = '문자열'
n1 = 10

print(str1*n1)
# print(str1+n1) -> error 유형이 다름

# int, float
s1 = '100'
s2 = '10.123'
print(int(s1)+1)
print(float(s2)+1)

#숫자가 아닌 것은 변환 할 수 없음
# n = int('안녕하세요') -> error

# 숫자를 문자로 변환 시 str을 사용
n1 = 100
n2 = 10.123
print(str(n1)+'1')
print(str(n2)+'1')


# 숫자 두개를 입력받아서 나눈 값, 몫, 나머지 값을 구하세요
n1 = input('숫자를 입력하세요 >> ')
n2 = input('숫자를 입력하세요 >> ')
n1 = int(n1)
n2 = int(n2)

result1 = n1/n2
result2 = n1//n2
result3 = n1%n2

print('나눈 값 : {:.1f} \n몫 : {} \n나머지 : {}'.format(result1,result2,result3))


