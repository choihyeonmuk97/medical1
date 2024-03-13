def first(win_num):
    for i in range(5):
        win_num.append(i)
        
while True:
    input('다시 실행합니까?.')
    win_num = []
    first(win_num)
    print('win num 데이터 :',win_num )
    # win_num = []