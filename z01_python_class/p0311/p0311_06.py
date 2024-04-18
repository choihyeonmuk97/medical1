sum = 0

def plus(num):
    global sum
    sum += num
    
n_input = int(input('숫자입력 > '))
plus(n_input)

print('총합 : ',sum)