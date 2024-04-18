import datetime # 날짜 관련 기능을 가져옴
now = datetime.datetime.now()

year = now.year
hour = now.hour

# 시간을 이용하여 지금이 오전이면 오전, 오후면 오후 출력
if hour < 12 :
    print('오전')
else:
    print('오후')

if hour < 12 :
    print('현재는 {}시로 오전입니다.'.format(hour))
else:
    print('현재는 {}시로 오후입니다'.format(hour))

# print(now) # -> 현재 날짜 시 분 초

# print(now.year)
# print(now.month)
# print(now.day)

# print(now.hour)
# print(now.minute)
# print(now.second)

# 1. 짝수달, 홀수달
m = now.month
if m % 2 == 0:
    print('이번달은 {}월로 짝수달 입니다.'.format(m))
else:
    print('이번달은 {}달로 홀수달 입니다.'.format(m))

# 2. 월을 이용하여 겨울입니다 아닙니다
if 1<=m<=3 or 11<=m<=12:
    print('이번달은 {}월로 겨울입니다.'.format(m))
else:
    print('이번달은 {}월로 겨울이 아닙니다.'.format(m))


