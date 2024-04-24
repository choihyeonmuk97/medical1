-- trunc : 버림, round : 반올림 (자리 지정 가능)
select sysdate,hire_date,round(sysdate-hire_date,3) from employees;

-- sysdate : 현재 일자 / -1 : 어제, +1 : 내일
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일, sysdate+100 from dual;

-- m_no - seq 1~9999 inc 1  -> 5번 반복해서 저장
-- m_yesterday, m_today, m_tomorrow,m_year 컬럼을 가진 m_date 테이블 만들고
-- 어제, 오늘, 내일, 1년 후 날짜 저장

create sequence m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select m_no.currval from dual;

create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date
);

select * from m_date;

insert into m_date values(
m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365);

-- ABS() : 절대값 출력
select abs(hire_date-sysdate) from employees;

-- 월을 기준으로 반올림
select hire_date,round(hire_date,'month') from employees;
-- 월을 기준으로 버림
select hire_date,trunc(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일, hire_date from employees
order by hire_date;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period = '201111';

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) count from students
group by trunc(kor,-1)
order by t_kor;

select trunc(hire_date,'month') m_hire_date, count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;
select * from employees;

--drop table board;

select * from stu_score
order by no;

update stu_score set name = '홍길순'
where no = 8;

update stu_score set avg = total/3;

-- 2개의 날짜에서 월 간격 확인 : BETWEENS_MONTH
select hire_date, floor(months_between(sysdate,hire_date)), trunc(sysdate-hire_date,2) from employees;

-- 개월 추가
select hire_date, add_months(hire_date,6) from employees;

-- last_day : 해당 월의 마지막 일
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

select sysdate 현재, trunc(sysdate,'month') 처음일, last_day(sysdate) 마지막일 from dual;

-- next_day : 다음 돌아오는 요일이 몇일인지 알려줌
select sysdate,next_day(sysdate,'토요일') from dual;
-- 한 주의 처음일
select sysdate, trunc(sysdate,'d') from dual;

-- default : 기본값 지정하여 자동 입력되게함
create table board (
bno number(4) primary key, -- 중복제거, null값 허용하지 않음
name varchar2(10),
btitle varchar2(1000),
bcontent clob, -- 글자 수 제한 없음.
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values (
board_seq.nextval, 'aaa', '제목', '내용', sysdate, 0, board_seq.currval, 0, 0, '1.jpg'
);

insert into board(bno,name,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval, 'bbb', '이벤트 신청', '이벤트', board_seq.currval, '2.jpg'
);

select * from board;

-- 형변환 : number, character, date
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate, 'yy/mm/dd') from dual;
select to_char(sysdate, 'yyyy') from dual;

-- ko20240001
select 'ko'||to_char(sysdate, 'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'), to_char(sysdate,'day') from dual;
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon dd day') from dual;

-- hire_date 
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon dd day') from employees;

select to_char(sysdate, 'am hh24:mi:ss' )from dual;

select * from stu_score;

select to_char(c_date, 'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- 날짜별로 몇개 데이터 있는지
select c_date, count(c_date) from stu_score
group by c_date
order by c_date;

-- 문자형 사칙연산 안됨 / 자리수, 쉼표 표시, 날짜표시유형변경 가능
-- 숫자형 사칙연산 가능 / 자리수, 쉼표 표시 불가
-- 날짜형 덧셈,뺄셈 연산 가능, MONTHS_BETWEEN : 2개 날짜의 월 차이 계산, 날짜표시유형을 지정할 수 없음(기본값 - yy/mm/dd).


-- 문자형 안에 있는 데이터가 숫자이면 자동으로 형변환해서 계산해준다,
-- 문자형 안에 숫자+문자 같이 있으면 형변환 안된다.
select 10 a, 100 b, (10+100) ab,to_char(100),10+'100' from dual; 
select 10 a, 100 b, (10+100) ab,to_char(100),10+'100원' from dual;  -- error

-- 0 은 빈자리를 0으로 채우고 9는 빈자리 채우지 않고 그냥 둠
select 12340000, to_char(12340000,'00,000,000') from dual;
select 12340000, length(to_char(12340000,'999,999,999')) from dual; -- 공백이 숨어있다

-- L : 지역 통화 표시
select 12340000, to_char(12340000,'L00,000,000') from dual;
select 12340000, to_char(12340000,'$00,000,000') from dual;
-- 소수점 자리 표시
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;

select length(trim(to_char(12345,'0000000000'))),to_char(12345,'999,999') from dual;

-- 123,456,789 + 100,000 = 값 출력
--select to_char(123456789+100000,'999,999,999') from dual;
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')),'L000,000,000') 
as sum from dual;

select to_number('0000123') from dual;

-- 날짜형변환
select to_date('2024-04-24')-to_date('2024-04-23') from dual;

-- yyyy-mm-dd
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') as 일자 from dual;

select hire_date from employees
where hire_date >= '20080101';

select * from stu_score;
select c_date from stu_score
where c_date = '2024/04/05';

select sysdate-to_date('2024/04/01') from dual;

-- '20,000' - '10,000' = 10,000
select to_char(to_number(replace('20,000',',',''))-to_number(replace('10,000',',','')),'00,000') 
as sum from dual;

select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999')
as sum from dual;


-- real salary // salary,commission_pct
select * from employees;

select nvl(commission_pct,0), salary+(nvl(salary*commission_pct,0)) from employees;

-- null 값만 출력
select emp_name,commission_pct from employees
where commission_pct is null;

-- null 이면 0 출력
select nvl(manager_id,0) from employees
order by manager_id desc;

select emp_name, nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;


-- length() : 데이터의 길이를 알 수 있음
select length('안녕하세요') from dual;
select length(1234000) from dual;

