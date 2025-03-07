#42008a8c8e7402a3fc9d3b1a7df8fee9
#https://api.openweathermap.org
#/data/2.5/weather?q={city name}&appid=42008a8c8e7402a3fc9d3b1a7df8fee9
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads

# 도시 이름 : 입력 (영어)
# 요청파라미터 추가 O
# 응답 내용 출력까지

hc = HTTPSConnection("api.openweathermap.org")
q = input("도시 이름 (영어):")

print(q)

url = f"/data/2.5/weather?q={q}&appid=42008a8c8e7402a3fc9d3b1a7df8fee9" 
url += "&units=metric&lang=kr"
print(url)
hc.request("GET", url)
res = hc.getresponse()
resBody = res.read()
print(resBody.decode())

# JS => Python
weather = loads(resBody) #JSON 데이터를 파이썬의 문자열로 변환 import json
print(weather)

#dict : {"key" : "value"}
#list : 인덱스 번호로 접근
l = [1,2,3] #python : list / JS : array
d = {"name" : "홍길동","age" : 17} #python : dict / JS : object
#############################################################################

# 날씨 / 기온 / 체감기온 / 습도 / 바람속도


#weather라는 속성은 dict안에 들어있는 weather라는 0번째리스트안에있는
#객체임

print(weather["weather"][0]["description"])
print(weather["main"]["temp"])
print(weather["main"]["feels_like"])
print(weather["main"]["humidity"])
print(weather["wind"]["speed"])

        











