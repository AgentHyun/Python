from cx_Oracle import connect

# 1. DB연결
con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe")

# 3. data확보!
# 로부스타 / 아라비카 / 리베리카
# 원두당 커피 3개씩 
n = input("커피 이름 : ")
p = int(input("가격 : "))
b = input("원두 이름 : ")

# 4. sql문 작성
#         Java : ?, ?
#         MyBatis : #{멤버변수명 } 
#         Python : 완성된 sql문을 사용!
#             sql문 끝나고나서 ;(세미콜론) 넣지 않는다!!!!!

sql = "insert into mar07_coffee values(mar07_coffee_seq.nextval,"
sql += " '%s', '%d', '%s')" % (n, p, b)

#5. DB관련 작업 (sql문을 서버로 전송, 실행, 결과 받기) : 총괄객체
#        Java : PreparedStatement (pstmt)
#        Python : cursor()

cur = con.cursor()

#6. 수행 (sql문을 서버로 전송, 실행, 결과 받기)
cur.execute(sql)

#7. 결과처리
if cur.rowcount == 1: #방금 작업때문에 영향을 받은 행 수가 1이면
    print("성공 ! ") # 성공
    con.commit()    #  commit을 해야 서버에 실제로 반영
    








# 2. DB연결 종료
con.close()
















