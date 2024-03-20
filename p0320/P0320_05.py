# 전개연산자 -> 함수의 가변매개변수에서도 사용이 가능함
def func (*a):
    # print(a) -> tuple 형태
    for i in a:
        print(i,end=' ')
print()

func(1,2,3,4,5,6,67,3,43,42,4,42,34)

