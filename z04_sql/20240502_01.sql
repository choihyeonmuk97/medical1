-- equi join .. 아래는 테이블 리셋이슈로 무시
select employee_id, emp_name,a.department_id,b.department_name
from employees a, departments b
where a.department_id = b.department_id;

alter table students add no number(38); -- no commit
--update students set no = 
--(select rnum  from 
--(select rownum rnum, a.* from students a));

drop table students;

-- 홍길동의 학생성적 모든 내용과 전화번호,이메일,과목,학년 -> 테이블 리셋했다 ㅋㅋ
select * from stu_score order by no;

-- rank() 함수
select ranks from (select no,id,rank() over(order by total desc) as ranks,rank,total from stu_score);

update stu_score a 
set rank = (select ranks 
from (select no,id,rank() over(order by total desc) as ranks,rank,total from stu_score) b 
where a.no = b.no);

select * from stu_score;

-- table reset
select a.*,phone,email,major,grade from stu_score a, students b
where a.name = b.name and a.name = '홍길동';

select a.id,a.name,phone,total,avg from stu_score b, students a
where a.id = b.id
order by name;

select * from students;

select * from member;

alter table member add no number;

select rownum,a.* from member a;

update member a set no =( select rnum 
from(select rownum rnum, id from member)b
where a.id = b.id);

update stu_score set rank = 0;

commit;

select total,rank from stu_score order by total desc;

select total, rank() over(order by total desc) ranks from stu_score;

-- rank update ㅡㅡ
update stu_score a 
set rank = (select ranks from
(select no,rank() over(order by total desc) ranks from stu_score) b
where a.no = b.no);

select * from stu_score;
-- row_number() over()

select * from
(select row_number() over(order by total desc) rnum, a.* from stu_score a)
where rnum >=11 and rnum <=20; 


select * from
(select rownum rnum, a.* from
(select * from stu_score order by total desc) a)
where rnum >=11 and rnum <=20;

-- self join
select * from employees;

-- 매니저의 이름을 알고 싶다!!
-- outer join : 값이 충족되지 않아도 (null) 출력해줌
-- null 값이 있는 반대편 항목에 (+) 기호를 넣는다
select a.employee_id,a.emp_name,a.department_id, a.job_id, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id(+) 
order by department_id;


-- equi join, outer join 기본 sql 구문에선 left,right,full 불가
select  emp_name, b.department_id,department_name from employees a, departments b
where a.department_id(+) = b.department_id 
order by department_id;
-- ansi left,right outer join, full outer join
select a.emp_name, a.manager_id, b.emp_name from employees a 
left outer join employees b
on a.manager_id = b.employee_id;

select department_id from departments;

-- ansi join // cross
select * from employees cross join departments;
select * from employees, departments; -- 위 아래 같음 테이블의 행 갯수는 두 테이블 행 갯수의 곱임

select a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id; -- equi
-- ansi inner join on~
select a.department_id,department_name 
from employees a inner join departments b
on a.department_id = b.department_id;
-- join using()~
select department_id,department_name 
from employees join departments 
using (department_id);
-- ansi natural join
select department_id, department_name
from employees natural join departments;
