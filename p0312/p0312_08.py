# 자바 같은 경우 매개변수 개수에 따라 다른 함수로 인정
# 파이썬은 이름이 무조건 달라야함.

# def aaa(num1):
#     print(num1)


# def aaa(num1,num2):
#     print(num1,num2)

def func2(num1=0,num2=10,num3=3): # 키워드 매개변수 - 값이 들어오지 않으면 디폴트값으로
    print(num1,num2,num3)

func2(100)