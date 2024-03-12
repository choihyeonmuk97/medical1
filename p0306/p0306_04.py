fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

# 복숭아 영어로 입력하시오. -> 영어 입력했을때 정답입니다

answer = 0
wrong = 0
for f in fruit:
    eng_in = input("{}를 영어로 입력하세요. > ".format(fruit[f]))
        
    print("입력한 단어 : {}".format(eng_in))
    if eng_in == f:
        print('정답입니다.')
        answer += 1
    else:
        print('틀렸습니다. 정답은 {} 입니다.'.format(f))
        wrong +=1

print(f"{answer}개 정답, {wrong}개 오답입니다.")

