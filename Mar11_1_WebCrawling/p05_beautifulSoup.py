from bs4 import BeautifulSoup

# cmd => pip install bs4
# Beautiful Soup :
#     파이썬에서 사용할 수 있는 웹데이터 크롤링 라이브러리

htmlEx = """
<html>
<head>
<meta charset="UTF-8">
<title>우리는 bs4로 Web Crawling을 할거에요!</title>
</head>
<body>
<h1>다들 식사 후라 피곤하시겠지만</h1>
<h2>조금만 더 힘내주세요 ! </h2>
<p><b>Beautiful Soup</b></p>
<p>Python에서 Crawling할 때 유용하게 사용할 수 있는 Library
<a href="#">구글</a>
<a href="#">네이버</a>
<a href="#">유튜브</a>
</p>
<p>How to use bs4</p>   
</body>
</html>
"""


# bs4 초기화
# html.parser : HTML 문법 규칙에 따른 문자열,
#               해당 문법을 바탕으로 단어의 의미나 구조를
#               분석하는 프로그램 중 하나
soup = BeautifulSoup(htmlEx, 'html.parser')

# print(soup)

# 코드 예쁘게 정리하기 - prettify()
#print(soup.prettify())

# title태그 찾기
title = soup.html.head.title
print(title)
print(title.string) #title의 내용만
print(title.text)
print(title.getText())
print("-------------------------------------")

#h1 태그의 내용
h1 = soup.html.body.h1
print(h1.text)


print("-------------------------------------")
# 첫번째로만나는 p태그의 내용
p = soup.html.body.p

print(p.text)
print("-------------------------------------")

#next_sibling : 동일한 레벨 상의 다음 요소를 불러올 수 있는 기능
#             <-> previous_sibling
# 태그와 태그사이에 개행이 있는 경우, 엔터처리 취급함
#            => 요소로 인식을 함 
p2 = p.next_sibling.next_sibling
print(p2)
print(p2.text)




