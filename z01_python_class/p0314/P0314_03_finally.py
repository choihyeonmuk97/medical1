print('프로그램 실행')
try:
    print(1)
    print(2)
#    print(1/0) # 에러 발생
    print(3)
except: # 예외가 발생했을 때 실행
    print(4)
    print(5)
else: # 예외가 발생하지 않았을 때 실행
    print(6)
finally: # 예외 발생 상관 없이 무조건 실행
    print(7)

print('프로그램 종료')