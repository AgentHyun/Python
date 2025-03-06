from urllib.parse import quote, quote_plus
from xml.etree.ElementTree import fromstring
from http.client import HTTPSConnection

#https://openapi.naver.com/v1/search/shop.xml
#sConcC52NqQqm4kY_QnA
#3KrYMEcEMg

hc = HTTPSConnection("openapi.naver.com")

#상품명 : 입력
# xml 파싱해서 
# 문서의 상품 이름 / 최저가 / 브랜드 / 대분류 카테고리 정보를 출력
q = input("상품명 : ")
q = quote(q)
print(q)

url = f"/v1/search/shop.xml?query={q}"

headers = {
    "X-Naver-Client-Id": "sConcC52NqQqm4kY_QnA",
    "X-Naver-Client-Secret": "3KrYMEcEMg"
}

hc.request("GET", url, headers = headers)
res = hc.getresponse()
resBody = res.read()
#print(resBody.decode())
for w in fromstring(resBody).iter("item"):
    print("===============================")
    print(w.find("title").text.replace("<b>","").replace("</b>", ""))
    print(w.find("lprice").text)
    print(w.find("brand").text)
    print(w.find("category1").text)






