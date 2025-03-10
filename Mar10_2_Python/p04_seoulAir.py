# DB에 있는 미세먼지 데이터 => CSV에 저장(데이터 콤마로 구분)
from cx_Oracle import connect

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe"); 

cur = con.cursor()

sql ="select * from mar10_air"

cur.execute(sql)
file = open("C:/Users/sdedu/Desktop/메추라기/air2.csv", "w", encoding="UTF-8")
file.write("구 이름, 미세먼지,초 미세먼지\n")

for city,dust,tiny_dust in cur:
    file.write(f"{city}, {dust}, {tiny_dust} \n")











