import oracledb 

# DB connect
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

# sql 실행
# employees 테이블에서 employee_id,emp_name,salary,real salary(1410원)
# sql = "select employee_id,emp_name,salary, \
#         trim(to_char(salary+(salary*nvl(commission_pct,0)),'99,999')) as real_sal, \
#         trim(to_char(salary*1410,'99,999,999')) as kor_sal \
#         from employees"

# 부서별 평균월급, 최대월급, 최소월급
sql="select department_id,round(avg(salary),0),max(salary),min(salary) from employees \
    where department_id is not null \
    group by department_id \
    order by department_id"

cursor.execute(sql)
data = cursor.fetchall()

print('데이터 출력')

for d in data:
    print("부서\t평균월급\t최대월급\t최소월급")  
    print(d[0],end="\t")
    print('$',d[1],end="\t\t")
    print('$',d[2],end="\t\t")
    print('$',d[3])
    print('-'*60)
    
conn.close()

# for d in data:
#     print("사번\t사원명\t\t월급\t실제월급\t원화환산")
#     print(d[0],end="\t")
#     print(d[1],end="\t")
#     print(d[2],end="\t")
#     print('￦',d[3],end="\t")
#     print('￦',d[4])
#     print('-'*60)