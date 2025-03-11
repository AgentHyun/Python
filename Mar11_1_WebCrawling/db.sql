-- (table간 제약조건 고려 X)
-- 학생 : 이름, 생일, 몇 강의장 소속, 중간, 기말
create table mar11_student(
s_no number(2) primary key,
s_name varchar2(5char) not null,
s_birthday date not null,
s_class number(3) not null,
s_mid_test number(3) not null,
s_final_test number(3) not null
);
create sequence mar11_student_seq;
drop table mar11_student
select * from mar11_student





--------------------------------------------------
-- 강의장 : 몇 강의장, 강의장 위치
-- 1강의장 : 5층 복도 오른쪽 / 2강의장 : 5층 복도 왼쪽 끝
-- 3강의장 :5층 복도 왼쪽 첫번째 / 4강의장 : 6층 정면
-- 5강의장 : 8층 정면

create table mar11_class(
c_class number(3) primary key,
c_location varchar2(30 char) not null
);

drop table mar11_class
insert into mar11_class values(1, '5층 복도 오른쪽')
insert into mar11_class values(2, '5층 복도 왼쪽 끝')
insert into mar11_class values(3, '5층 복도 왼쪽 첫번째')
insert into mar11_class values(4, '6층 정면')
insert into mar11_class values(5, '8층 정면')

select * from MAR11_CLASS




















