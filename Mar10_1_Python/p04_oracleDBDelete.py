from cx_Oracle import connect

#select 번호순으로 조회 => 번호를 입력하면 => 그 데이터가 삭제!
# 999를 입력하게 되면 프로그램이 종료 => 종료하기 전까지 반복

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe");

while True:
    
    sql = "select * from mar07_coffee order by c_no "

    cur = con.cursor()
    cur.execute(sql)
    for c in cur:
        print(c)
    num = int(input("넘버 : "))
    if(num == 999):
        print("종료!")
        break
    sql = f"delete from mar07_coffee where c_no = {num}"
    cur.execute(sql)    
        
    if cur.rowcount == 1:
        print("삭제 성공!")
        con.commit()

    

con.close()













