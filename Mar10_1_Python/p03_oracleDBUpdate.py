from cx_Oracle import connect

# input 2개 : 원두 이름 검섹 / 숫자를 입력
# 검색한 원두를 사용하는 커피들의 가격을 => 입력한 숫자만큼 인상


bean = input("원두 이름 : ")
price = input("올릴 가격 : ")

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe");
   
sql = f"update mar07_coffee set c_price = c_price + {price}";
sql += f" where c_bean = '{bean}'";

cur = con.cursor()
cur.execute(sql)

if cur.rowcount >= 1:
    print("Success !")
    con.commit()
sql = "select * from mar07_coffee order by c_no "
cur.execute(sql)
for c in cur:
    print(c)








con.close()





