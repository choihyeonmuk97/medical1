# 함수 선언
def calc(v1,v2,op):
    result = 0 # 지역 변수
    if op == '1':
        result = v1+v2
    elif op == '2':
        result = v1-v2
    elif op == '3':
        result = v1*v2
    elif op == '4':
        result = v1/v2
    
    return result

print('1. 더하기 2. 빼기 3. 곱하기 4,. 나누기')
a_input = input('계산하려고 하는 방식을 입력하세요. > ')
var1 = int(input('첫번째 숫자를 입력하세요. > '))
var2 = int(input('두번째 숫자를 입력하세요. > '))

aaa =0 # 전역 변수
# 호출
data = calc(var1,var2,a_input)
# 출력
print('결과값 : ', data)
