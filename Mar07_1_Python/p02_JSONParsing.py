from urllib.parse import quote
from http.client import HTTPSConnection
from json import loads


#8d2e282a4bd0da67042f8cfcf8ac3a51

#https://dapi.kakao.com/v3/search/book?query=


#Authorization: KakaoAK ${REST_API_KEY}

q = input("책 이름 : ")
q = quote(q)

url = f"/v3/search/book?query={q}"

headers = {
    "Authorization": "KakaoAK 8d2e282a4bd0da67042f8cfcf8ac3a51",
}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", url,  headers = headers)
res = hc.getresponse()
resBody = res.read()
books = loads(resBody) 
print(books)

# 필요한 데이터 챙긴 후,
# 책 이름 검색해서 책 제목 - 작가 / 할인가 / 도서 소개 출력

print(books['documents'][0]['title'])
print(books['documents'][0]['authors'])
print(books['documents'][0]['sale_price'])
print(books['documents'][0]['contents'])











