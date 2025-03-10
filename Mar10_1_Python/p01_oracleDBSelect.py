#커피테이블
# input으로 숫자 2개를 입력 => 가격순 (오름차순)으로 정렬해서
#     =>시작 부터 끝값까지 평균 가격을 출력
from cx_Oracle import connect


num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자:"))

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe");

sql = "select AVG(c_price) from"
sql +="(select rownum as rn, c_price from(select c_price from mar07_coffee order by c_price))"
sql += f"where rownum between {num1} and {num2}" 

cur = con.cursor()

cur.execute(sql) 

for c in cur:
    for j in c:
        
        print("%.1f"%j)













