import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()


while True:
    search = input('찾고자 하는 이름을 검색하세요 >> ')

    sql = f'''select * from stu_score \
        where name like '%{search}%'
        '''
    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        print(d)
        
    if search == '-1':
        print('종료')
        break
    
conn.close()