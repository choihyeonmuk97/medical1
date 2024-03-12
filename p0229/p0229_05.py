# continue : 
# 반복문에서 남은 문장을 수행하지 않고 다음으로 넘어감
# pass는 문법적으로 필요는 하지만 어떤 동작도 원하지 않을 경우 사용
# 즉, 어떤 것도 수행하지 않고 해당부분을 패스함

n = 0
while n < 100:
    n += 1
    if n % 2 == 0:
        continue # 건너뛰기
    print(n, end=' ')

print()
