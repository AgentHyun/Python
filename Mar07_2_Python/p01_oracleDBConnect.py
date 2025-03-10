from cx_Oracle import connect


# OracleDB와 연동이 되는 Java : instantClient에 있는 ojdbc8.jar
# OracleDB와 연동이 되는 Python : cx_oracle.py(가 instantClient를 사용)

# 기본적으로 python에는 oracleDB 연결 기능이 없음
# cx_oracle.py => ojdbc8.jar를 사용
# 시작 - cmd - ' pip install cx_oracle'

#sqlplus로 접속할 때 사용하는 주소
#    sqlplus [ID]/[PW]@[IP Address]:[PORT]/[SID]
#    sqlplus ekdh3904/fogus12@192.168.0.12:1521/xe
try:
    c = connect("ekdh3904/fogus12@192.168.0.12:1521/xe")
    print("Success !")
except Exception as e:
    print(e)
c.close()
















