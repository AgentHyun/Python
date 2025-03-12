from urllib.parse import quote
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect


q = quote(input("검색어를 입력 : "))


x = 37.5780858
y = 127.0069408

hc = HTTPSConnection("dapi.kakao.com")
headers = {
    "Authorization": "KakaoAK 8d2e282a4bd0da67042f8cfcf8ac3a51",
}

url = f"/v2/local/search/keyword.json?query={q}&x={x}&y={y}&radius=1000"
print(url)

hc.request("GET", url, headers=headers)
res = hc.getresponse()
resBody = res.read()
datas = loads(resBody)
data = datas['documents']

name = []
ph = []
x_data = []
y_data = []

for d in data:
    name.append(d['place_name'])
    ph.append(d['phone'] if d['phone'].strip() else "-")  
    x = round(float(d['x']), 6)
    x_data.append(x)  
    y = round(float(d['y']), 6)
    y_data.append(y)

con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe")
cur = con.cursor()

for i in range(len(name)):
    sql = f"INSERT INTO mar12_location (l_name, l_ph, l_x, l_y) VALUES ('{name[i]}', '{ph[i]}', {x_data[i]}, {y_data[i]})"
    cur.execute(sql)
    
print("삽입 완료!")
con.commit()
con.close() 
