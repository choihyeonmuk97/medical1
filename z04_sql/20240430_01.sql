select * from stu_score;

select * from board;

select no,name,total,avg, 
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score 
order by grade
;

select * from employees;

select employee_id,emp_name,salary, 
to_char(salary+(salary*nvl(commission_pct,0)),'L99,999') as real_sal, 
to_char(salary*1410,'L99,999,999') as kor_sal 
from employees;

select department_id,round(avg(salary),0),max(salary),min(salary) from employees
where department_id is not null
group by department_id 
order by department_id;

select * from stu_score
order by no;

select * from stu_score
where name like '%홍%';

select avg(avg) from stu_score;

select avg from stu_score
where avg >= (select avg(avg) from stu_score);

-- EQUI JOIN : 컬럼명이 같은 것이 있는 테이블간의 조인
-- 사원번호, 사원명, 부서번호, 부서명을 출력
select employee_id,emp_name,a.department_id,department_name 
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees); 

-- 그리고 두번째 자리에 a가 들어가는 사원
select emp_name from employees
where emp_name like '_a%';

-- 월급이 평균이상인 사람 출력
select emp_name,salary from employees
where salary >= (select avg(salary) from employees);

select * from employees;
select * from departments;

select * from jobs;

-- 사원번호,사원명,월급,최소월급,인상분,직급,직급명
-- 최소월급보다 몇%이상을 받고 있는지 ( 최소월급 / 현재월급 *100)
select employee_id, emp_name, salary, min_salary,to_char(round(((salary-min_salary)/salary)*100,2))||'%' as 인상, a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
order by employee_id; 

-- 사원번호, 사원명, 부서번호, 부서명, 직급번호(job_id?), 직급명
select employee_id, emp_name, e.department_id, department_name, e.job_id, job_title 
from employees e,departments d,jobs j
where e.job_id = j.job_id and e.department_id = d.department_id
order by employee_id;

select job_id, job_title from jobs;
-- job_title 에 Manager 글자가 포함된 사원의 
-- 사원번호,사원명,직급id,직급명,월급,최대월급
select employee_id, emp_name, a.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id = b.job_id and job_title like '%Manager%'
order by employee_id;


-- ERD 예제로 조인 만들어보기
-- select user.user_id, user_name, user_phone, user_address1, user_address2, user_address3
-- from user,deliver_address
-- where user.user_id = deliver_address.user_id;

-- NON-EQUI JOIN 같은 컬럼이 없는?

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);

commit;

select * from stu_grade;

select avg from stu_score;

-- case 문 사용해서 grade 컬럼 
select no,name,avg,
case
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
when avg >=60 then 'D'
else 'F'
end as grade
from stu_score
order by no  ;

update stu_grade set low_score = 92
where grade = 'A';
update stu_grade set low_score = 82, high_score=91
where grade = 'B';
update stu_grade set high_score=71
where grade = 'D';

-- 지역별 대출액 합계
select region,gubun,sum(loan_jan_amt) from kor_loan_status
group by region, gubun
order by region ;

-- 연도별, 지역별 대출합계금액
select substr(period,1,4),region,sum(loan_jan_amt) from kor_loan_status
group by substr(period,1,4), region 
order by region;

select * from kor_loan_status order by period;

-- 부서별 월급의 합계
select department_id,sum(salary) a from employees 
group by department_id
order by a;

-- 시간대, 연령대별 판매량 총 합을 출력
select * from lotte_product;

select time_cd,age_cd,sum(purh_amt) a from lotte_product
group by time_cd,age_cd
order by a desc;

select * from shop_product
where pdate >= '2024/03/01'
order by pdate;

-- 2024/03/01이후 이름별 금액 합계를 구하기
select name,sum(amount) from shop_product
where pdate >= '2024/03/01' 
group by name;

-- non-equi join : 컬럼명이 같은것이 없는 테이블간의 조인
select no,name,avg,grade from stu_score,stu_grade
where avg between low_score and high_score
order by no;


-- customer_rank 테이블 생성
-- rank : 100만원 미만 bronze, 200 미만 silver 300 미만 gold, 300 이상 platinum

-- 240301이후 name,sum(amount),rank 출력 non-equi join 사용

create table customer_rank (
rank varchar2(10) primary key,
low_amount number(10) not null,
high_amount number(10) not null
);

insert into customer_rank values(
'PLATINUM',3000000,99999999
);

commit;

select * from customer_rank;


select name,s_amount,rank 
from
(select name,sum(amount) s_amount 
from shop_product
where pdate >= '2024/03/01'
group by name),customer_rank
where s_amount between low_amount and high_amount
;

select * from lotte_product
order by std_ym;

-- rownum : 순번을 새롭게 부여해서 출력 ,row_number() 
select rownum, std_ym,sex_cd,age_cd,time_cd,purh_amt from lotte_product
;

select rownum rnum,a.* from lotte_product a;

select rnum, std_ym,sex_cd,age_cd,time_cd,purh_amt from 
(select rownum rnum,a.* from lotte_product a) b -- rnum에는 번호가 부여되었다
where rnum >= 21 and rnum <= 30;


select rownum, b.* 
from(select * from lotte_product order by std_ym) b -- b는 날짜 asc로 미리 정렬됨
;

select * from stu_score
order by no;

-- kor 점수가 높은 순으로 21~30등 까지
select rnum, name,kor from
(select rownum rnum, c.* from
(select name,kor from stu_score order by kor desc) c) 
where rnum >=21 and rnum <=30
;

select name,kor from stu_score order by kor desc;

select rownum rnum, c.* from
(select name,kor from stu_score order by kor desc) c;


select * from stu_score 
where no >= 21 and no <= 30
order by no;

