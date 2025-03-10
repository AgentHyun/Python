create table mar07_coffee(
 c_no number(3) primary key,
 c_name varchar2(10 char) not null,
 c_price number(5) not null,
 c_bean varchar2(10 char) not null


);
create sequence mar07_coffee_seq;

select * from MAR07_COFFEE;
select count(c_name), AVG(c_price) from mar07_coffee where c_bean = '아라비카';

select AVG(c_price) from mar07_coffee where c_price >= 3000 and c_price <= 5000 order by C_PRICE
update mar07_coffee set c_price = c_price + 5000 where c_bean = '아라비카'


create table mar10_weather(
w_no number(3) primary key,
w_time varchar2(100 char) not null,
w_temp varchar2(100 char) not null,
w_max varchar2(100 char) not null,
w_min varchar2(100 char) not null,




);






