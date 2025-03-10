#http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/5/
from http.client import HTTPSConnection, HTTPConnection
from json import load, loads
from cx_Oracle import connect


# 구 이름, 미세먼지, 초미세먼지의 정보를 db에 담아주세요
#     (여러 기간에 걸쳐 이 데이터를 모은다고 가정")
# MSRSTE NM, PM10, PM25


hc = HTTPConnection("openAPI.seoul.go.kr:8088")

url = "/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/";
hc.request("GET", url)
res = hc.getresponse()
resBody = res.read()
print(resBody.decode())
air = loads(resBody)
print(air)

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe"); 





for i in range(len(air["RealtimeCityAir"]["row"])):
    city = air["RealtimeCityAir"]["row"][i]["MSRSTE_NM"]
    dust = air["RealtimeCityAir"]["row"][i]["PM10"]
    tiny_dust = air["RealtimeCityAir"]["row"][i]["PM25"]
    sql = f"insert into mar10_air values('{city}', {dust}, {tiny_dust})"

    cur = con.cursor()
    cur.execute(sql)    
 
if cur.rowcount == 1:
    print("삽입 완료")
    con.commit()
    
    
    








