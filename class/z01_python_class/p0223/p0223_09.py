import datetime
now = datetime.datetime.now()

# print(now)
month = now.month

# 현재의 계절을 출력
# 3,4,5 봄 / 6,7,8 여름 / 9,10,11 가을 / 12,1,2 겨울 

if 3<= month <= 5:
    print('봄')
elif 6 <= month <= 8:
    print('여름')
elif 9<= month <= 11:
    print('가을')
else:
    print('겨울')

