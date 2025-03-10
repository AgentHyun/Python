from cx_Oracle import connect

# DB 연결 => 커피 이름, 가격, 원두 정보 => .csv파일로 생성(, 를 기준으로 데이터를 나눔_
# ex) 이름 , 가격 , 원두
#     이름 , 가격 , 원두
#     ...
   
con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe");   
sql = "select c_name,c_price,c_bean from mar07_coffee";

cur = con.cursor();
cur.execute(sql);
file = open("C:/Users/sdedu/Desktop/메추라기/coffee2.csv", "w", encoding="UTF-8")


for n, p, b in cur:
    print(n, p, b)    
    file.write(f"{n}, {p}, {b} \n")
print("완료")
        
file.close()
con.close()    
        
        
    






















