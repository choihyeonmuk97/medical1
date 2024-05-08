-- 어제, 오늘, 내일
select sysdate-1, sysdate, sysdate+1 from dual;

-- 오늘, 이번달의 처음일, 마지막일
select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;

-- 두 날짜간의 일수, 두 날짜간의 개월 차이
select trunc(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2) from employees;

select trunc(kor,-1) kor, count(trunc(kor-1))  from stu_score
group by trunc(kor,-1)
order by kor ;

-- hire__date 에서 월 만 출력
select to_char(hire_date, 'yyyy-mm-dd') from employees;
select to_char(hire_date, 'mm') hire_date, count(to_char(hire_date, 'mm')) from employees
group by to_char(hire_date, 'mm')
order by hire_date;

-- hire_date 에서 연도를 출력하고 카운트 그룹바이
select to_char(hire_date, 'yyyy') hire_date, count(to_char(hire_date, 'yyyy')) as 인원수 from employees
group by to_char(hire_date, 'yyyy')
order by hire_date;

-- 시퀀스로 학번 부여 ko20240001 5개 학번 출력
insert into dual values (
'ko'||to_char(sysdate,'yyyy')||stu_seq.nextval
); -- 테이블이 없어서 인서트 안됨 ㅋㅋ

select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;

-- '123,456,789' + '100,000' = 123556789
select to_number('123,456,789','999,999,999')+to_number('100,000','999,999') from dual;

select to_char(to_number('123,456,798','999,999,999')+to_number('156,778','999,999'),'L999,999,999') 
as sum from dual;

-- 숫자형으로 표시된 날짜를 날짜 타입으로 변경 20240425 ->24/04/25
select to_date(20240425)+3 from dual;

select emp_name,hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

-- 20070101 이후 입사, 두번째에 a 들어간 사람
select emp_name,hire_date from employees
where emp_name like '_a%' and hire_date >= '20070101';

-- 08월 입사, 사원이름 2번째에 a가 들어간 사람
select emp_name,hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') = 08 ;

-- 01,05,08 // 조회하고자 하는게 다수 일 경우 in()
select emp_name,hire_date from employees
where to_char(hire_date,'mm') in(01,05,08);

select * from m_date;

-- 입력 시 날짜타입에 문자(형태:날짜)를 입력해도 저장이 된다
-- 날짜 - 문자 불가능 ! 문자 -> 날짜 형변환 해야함
insert into eventDate values(
seq_mno.nextval, sysdate, '2024-04-01', sysdate-to_date('2024-04-01')
); 

select * from eventDate;

create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

-- 문자 -> 숫자
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- nvl() : null value
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

select emp_name, nvl(to_char(manager_id),'ceo') manager_id from employees
order by manager_id desc;

-- 그룹합수 - sum, avg, count(), count(*):전체, min, max
-- count() : 집계
select count(*) from employees;
select count(emp_name) from employees;

select count(manager_id) from employees; -- null이 있으면 count 되지 않음

select emp_name,manager_id from employees;

-- sum() : 총합
select sum(salary) from employees;

-- avg() : 평균
select avg(salary) from employees;

-- min() : 최소값, max() : 최대값
select min(salary),max(salary) from employees;

-- 6461(avg) < salary
select emp_name,salary from employees
where salary > (select avg(salary) from employees) 
order by salary asc;

select min(salary) from employees;

-- min(salary) 대상자 사번, 이름 출력
select employee_id,emp_name,salary from employees
where salary = (select min(salary) from employees);

-- max
select employee_id,emp_name,salary from employees
where salary = (select max(salary) from employees);

-- id = 50의 salary 합계
select department_id, salary from employees;

select sum(salary) from employees
where department_id = 100;

select count(*) from stu_score;

-- kor >= 80
select name,kor from stu_score
where kor >= 80
order by kor;

-- 국어점수 평균 이상, 영어 점수 평균 이상
select name,kor,eng from stu_score
where kor >= (select avg(kor) from stu_score) and eng >= (select avg(eng) from stu_score)
order by kor, eng;

create table s_info (
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,2000
);

insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) 
and eng >= (select avg(eng) from stu_score))
);

select * from s_info;

-- salary max, min, avg (가장 접근)
select emp_name,salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select trunc(avg(salary),-2) from employees);

select * from employees order by salary;

-- max
select emp_name, salary from employees
where salary = (select max(salary) from employees);

-- avg 이하 56명 중 최대값
select emp_name,salary from employees
where salary = (select max(salary) from(
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
));

-- 문자함수
-- LPAD, RPAD (comm,자리수,'채울문자')
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name,rpad(emp_name,20,'@') from employees;

-- LTRIM, RTRIM(comm,'슬라이싱할 문자')
select emp_name,ltrim(emp_name, 'Do') from employees;

select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

-- substr(컬럼or문자열,시작점,슬라이싱할 문자수)
select emp_name, substr(emp_name,3,4) from employees;

select job_id from employees;

-- job_id 앞 두글자 + 사원번호 결합
select substr(job_id,1,2)||employee_id from employees;

-- length : 길이
select emp_name, length(emp_name) from employees
where length(emp_name) > 15;

-- 날짜 함수 +,- 가능 ! 날짜+날짜 더하기 안됨

-- add_months : 개월 계산
-- months_between : 두 날짜 간의 차이 계산

-- 숫자 함수
-- ceil floor mod power 

-- emp_name || hire_date
select emp_name || to_char(hire_date,'yyyy"년" mm"월" dd"일" day') from employees;

-- emp_name, salary*1400 원화표시랑 쉼표, 9자리 빈공백 0
select emp_name, to_char(salary*1400, 'L000,000,000') KRW from employees
order by KRW;

-- 내 생일 속한 달의 마지막 일
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day(to_date('2010-10-10')) from dual;

select * from member;

-- DDL (data definition language) 
-- commit, rollback 불가
-- 컬럼 추가
alter table member add gender  varchar2(6) default 'female' not null;

update member set gender = 'male';

-- 컬럼 수정 : 컬럼의 이름, 타입 변경 가능
alter table member rename column name to stu_name; -- 이름 변경

alter table member modify(stu_name varchar2(50)); 
-- 타입 변경 / 컬럼의 데이터 형식이 맞거나 그렇지 않으면 비어있거나 null 이어야함


-- 컬럼 삭제
alter table member drop column phone;