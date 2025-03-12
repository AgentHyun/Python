create table mar12_location(
l_name varchar2(40 char) not null,
l_ph varchar2(40 char) not null,
l_x number(30, 6) not null,
l_y number(30, 6) not null



);
select * from mar12_location
drop table mar12_location

--nvl 함수 : null일때 지정한 값으로 대치하는 함수
--nvl(값, (값이) null일때 대체값
select nvl(null, '-'), nvl('null', '-'), nvl('', '-') from dual;


-- nvl2 함수 : null의 여부에 따라서 지정한 값으로 대치하는 함수
-- nvl2(값, 값이 있을때 대체값, 값이 없을 때 대체값)
select nvl2(null, 'A', 'B'), nvl2('null', 'A', 'B') from dual;










