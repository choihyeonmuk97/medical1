select * from stu_score where id like '%a%'
order by no;

select count(*) from stu_score where id like '%a%';

-- row_number() 이름에 a가 들어간
-- 11~20
select * from(select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%') where rnum >= 11 and rnum <= 20;

select count(*) from(select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%');

create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number
);

select * from melon;

create table yanolja(
yno number primary key,
img varchar2(300),
title varchar2(100),
grade number,
grade_num number,
price number
);

alter table melon modify img varchar2(300);