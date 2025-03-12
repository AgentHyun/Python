from urllib.parse import quote
import requests
from bs4 import BeautifulSoup



def getTitle(addr, q):
    for i in range(1, 6):
        print(f"============={i}페이지==================")
                   
        address = addr + q + f"&p={i}"
        print(address)
        res = requests.get(address)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        ul = soup.select_one("ul.c-list-basic")
   
       
        news = ul.select("li > div > div > div > strong > a")
        for i in news:
            print(i.get_text())


url ="https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="
query = quote(input("검색어 입력: "))

getTitle(url, query)
    





