select * from employees;

create table member(
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
 
insert into member (id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111'
);

insert into member values (
'bbb','1111','유관순','010-2222-2222'
);

insert into member (id,name,phone) values(
'ccc','이순신','010-3333-3333'
);

/* 컬럼 수 부족 에러
insert into member values(
'ddd','강감찬','010-4444-4444'
);
*/

select id,pw,name,phone from member;

commit;

rollback;

select * from member;

insert into member values(
'ddd','1111','강감찬','010-4444-4444'
);

select * from member;

rollback;

commit;

update member set pw='2222' where id='ccc';

-- 모든 테이블 확인
select * from tab;

-- 오라클 타입
-- number(숫자),date(날짜), char(고정문자), varchar2(가변문자), clob(대용량 문자)

-- number : 정수, 실수
-- number(4) -> 자릿수는 4자리 (소수점 포함)

create table mem (
no number, -- 자릿수 정의 안함
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values(1234567890);
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11); -- 소수점 할당 안했기 때문에 1(정수)만 출력됨
insert into mem (no2) values(-9999);

insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- 111.00 error!!

select * from mem;

create table mem2 (
no number(4,2),
mdate date, -- date -> 년,월,일,시,분,초
mdate2 timestamp -- date = timestamp -> 밀리세컨드(1/1000)까지 저장 가능함 
);

insert into mem2 (mdate) values('2024-04-19');
insert into mem2 (mdate) values(sysdate); -- sysdate : 현재 시간 
insert into mem2 (mdate2) values(sysdate);
insert into mem2 (mdate,mdate2) values(sysdate,sysdate+30);

SELECT * FROM mem2;
select to_char(mdate,'yyyy-mm-dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy-mm-dd hh:mi:ss:ff') from mem2;

select mdate,mdate+30 from mem2;

select * from employees;
select sysdate-hire_date from employees;

create table mem3(
no number(4,2),
tel char(8), -- 고정 문자 : 8자리 고정. 더 커지면 error
name varchar2(9), -- 가변 문자
mdate date,
mdate2 timestamp
);

insert into mem3 (tel) values('11112222');
insert into mem3 (tel) values('22223333');
insert into mem3 (tel) values('111');
insert into mem3 (tel) values('123456789'); 

insert into mem3 (name) values ('홍길동'); -- 한글은 한글자당 3byte
insert into mem3 (name) values ('신사임당'); -- varchar2 : 가변 
INSERT INTO mem3 (name) VALUES ('AAA');
insert into mem3 (name) values ('aaa');

COMMIT;

select * from mem3 where name='AAA';
select * from mem3 where name='aaa';
select * from mem3 where lower(name)='aaa';

-- select, from 2개의 키워드로 구성됨. from 뒤엔 테이블명
-- SQL구문은 대소문자 구분하지 않는다!! 하지만 데이터는 대소문자를 구분함 !!

select emp_name,department_id from employees;

select distinct department_id from employees; -- distinct 중복 제거

select * from departments;
select department_id,department_name from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select no,mdate2,tel,name,mdate from mem3;

-- 사원번호, 사원이름, 급여, 입사일자 순으로 출력
select employee_id,emp_name,salary,hire_date from employees;

desc employees; 

drop table stu_score;

create table stu_score(
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);

insert into stu_score values (
6,'김유신',100,95,96,(100+95+96),(100+95+96)/3,1
);

commit;

select * from stu_score;

-- 산술연산자 : number타입인 경우에 사용가능
insert into stu_score values(
7,'홍길자',100,100,99,(100+100+99),(100+100+99)/3,1
);

select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;

-- 원화 환산 (1381.79원)
select employee_id,emp_name,salary from employees;
select employee_id,emp_name,salary,salary*1381.79 from employees;

-- 실제월급 = 월급 + (월급*커미션)
select employee_id,emp_name,salary+(salary*commission_pct) from employees;

-- Nvl(컬럼,0(정의)) : null value
select employee_id,emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;

-- 달러 연봉, 원화 연봉 
select emp_name,salary*12,(salary*12)*1381.79 from employees;
