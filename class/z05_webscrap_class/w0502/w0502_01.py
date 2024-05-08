import oracledb
import math

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

# 최초 번호
num = 0
perCount = 10
startrow = 1 # 1,11,21,31,....
endrow = 10 # 10,20,30,40,...
limit = 0
search = input('학생이름을 입력하세요 : ')

sql = f'''select count(*) from(select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%{search}%')'''
cursor.execute(sql)
all_count = cursor.fetchone()
limit = math.ceil(((all_count[0])/perCount))


while True:
    if num != 0:
        print('1. < 이전 ')
        print('2. 다음 > ')
        no = input('원하는 번호를 입력하세요 : ')
        if no == '1': 
            if num == 1 : num = 1
            else : num -= 1
        else: num += 1
        startrow = (num-1)*perCount+1 # 1,11,21,31,....
        endrow = startrow+perCount-1 # 10,20,30,40,...        
    else: 
        num += 1
        if num >= limit:
            num = limit
    sql = f'''select * from(select row_number() over(order by no) rnum,a.* from stu_score a 
            where id like '%{search}%') where rnum >= {startrow} and rnum <= {endrow}'''
    cursor.execute(sql)
    data = cursor.fetchall()

    ## 10개씩 끊어서 보여주도록 구성
    print('[ 학생 검색 데이터 ]')
    for d in data:
        print(d)
        
    print('-' *100)
    print('검색된 페이지 :',num,'검색된 데이터 수 :',all_count)
    
    
        
        