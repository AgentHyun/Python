# 각각의 커피 이름, 가격, 원두 정보 가격 오름차순으로 정렬해서 출력
from cx_Oracle import connect

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe")

sql = "select c_name, c_price, c_bean from mar07_coffee order by c_price"

cur = con.cursor()

cur.execute(sql) # 수행하면 select의 결과가 cur에 tuple로 들어가게 됩니다.

# for c in cur:
#     print(c, type(c))

for n, p, b in cur:
    print(n, p, b)