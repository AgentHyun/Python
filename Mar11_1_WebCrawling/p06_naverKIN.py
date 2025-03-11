#https://kin.naver.com/search/list.naver?query=
# %EB%AF%B9%EC%8A%A4%EB%A7%88%EC%8A%A4%ED%84%B0
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

q = quote(input("검색어 : "))
print(q)

url = f"https://kin.naver.com/search/list.naver?query={q}"

# cmd => pip install requests
# requests : 간편하게 HTTP 요청을 하기위해서 사용하는 모듈

response = requests.get(url) # get() : GET방식 요청
#print(response.status_code)

if response.status_code == 200:
    html = response.text
    print(html) 

    soup = BeautifulSoup(html, "html.parser")
    
    #select_one을 사용한 경우 : 문서의 처음부터 찾게 되며,
    #                        가장 처음에 만나는 해당 selector를 불러옴
    
    ul = soup.select_one("ul.basic1")

    # select() : 해당하는 selector들의 모든 내용이 list에 담김
    # > : 그 하위에 있는 selector들 전부 다!
    titles = ul.select("li > dl > dt > a")

    for title in titles:
        print(title.text)
else:
    print(response.status_code)













