alter session set "_ORACLE_SCRIPT"=true;

-- 사용자 생성 시 따옴표 쓰면 안됨!!!
CREATE USER ora_user IDENTIFIED BY 1111;

-- 권한 부여하기
grant connect, resource, dba to ora_user;

-- 사용자 삭제
drop user ora_user CASCADE;

-- 권한 삭제
revoke connect, resource, dba from ora_user;
