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

w_title = ['','명사','동사','형용사']

choice = 1

w_list = list(words[choice].keys())

w_list_ran = random.sample(w_list,5)


# 함수 선언
def w_quiz(choice):
    print('{}를 선택하셨습니다.'.format(w_title[choice]))
    chk = input('1. 실행 0. 취소 ')
    if chk == '1':
        #print(w_noun.keys()) # 전체 key
        #print(w_noun.values()) # 전체 value
        count = 0
        for key in w_list_ran:
            #print(key,':',w_noun[key])
            answer = input('{} 뜻? '.format(key))
            if answer == words[choice][key]:
                print('정답입니다.')
                count += 1
            else:
                print('오답입니다.')
        print('총 {}문제를 맞추셨습니다.'.format(count))
    elif chk == '0':
        print('취소하셨습니다. 메뉴로 돌아갑니다.')
    else:
        print('잘못입력하였습니다. 다시 입력하세요. ')


while True:
    print('[영단어 맞추기 프로그램]')
    print('-'*50)
    print('1. 명사')
    print('2. 동사')
    print('3. 형용사')
    print('0. 종료')
    print('-'*50)
    choice = int(input('원하는 번호를 입력하세요. > '))

    if choice == 1:
        w_quiz(choice)
    elif choice == 2:
        w_quiz(choice)
    elif choice == 3:
        w_quiz(choice)
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break