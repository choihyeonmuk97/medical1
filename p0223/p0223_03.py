# if
# 1. 키가 130 이상이어야 놀이기구 탑승 가능
height = 120
if height >= 130:
    print('놀이기구 탑승 가능')
else:
    print('탑승 불가')

# 2. 나이가 10살 이상, 키 130 이상 놀이기구 탑승 가능
age = 11
if age >= 10 and height >= 130:
    print('놀이기구 탑승 가능')
else:
    print('탑승 불가')

# 3. 비 -> 우산을 챙겨주세요 아니면 선크림 발라주세요
weather = '비'
if weather == '비':
    print('우산을 챙겨주세요')
else:
    print('선크림 발라주세요')

# 4. 비 나 눈 -> 우산을 챙겨주세요 아니면 선크림 발라주세요
snow = '눈'
if weather == '비' or snow == '눈':
    print('우산을 챙겨주세요')
else:
    print('선크림 발라주세요')


