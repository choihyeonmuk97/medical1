def cal(input1,input2):
    result1 = input1+input2
    result2 = input1-input2
    result3 = input1*input2
    result4 = input1/input2
    return result1,result2,result3,result4    


input1 = int(input('1번째 숫자를 입력하세요. > '))
input2 = int(input('2번째 숫자를 입력하세요. > '))

# 함수의 return을 사용하여 입력된 두 수의 사칙연산 결과값을 출력

result1,result2,result3,result4 = cal(input1,input2)
print('결과값 : ',result1,result2,result3,result4)



# for i in range(10):
#     sum = 0
#     sum += i

# for i in (5):
#     result = 1 
#     result += 1



# def plus(v1,v2):
#     v1 = v1 + 100
#     v2 = v2 + 200
    
#     return(v1,v2)
    
# v1 = 1
# v2 = 2 
# plus(v1,v2)

# print(v1,v2)