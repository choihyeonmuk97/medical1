select * from students;

update students set id = 'aaa', name = '홍길동', gender = 'M'
where id = 'Timothee';

update students set id = 'Thresh', name = 'Lolbug', gender = 'M'
where id = 'bbb' and pw = '2864';

update students set id = 'ggg', name = '홍길자', gender = 'F'
where id = 'ggg';

commit;

select rownum,a.* from students a -- 이미 번호가 부여된 후 정렬됨 -> 번호가 뒤섞임
order by grade;

select rownum, b.* from
(select a.* from students a order by grade) b ; -- 정렬한 뒤 번호를 부여하여야 1번 부터 부여됨

-- 평균이 85점 이상이면서 no >= 500
select * from stu_score
where avg >= 85 and no >= 500
order by no;

select name,amount,pdate from shop_product
where pdate >= '2024/03/01';

-- 이름별 구매내역 합계
select name,sum(amount) from shop_product
where pdate >= '2024/03/01'
group by name;

select * from customer_rank;

-- non-equi join
select name,avg,grade from stu_score, stu_grade
where avg between low_score and high_score;

select name,s_amount,rank from 
(select name, sum(amount) s_amount from shop_product
where pdate >= '2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount;

-- row_number() : 정렬 후 번호 부여 가능
select * from(
select row_number() over(order by id) rnum,a.* from students a)
where rnum >= 11 and rnum <= 20
;

-- equi join
select employee_id, emp_name, a.department_id, department_name, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id
order by department_id;

select * from departments;

-- self join + equi join
select a.employee_id, a.emp_name,a.department_id, department_name, a.manager_id, b.emp_name 
from employees a, employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
order by a.employee_id;

-- self join
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

-- Guy Himuro 과 동일한 부서에 근무하는 사람을 출력
select * from employees
where emp_name = 'Guy Himuro'; -- dep.._id 30

select a.emp_name, a.department_id, b.department_id, b.emp_name 
from employees a, employees b
where a.department_id = b.department_id and a.emp_name = 'Guy Himuro';

select a.department_id,c.department_name,b.emp_name from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name = 'Pat Fay' and a.department_id = c.department_id;


select * from member;

insert into member values(
member_seq.nextval,'ggg','1111','홍길순','여자',sysdate
);

commit;

rollback;

update member set name = '홍길동' where id = 'aaa';

-- 테이블 생성
create table mem (id varchar2(30) primary key ,pw number,name varchar2(30),mdate date);

select * from mem;

-- 웹스크래핑 DB 저장
create table yeogi (
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(500),
price number
);

drop table yeogi;

select * from yeogi;