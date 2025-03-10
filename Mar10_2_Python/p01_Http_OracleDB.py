#https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4122066000
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect


#기상청 XML 

hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4122066000") 

res = hc.getresponse() 
resBody = res.read() 

#기상청 XML => DB에 적재
# 시간대 /기온 /최고 기온/ 최저기온 정보 담기

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe"); 
for w in fromstring(resBody).iter("data"):
    time = w.find("hour").text
    temp = w.find("temp").text
    max = w.find("tmx").text
    min = w.find("tmn").text
    sql = "insert into mar10_weather values(mar10_weather_seq2.nextval,"
    sql += f"{time},{temp},{max},{min})"
    cur = con.cursor()
    cur.execute(sql)   


if cur.rowcount == 1:
        print("삽입 성공!")
        con.commit()


    
con.close()























