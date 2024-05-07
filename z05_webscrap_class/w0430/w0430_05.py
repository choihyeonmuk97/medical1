import oracledb


# 평균점수 입력받아 입력한 평균점수 이상의 학생을 출 력
# 반복문 돌리고 -1 - 종료
while True:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    cursor = conn.cursor()
    search = input('점수 입력 : ') 
    
    if search == '-1':
        break

    print('1. 평균이상')
    print('2. 평균이상')
    num = input('번호 입력 : ')
    if num == 1:
        print()
    
    sql = f'''
    select name, avg from stu_score \
    where avg >= {search}
    '''
    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        print('이름 :',d[0],end='\t|  ')
        print('평균 :',d[1])
        print('-'*50)
    conn.close()
print('종료')
    
conn.close()