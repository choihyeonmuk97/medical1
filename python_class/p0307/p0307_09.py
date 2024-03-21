import random

words = [{},
        {'airplane':'비행기','apple':'사과','bakery':'빵집','banana':'바나나',
          'bank':'은행','bean':'콩','bicycle':'자전거','boat':'보트',
          'bowl':'그릇','bus':'버스'},
         {'make':'만들다','have':'가지다','meet':'만나다','save':'저축하다',
          'write':'쓰다','spend':'보내다','remember':'기억하다',
          'miss':'놓치다','hate':'미워하다','eat':'먹다'},
         {"accumulated":"누적된","additional":"추가적인","adequate":"적당한",
    "administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한",
    "annual":"해마다의","different":"다른","local":"지역의",
    "social":"사회의"}]

choice = 1

w_list = list(words[choice].keys())
print(w_list)

w_list_ran = random.sample(w_list,5)
print(w_list_ran)

for w in w_list_ran:
    print(words[choice][w],end=' ')
print()
