import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import time  # ⬅️ sleep을 위해 추가

# 검색어 입력
query = input("검색어 입력: ")
encoded_query = quote(query)  # 한글 URL 인코딩

# 1~5페이지(50개 뉴스) 반복 크롤링
for page in range(1, 6):
    start_num = (page - 1) * 10 + 1  # 1, 11, 21, 31, 41

    # 네이버 뉴스 검색 URL
    url = f"https://search.naver.com/search.naver?where=news&query={encoded_query}&start={start_num}"

    # 요청 보내기 (User-Agent 추가하여 차단 방지)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    # 페이지별 뉴스 제목 출력
    print(f"\n===== {page} 페이지 뉴스 제목 =====")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # 뉴스 제목 가져오기
        titles = soup.select(".news_tit")  

        for idx, title in enumerate(titles, start=1 + (page - 1) * 10):
            print(f"{idx}. {title.text}")  # 뉴스 제목 출력
    else:
        print(f"페이지 {page} 요청 실패")

 
