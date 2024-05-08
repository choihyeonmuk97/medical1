# 변수
# 기본 : bool, int, float, string
# list, tuple, dict
a = True
b = False
print('bool형은 {},{}가 있다.'.format(a,b))

c = 45
print('int형은 정수 {:d}와 같은 숫자'.format(c))
print('%d'%(c))

d = 3.123456
print('float형은 실수 {:.2f}'.format(d))

e = '문자' # string
print('%s'%e)

# input() : 콘솔창에서 입력
str1 = input('word insert ')
print('{}은 입력한 변수값입니다.'.format(str1))

n1 = int(input('숫자? '))
n2 = int(input('숫자? '))
print(n1 * n2)



