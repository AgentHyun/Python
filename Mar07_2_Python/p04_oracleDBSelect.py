#원두 이름을 검색해서
# 그 원두를 사용하는 커피의 종류 갯수, 평균가를 출력
from cx_Oracle import connect


con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe");

bean = input("커피 원두는 : ");
sql = "select count(c_name), AVG(c_price) from mar07_coffee ";
sql += f"where c_bean = '{bean}'";

print(sql)

cur = con.cursor()

cur.execute(sql) 

for c in cur:
    print(c)








