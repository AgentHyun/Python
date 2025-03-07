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
weather = loads(resBody)
print(weather)










