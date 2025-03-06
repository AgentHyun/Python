#https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4122066000
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring


# Http 통신

hc = HTTPSConnection("www.kma.go.kr") # 서버 주소(KR까지)
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4122066000") #요청(요청 방식, 나머지 주소값)

res = hc.getresponse() # 응답
resBody = res.read() # 응답 내용 읽기

#print(resBody)

#print(resBody.decode()) # 출력(한글처리)

####################################################


# XML Parsing
# DOM객체 여러개 찾기 : .getiterator("태그명") / .iter("태그명")
# DOM객체 하나 찾기 : .find("태그명")

# XML Data -> Python str
kmaWeather = fromstring(resBody)
#print(kmaWeather)

weather = kmaWeather.iter("data")
#print(weather)
#for w in weather:
#    print(w)

for w in fromstring(resBody).iter("data"):
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    print(w.find("wdKor").text)
    print("----------------------")











