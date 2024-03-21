# 두 수를 입력받아, 두 수 사이의 합계를 구하기

# 1. 입력
# 2. 함수 호출
# 3. 1, 10 -> 1+2+3+4+5+....+10
# 4. 합계를 리턴받아서 
# 5. 합계 : 55 출력

# 선언
# def cal(num1,num2):
#     sum = 0
#     if num1 > num2:
#         num1,num2 = num2,num1
#     for i in range(num1,num2+1):
#         sum += i
#     return sum
    
# num1 = int(input('첫번째 숫자를 입력하세요. > '))
# num2 = int(input('두번째 숫자를 입력하세요. > '))
# # 호출
# sum = cal(num1,num2)
# # 출력
# print('합계 :',sum)


''' 리스트 출력
def cal(s_list):
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] += i

sum = 0    
num1 = int(input('첫번째 숫자를 입력하세요. > '))
num2 = int(input('두번째 숫자를 입력하세요. > '))
s_list = [num1,num2,sum]
# 호출
cal(s_list)
# 출력
print('s_list :',s_list)
'''

# 파이썬 언어는 인터프리터 언어, 컴파일러 언어
# 1~10 까지의 더하기, 빼기, 곱하기의 결과값을 출력

def cal (s_list):
    # 더하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] += i
    # 곱하기
        s_list[4] *= i
    # 빼기
    for i in range(s_list[0]+1,s_list[1]+1):
        s_list[3] -= i
    


pls = 0
min = 1
mult = 1
num1 = int(input('첫번째 숫자를 입력하세요. > '))
num2 = int(input('두번째 숫자를 입력하세요. > '))
s_list = [num1,num2,pls,min,mult]
cal(s_list)

print('더하기 :',s_list[2])
print('빼기 :',s_list[3])
print('곱하기 :',s_list[4])