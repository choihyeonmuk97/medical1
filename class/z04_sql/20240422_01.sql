select * from employees;

select employee_id,emp_name from employees;

-- type = number 인 경우 사칙연산 가능
select salary,salary*1400 k_sal,salary*1400*12 as y_sal from employees;
-- as 별칭 : 컬럼명을 별칭을 부여 as 생략 가능

select * from stu_score;

-- 파이썬으로 연결하면 컬럼 이름이 변수명으로 넘어온다 

select department_id from employees;

-- null : 0 일수도 있고 무한의 값 일 수도 있음 -> value를 알 수 없음!!
-- Nvl() : null value -> 값이 null 인 경우 value 값을 부여해줌
select nvl(department_id,0) from employees;

select salary,salary + (salary*nvl(commission_pct,0)) as "Real_sal" from employees;
-- oracle은 대소문자의 구별이 없음! 별칭(변수명)에 대소문자 구별을 하고 싶으면 ""를 붙여야함(특수문자 사용 가능)

select salary as 월급 from employees; 
-- as 한글 가능하나 가급적 별칭에 한글은 지양함 (에러가 날 수 있음)

select * from departments;

select department_id, department_name from departments;

-- concat (||) : 데이터를 하나로 합칠 때 사용 
-- split() : 데이터를 분리시킴
select kor||','||eng||','||math stu from stu_score; 

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- 중복제거 distnct
-- 조건절 where
select distinct department_id from employees where department_id is not null;

select distinct manager_id from employees where manager_id is not null;


select employee_id,salary from employees
where employee_id = 200 or employee_id = 201 or employee_id = 202;

select * from employees
where employee_id >= 200 and employee_id <= 203;

select * from employees
where employee_id <= 150 or employee_id >= 200;

select * from employees
where department_id = 10 or department_id = 30 or department_id = 50;

-- salary 6000~9000
select * from employees
where salary >= 6000 and salary <= 9000 order by salary desc;
-- 정렬 : order by comn asc(순차정렬), desc(역순정렬)

-- salary = 6000,7000,8000
select * from employees
where salary = 6000 or salary = 7000 or salary = 8000;

-- department_id = 50 and salary >= 8000
select * from employees
where department_id = 50 and salary >= 8000;

-- stu_score name = 홍길동
select * from stu_score
where name = '홍길동';

select hire_date from employees
order by hire_date asc;

select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date >= '02/01/01' order by hire_date asc;

select hire_date, hire_date+100 from employees;
select round(sysdate-hire_date,2) from employees;

select * from employees;

-- concat
select emp_name || email from employees;

-- hire_date 05~06y and salart >= 6000 / order by desc
select * from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >= 6000
order by hire_date desc;

-- not 연산자 -> !=, <>, ^=, not(comn 앞에 붙어야함)
select department_id from employees
where department_id != 10 and NOT department_id = 50
order by department_id;

-- salary 5000~9000
select emp_name,salary from employees
where salary >= 5000 and salary <= 9000
order by salary;

-- avg >= 99
select * from stu_score
where avg >= 99;

select * from students;

update students set name = '관순스'
where no = 10;

commit;

-- kor >= 70 and avg >= 75
select * from students
where kor >= 70 and avg >= 75 order by avg;

-- kor = 80 and 70 and 90
select * from students
where kor = 70 or kor = 80 or kor = 90
order by kor;

update students set kor = 100
where no = 1;

rollback;

update students set kor = 100, total = 100+eng+math, avg = (100+eng+math)/3
where no = 1;

select * from students;

-- kor 80~90
select * from students
where kor >= 80 and kor <= 90 order by no;

-- between a and b : a <= value <=b, a 와 b의 값은 무조건 포함
select * from students
where kor between 70 and 90; 

-- not between a and b a < value and value < b , a,b 값 포함되지 않음
select * from students
where kor not between 70 and 90; 

select emp_name,hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date;

-- in : 동일한 필드에서 여러개의 값 중 하나가 필요한 경우 
select name,kor from students
where kor in (70,80,90);

-- like 검색 : 특정단어가 포함되어 있는 것을 검색. %를 끝에 붙이면 그 단어로 시작하는 단어 검색
select * from students
where name like '홍%';

-- %단어 : 해당 단어로 끝나는 단어를 검색
select * from students
where name like '%순';

-- %단어% : 해당 단어가 포함 되어 있으면 검색
select * from students
where name like '%길%';

-- _ : 1칸을 의미함
select * from students
where name like '_길%';

-- 3번째에 't' 포함
select * from students
where name like '__t%';

-- 이름이 4자리고 3번째에 'r'
select * from students
where name like '__r_';

select * from students
where name like '__r%' and length(name) = 4;

-- 이름이 A로 시작
select * from students
where name like 'A%';

-- 이름에 a가 들어있는
select * from students
where name like '%a%';

-- 대소문자 구분 없이 a가 포함 
-- > 치환 !! lower() : 소문자 / upper() : 대문자 / initcap : 첫글자만 대문자로 치환
select * from students
where lower(name) like '%a%';

-- a,A가 포함되지 않은
select * from students
where lower(name) not like '%a%';

select * from employees
where manager_id = 100;

-- null 값은 등가비교 할 수 없음
select * from employees
where manager_id = null;

-- is null 을 이용하여 값이 null 인 것을 출력할 수 있음 
select * from employees
where manager_id is null;

-- 정렬 한글도 가능!
select name from stu_score
order by name asc;

-- 동시 정렬 : 첫번째 조건 먼저 실행 후 두번째 조건 실행함
select * from students
order by kor desc, eng asc;

select * from students
order by total desc;

-- 컬럼 추가
alter table students add rank number(3);

select * from students;

update students set rank = 0 ;

commit;

-- 등수 매기기
select no,rank() over(order by total desc) rank from students;

-- 등수를 테이블로 넣기
update students s1 set rank = (
select ranks from (select no, rank() over(order by total desc) as ranks from students) s2
where s1.no = s2. no);


update students set rank = 13
where no = 1;

select * from students;

