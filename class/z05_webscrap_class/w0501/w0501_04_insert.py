import oracledb

while True:
    # hhh,1111,홍길자,여자,sysdate
    id = input('아이디를 입력하세요 (-1:종료) : ')
    if id == '-1':
        break
    
    # id를 먼저 검색 한 후 데이터를 입력하도록 해야 함
    # id가 존재하면 id를 다시 입력하고, 존재하지 않으면 비밀번호 입력으로 넘어가기

    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    cursor = conn.cursor()
    
    sql = f"select * from member where id = '{id}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    # id 중복 확인
    if len(data) == 1:
        print('중복아이디가 존재합니다. 다시 입력하세요')
        print()
        continue # 반복문으로 돌아간다
    
    pw = input('비밀번호를 입력하세요 : ')
    name = input('이름을 입력하세요 : ')
    gender = input('성별을 입력하세요 : ')


    sql = f"insert into member values(member_seq.nextval,'{id}','{pw}','{name}','{gender}',sysdate)"
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.execute('commit')

    print('-완-')

    conn.close() 