import oracledb

# sql 불러오기
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor() # db와 연결되어 지시자 생성

# 이름 2번째에 a가 있는 학생 출력, 학번으로 순차정렬
# sql = 'select * from stu_score'
sql = "select * from stu_score\
    where name like '_a%'\
    order by no asc"
cursor.execute(sql) # cursor에 select 한 결과값을 저장(list)
data = cursor.fetchall() # fetchall() : 모든 데이터를 가져옴 / fetchone() : 1개의 데이터를 가져옴

print('[ 모든 데이터 출력 ]')
# print(data)
for d in data:
    print(d)
    print('-'*20)
print('-')
print('타입 :',type(data))