while True:
    print('[ LogIn ]')
    print('-'*30)
    id = input('ID : ')
    pw = input('PW : ')
    print('-'*30)

    # 파일에서 아이디, 패스워드 확인    
    chk = 0
    with open('member.csv','r',encoding='utf8') as f:
        while True:
            txt = f.readline()
            if txt == '': break
            mem = txt.split(',')
            # 아이디, 패스워드 비교
            if id == mem[1] and pw == mem[2]:
                chk = 1
                break
    
    # 아이디 패스워드 없으면 chk == 0, 있으면 chk == 1
    if chk == 1:
        print('로그인 되었습니다.')
        break
    else:
        print('정보가 일치하지 않습니다. \n다시 입력해주세요.')


while True:
    print('[ 학생성적 프로그램 ]')
    print('-'*60)
    print('1. 학생성적입력')
    print('0. 프로그램 종료')
    print('-'*60)
    choice = int(input('번호를 입력하세요. > '))
    
    if choice == 1:
        print('[ 학생성적입력 ]')
    
    elif choice == 0:
        print('프로그램 종료')
        break