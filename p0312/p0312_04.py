# 매개변수 순서, 타입 중요

def str_print(txt,num):
    for i in range(num):
        print(txt,end=' ')

txt = input('출력하고 싶은 글자를 입력하세요. > ')
num = int(input('출력하고 싶은 글자의 반복횟수를 입력. > '))

str_print(txt,num)
