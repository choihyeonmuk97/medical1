import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

sql = "create table mem (id varchar2(30) primary key, pw number, name varchar2(30), mdate date)"
cursor.execute(sql)

# ddl 데이터 명령어 : create,alter,drop-> commit이 없음
# dml 데이터 정의어 : insert, update, delete -> commit 필요

print('테이블 생성 완료')

conn.close() 