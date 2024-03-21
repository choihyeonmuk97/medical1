# 함수 선언 : def 함수명()
# 함수값은 return (출력값) // 리턴 = 출력값이라고 생각하자
# 함수 호출 : 함수명()
# 매개변수 : 함수로 데이터를 전달하는 변수 / 매개변수 개수는 항상 같아야함.
# 가변매개변수는 일치하지 않아도 됨 // 선언 : def 함수명(*values)
# 리스트, 딕셔너리의 매개변수는 해당 주소값이 전달됨

# 함수를 사용하여 두 수를 입력받아
# 더하기, 빼기, 곱하기, 나누기 결과값 출력

# 선언
def cal(num1,num2):
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2
    return result1,result2,result3,result4

num1 = int(input('첫번째 숫자를 입력하세요. > '))
num2 = int(input('두번째 숫자를 입력하세요. > '))

# 호출
result1,result2,result3,result4 = cal(num1,num2)

# 출력 print('결과값 :',result1,result2,result3,result4)
print(f'더하기 : {result1}')
print(f'빼기 : {result2}')
print(f'곱하기 : {result3}')
print(f'나누기 : {result4}')

# 원하는 사칙연산 (input) -> 0311_08

def cal1(n1,n2,c):
    if c == '1':
        res = n1+n2
    elif c == '2':
        res = n1-n2
    elif c == '3':
        res = n1*n2
    elif c == '4':
        res = n1/n2
    return res

n1 = int(input('첫번째 숫자. > '))
n2 = int(input('두번째 숫자. > '))
c = input('원하는 사칙연산을 입력하세요. 1.+ 2.- 3.* 4./ ')

cal2 = cal1(n1,n2,c)
print('결과 :',cal2)