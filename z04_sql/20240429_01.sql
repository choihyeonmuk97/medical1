
-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check...
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

-- 데이터 입력, 출력, 수정, 삭제 
insert into member (memNo, id, pw, name, gender, mdate) values(
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);

insert into member (memNo, id, pw, name, gender) values(
member_seq.nextval,'bbb','1111','유관순','여자'
);

insert into member values(
member_seq.nextval,'ccc','1111','이순신','남자',sysdate
);

create table board (
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- 외래 키 (foreign key)의 별칭 : fk_id
references member(id) -- member 테이블의 primary key id
);

-- primary key를 삭제하려면 foreign key에 등록되어 있는 데이터를 모두 삭제해야함.
-- 모두 삭제하는 방법 : on delete cascade, 모두 남겨두는 방법 : on update cascade

insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','제목','내용',sysdate,board_seq.currval,0,0,1,''
);


insert into board values(
board_seq.nextval,'bbb','제목2','내용2',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values(
board_seq.nextval,'aaa','제목3','내용3',board_seq.currval
);

select * from board;
-- row delete
delete board where bno=3;

commit;

select * from member;

-- DECODE 조건문 : 무조건 맞아야 한다 // switch case 랑 같다
select emp_name,department_id ,
decode(department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부') as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;
-- 90점 : A, 80점 : B, 70점 : C
select avg, 
decode(avg,
90,'A',
80,'B',
70,'C') as grade
from stu_score order by avg desc;

-- sh_clerk : salary * 15%, ad_asst : salary * 10%, mk_rep * 5%
select job_id, salary,
decode(job_id,
'SH_CLERK' , salary+salary*0.15,
'AD_ASST', salary+salary*0.1,
'MK_REP', salary+salary*0.05) as bonus
from employees;

-- job_id에 CLERK 이 포함된 것을 검색..
select job_id, salary from employees
where job_id like '%CLERK%'; -- ___CLERK% 


-- case when 조건 then 결과 else end // if문과 같다
select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id, department_name from departments;

-- case 사용 department_id 이름 출력
select department_id,
case
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then '구매/생산부'
when department_id = 40 then '인사부'
when department_id = 50 then '배송부'
else '기타'
end as dep_id
from dpartments;

-- CLERK : 15%, ASST : 10%, REP : 5%, MAN : 2%
select job_id, salary,
case
when job_id like '%CLERK%' then salary+salary*0.15
when job_id like '%ASST%' then salary+salary*0.1
when job_id like '%REP%' then salary+salary*0.05
when job_id like '%MAN%' then salary+salary*0.02
else salary
end as bonus
from employees order by bonus asc;

-- salary 평균 이하 = 15%, 이상 = 5%
select emp_name,salary,인상1, 
case
when salary < (select avg(salary) from employees) then salary+salary*0.15
when salary >= (select avg(salary) from employees) then salary+salary*0.05
end as 인상
from (select emp_name,salary, --avg(salary),
case
when salary < 6461 then '15%'
when salary >= 6461 then '5%'
end as 인상1
from employees
order by 인상1 asc)
order by 인상 asc;  -- 둘 합치기 ( 아래 조건을 테이블로 ) 


select emp_name,salary, --avg(salary),
case
when salary < 6461 then '15%'
when salary >= 6461 then '5%'
end as 인상
from employees
order by 인상 asc;


-- 다중 case 가능하다
select emp_name,salary, 
case
when salary < (select avg(salary) from employees) then '15%up'
when salary >= (select avg(salary) from employees) then '5%up'
end as salary_updown,
case
when salary < (select avg(salary) from employees) then salary+salary*0.15
when salary >= (select avg(salary) from employees) then salary+salary*0.05
end as salary_up
from employees
order by salary asc;  -- 둘 합치기 

select * from stu_score;

select total,rank from stu_score
order by total desc;

-- rank() 함수 : 등수매기기
select total,rank() over (order by total desc) as ranks from stu_score;

select no,rank() over (order by total desc) as ranks from stu_score;

select total,rank from stu_score order by total desc;

update stu_score set rank = 1
where total=295;

-- 1,000명의 순위를 각각 입력
update stu_score a 
set rank = (
select ranks from (
select no,rank() over (order by total desc)as ranks from stu_score
) b
where a.no = b.no
);

commit;

select no,total,rank from stu_score order by total desc;

select emp_name,department_id from employees;
select department_id, department_name from departments;

-- 두 테이블 조인 !!
select emp_name, employees.department_id, department_name from  employees,departments
where employees.department_id = departments.department_id;

-- 두 테이블 조인해서 출력
select a.department_id, department_name from employees a , departments b
where a.department_id = b.department_id;

-- 그룹함수 : avg,sum,count,max,min, stddev - 표준편차, variance - 분산

-- 월급의 총 합
select sum(salary) from employees;
-- sum(kor)
select sum(kor) from stu_score;

select count(*) from employees;

select count(*) from employees
where department_id = 50 ;

-- commission 받는 사원 수?
select * from employees
where commission_pct is not null; -- commission이 있는 사원만 출력

select count(*) from employees
where commission_pct is not null;

select count(*) from employees
where department_id = 20;

select department_id,count(department_id) from employees
group by department_id
order by department_id asc;


-- avg 90점 이상 a, 80 b, 70 c, 60 d, f
select name,avg ,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade 
from stu_score;

-- A 몇명인지
select grade,count(grade) from(
select avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade  
from stu_score
)
group by grade order by grade asc
;

-- kor 
select kor,(trunc(kor,-1)) from stu_score
order by kor desc;

-- 90점 몇명인지?
select count(trunc(kor,-1)) from stu_score
where trunc(kor,-1) = 90;

select trunc(kor,-1),count(*) from stu_score
where trunc(kor,-1) = 90
group by trunc(kor,-1);

-- 각 점수대 몇명인지
select trunc(kor,-1),count(*) from stu_score
group by trunc(kor,-1)
order by trunc(kor,-1) asc;

select k_kor, count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor; -- 그룹바이에 컬럼명 별칭 쓰는 방법

select department_id, count(*) from employees
group by department_id
order by department_id;

-- 부서별 평균 월급
select * from employees;
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id;

-- CLERK, REP, MAN 각각 월급 평균 구하기
select job_id, avg(salary) from employees
where job_id like '%CLERK%'
or job_id like '%REP%'
or job_id like '%MAN%'
group by job_id
order by job_id ;

-- CLERK 만 출력 되도록..
select substr(job_id,4,7), count(*) from employees
where job_id like '%CLERK%'
group by substr(job_id,4,7);

select substr(job_id,4,7) as job_id, count(substr(job_id,4,7)) as c_job_id from  employees
where substr(job_id,4,7) = 'CLERK'
group by substr(job_id,4,7);

 -- 부서별 최대월급, 최소월급, 평균월급
 select department_id, max(salary), min(salary), round(avg(salary),2) 
 from employees
 where department_id is not null 
 group by department_id 
 order by department_id;
 
select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

select department_id, commission_pct from employees
where commission_pct is not null;

-- 부서별 사원 수, 커미션을 받는 사원 수
select department_id, count(department_id),count(commission_pct) from employees
group by department_id
order by department_id;

-- having : group by 조건절, where : 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

-- emp_name 두번째 글자가 a로 시작하지 않는 것은 제외
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- 부서별 최대 월급이 8000 이상
select department_id, max(salary) from employees
group by department_id
having max(salary) >= 8000
order by max(salary);

-- 조인 : 테이블 2개를 연결
select emp_name,department_id,salary from employees;
select department_id, department_name from departments;

select count(*) from employees,departments;

-- EQUI JOIN : 두 테이블간 같은 컬럼을 가지고 비교해서 해당되는 데이터를 출력
select employee_id, emp_name, employees.department_id,department_name,salary 
from employees , departments
where employees.department_id = departments.department_id;

select department_id,department_name from departments;

select id,name from member;
select id,btitle,bcontent from board;

update member set name = '홍길자'
where id = 'aaa';

select bno,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board,member
where member.id = board.id;

