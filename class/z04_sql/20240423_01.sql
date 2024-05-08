select * from students;

--  순차정렬 / asc 생략가능 (defalut)
select * from students
order by name asc;

-- drop table students;
-- 컬럼 추가 : alter
alter table students add rank number(3);

-- 등수 매기기
select total,rank() over(order by total desc) rank from students;

-- no로 순차정렬
select * from students
order by no ;

-- 정렬 복수 가능 : 첫번째 조건 무조건 먼저 실행 후 두번째 조건 실행
-- 국어점수 같은 경우 영어점수로 정렬
select * from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

-- 날짜도 연산이 가능 !!
select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

-- hire_date : asc, comm -> 사원번호, 사원명, 직급, 입사일,월급 
select * from employees;

select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date desc; 

-- salary -> asc, if same salary -> emp_name desc
select * from employees
order by salary asc, emp_name desc;

-- 숫자함수 : ABS 절대값
select -10, abs(-10) from dual; -- dual : 가상 테이블

-- FLOOR : 소수점 아래 버림(자리 수 지정 불가), ROUND : 소수점 반올림
select 34.789, floor(34.789) as f, round(34.789) as r from dual;

select 34.178, round(34.178), round(34.178,2) from dual; --소수점 둘째자리 까지 출력(자리 지정)

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual; -- 자리 수 -(음수)는 정수 부분 자리 지정

-- TRUNC 지정한 자리 수 이하 버림 / 자리 수 지정 안하면 소수점 이하 버림
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

-- CEIL : 소수점 이하 올림 (자리수 지정 불가)
select ceil(34.123) from dual;

-- kor 첫째자리 절사
select no,name,trunc(kor,-1) from students
order by kor;

-- kor,eng,math 첫째 절사 -> total 출력
select trunc(kor,-1) kor,trunc(eng,-1) eng,trunc(math,-1) math,
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) total from students;

-- MOD : 나머지 값 출력
select round(100/7,2) from dual;
select mod(10,7)from dual;

-- 사원번호가 짝수인 것을 출력
select employee_id from employees 
where mod(employee_id,2)=0;

-- no 이 3의 배수인 학생만 출력
select * from students
where mod(no,3)=0;

-- 시퀀스 : 고유 번호 부여 (중복 불가)
create sequence seq_no
increment by 1 -- 증감 1
start with 1 -- 1부터 시작 
minvalue 1 -- 최소값 = 1 
maxvalue 9999 -- 최대값 = 9999
nocycle -- 반복하지 않음
nocache -- 캐시 사용안함
;

-- nextval : 시퀀스 번호가 1씩 증가함
select seq_no.nextval from dual;

-- currval : 시퀀스 현재 번호 확인
select seq_no.currval from dual;

--drop table member;
--drop table mem3;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select seq_mno.nextval from dual; -- nextval 무조건 번호 증가

insert into member values (
seq_mno.nextval,'eee','1111','김구','010-5555-5555'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

select 's'||to_char(seq_mno.nextval,'00000') from dual;

-- ko202400001 형식으로 시퀀스 : seq_kono, 1~99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

-- trim() 공백제거
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;

-- 게시판 생성
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

-- start 1001, increment 10 min 1, max 99999 5번 실행
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
nocycle
nocache
;

select seq_deptno.nextval from dual;


create table emp01(
empno number(4) primary key,
ename varchar2(30),
hire_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- alter() : 수정
alter sequence emp_seq
increment by 1001
;

insert into emp01 values(
emp_seq.nextval, '이순신', sysdate
);

select * from emp01;

commit;

-- hire_date desc, employee_id,emp_name,job_id,hire_date
-- 입사한지 몇일 됐는지 올림 사용
select employee_id,emp_name,job_id,hire_date, ceil(sysdate-hire_date)||'일' day from employees
order by hire_date desc;

select emp_name from employees;

-- job_id || employee_id

select job_id||employee_id from employees;

-- substr(대상,시작위치,개수) : 문자열을 시작위치 부터 n개 만큼 자름
select substr(job_id,0,2) from employees;

select emp_name,substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;

-- job_id 앞에 2개 글자 || employee_id 5자리
select * from employees;

select substr(job_id,1,2)||trim(to_char(employee_id,'00000')) as id from employees;

-- 날짜함수 sysdate : 현재

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') now from dual;

-- months_between : 두 날짜 사이의 n개월
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;

-- 월 더하기
select sysdate,add_months(sysdate,2) from dual;

-- 입력한 날짜 기준으로 다음에 오는 요일을 출력
select NEXT_DAY(sysdate, '월요일') from dual;

-- 입력한 기준으로 해당 월의 마지막 일을 출력
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;


