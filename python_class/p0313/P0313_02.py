# 선언
def cal(num1,num2):
    r_list =[0]*6
    r_list[0] = num1 
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    r_list[5] = num1 / num2
    return r_list

save_list = []

while True:
    num1 = int(input('첫번째 숫자를 입력하세요. > (0. 종료) '))
    if num1 == 0:
        break
    num2 = int(input('두번째 숫자를 입력하세요. > '))
    # 호출
    r_list = cal(num1,num2)
    save_list.append(r_list)
    
    # 출력 
    print('{},{} 결과값 : {},{},{},{}'.format(*r_list))

# 현재까지 입력한 숫자와 결과값을 모두 출력

print('현재까지 입력한 숫자 및 결과값 : ')
for s in save_list:
    print('{},{} 결과값 : {},{},{},{}'.format(*s)) 
