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
books = books["documents"]
# 필요한 데이터 챙긴 후,
# 책 이름 검색해서 책 제목 - 작가 / 할인가 / 도서 소개 출력
for b in books:
 #   print(b['title'], "-", b["authors"][0])
    print(b["title"], "-", ",".join(b["authors"]))
    #.join() : list를 문자열로
    # 구분자.join() : list의 요소들을 지정한 구분자로 나눠
    # 하나의 문자열로 합쳐줌
    #ex) ", ".join(['a', 'b', 'c']
   
    print(b['sale_price'])
    print(b['contents'])

    











