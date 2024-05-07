import oracledb

# sql 불러오기
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor() # db와 연결되어 지시자 생성

 # 학번, 이름, 합계, 평균, 학점을 프로그램해서 출력
 # 평균을 가지고 파이썬 이용하여 학점을 출력
sql = "select * from stu_score"

cursor.execute(sql) # cursor에 select 한 결과값을 저장(list)
data = cursor.fetchall() # fetchall() : 모든 데이터를 가져옴 / fetchone() : 1개의 데이터를 가져옴

print('[ 모든 데이터 출력 ]')
for d in data:
    if d[6] >= 90 :
        print('학번 :',d[0],'이름 :',d[1],'합계 :',d[5],'평균 :',d[6],'학점 : A')
        print('-'*60)
    elif d[6] >= 80 :
        print('학번 :',d[0],'이름 :',d[1],'합계 :',d[5],'평균 :',d[6],'학점 : B')
        print('-'*60)
    elif d[6] >= 70 :
        print('학번 :',d[0],'이름 :',d[1],'합계 :',d[5],'평균 :',d[6],'학점 : C')
        print('-'*60)
    elif d[6] >= 60 :
        print('학번 :',d[0],'이름 :',d[1],'합계 :',d[5],'평균 :',d[6],'학점 : D')
        print('-'*60)
    else :
        print('학번 :',d[0],'이름 :',d[1],'합계 :',d[5],'평균 :',d[6],'학점 : F')
        print('-'*60)


print('-')
print('타입 :',type(data))


# 월급의 평균을 구하기
sql = "select round(avg(salary),2) from employees"
cursor.execute(sql) # cursor에 select 한 결과값을 저장(list)
data = cursor.fetchone() # fetchall() : 모든 데이터를 가져옴 / fetchone() : 1개의 데이터를 가져옴

print(data[0])


conn.close()












# stu_score avg 90점 이상 A, 80 B, 70 C, 60 D, 나머지 F
# sql = '''select no,name,total,avg, 
#     case
#     when avg >= 90 then 'A'
#     when avg >= 80 then 'B'
#     when avg >= 70 then 'C'
#     when avg >= 60 then 'D'
#     else 'F'
#     end as grade
#     from stu_score 
#     order by grade'''




# board 테이블 id, member 테이블 name
# board 테이블의 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력하기
# sql = "select bno,board.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board, member\
#     where member.id = board.id" 