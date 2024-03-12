import random

fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

print('개수 : ',len(fruit))
# 랜덤으로 4개 출력
# 랜덤은 리스트에서 출력 -> key를 리스트 타입으로 변경
print(fruit.keys()) # 딕셔너리에서 key 값 추출

f_list = random.sample(list(fruit.keys()),4)

f_list2 = ['키위','포도','복숭아','배']


# value값을 전체 출력
# for key in fruit:
#     print(fruit[key])
