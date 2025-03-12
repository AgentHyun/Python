import requests
from bs4 import BeautifulSoup

# sss = ["ㅋㅋㅋ", "ㅁㅁㅁ", "ㅂㅂㅂ", "ㅎㅎㅎ", "ㅁㅁㅋㅋㅋ", "ㄹㄹㄹ"]
# for s in sss:
#     # 찾는 문자열이 존재하는 경우 : 그 문자열이 있는 인덱스값을 리턴
#     # 찾는 문자열이 존재하지 않는 경우 : -1 리턴
#     print(s.find("ㅋㅋ"))

# 조조(맹덕), 유비(현덕), 손권(중모)
# 책을 훑어보면서... => 위의 인물들이 몇 번 언급되는지 카운팅하기!
# 인물, 언급횟수 의 형태로 => csv파일에 저장

# 텍스트 파일 열고 - 찾고 - 저장

# 파일명을 저장할 변수
filename = None

# 한줄한줄 중복 있을 수 있음
line, word = None, None  # 한 줄(line)과 단어(word)를 저장할 변수 (초기화)

# 카운팅을 위한 dict를 만들어주겠습니다
wc = {"조조" : 0, "유비" : 0, "손권" : 0}

# 1번 파일부터 10번 파일까지 반복하면서 처리
for i in range(1, 11):
    filename = "C:/Users/sdedu/Desktop/threekingdoms/tk%02d.txt" % i
    # 파일을 열어서 읽기
    with open(filename, "r", encoding="UTF-8") as f:
        # 파일의 모든 줄을 한 줄씩 읽어오기
        for line in f.readlines():
            # print(line)
            # 줄 끝에 있는 개행 문자(\n)를 제거 (한줄로 쭉)
            line = line.replace("\n", "")
            # print(line)
            # 한줄 한줄의 문장을 단어 단위로 나눌건데
            # 문장을 공백(띄어쓰기) 기준으로 단어별로 나누기
            line = line.split(" ")
            
            # 단어 리스트를 하나씩 확인하면서 특정 이름이 포함되어 있는지 검사
            for word in line:
                # print(word)
                # "조조" 또는 "맹덕"이라는 단어가 포함되어 있다면 조조 카운트 증가
                if word.find("조조") != -1 or word.find("맹덕") != -1:
                    wc["조조"] += 1
                # "유비" 또는 "현덕"이라는 단어가 포함되어 있다면 유비 카운트 증가
                elif word.find("유비") != -1 or word.find("현덕") != -1:
                    wc["유비"] += 1
                # "손권" 또는 "중모"라는 단어가 포함되어 있다면 손권 카운트 증가
                elif word.find("손권") != -1 or word.find("중모") != -1:
                    wc["손권"] += 1
                    
# for key in wc:
#     print(key)
# for val in wc.values():
#     print(val)

# 결과를 CSV 파일로 저장하기
with open("C:/Users/sdedu/Desktop/threekingdoms/tkResult.csv", "w", encoding="utf-8") as f:
    for k, v in wc.items(): # 딕셔너리에서 이름(key)과 등장 횟수(value) 가져오기
        f.write(f"{k}, {v}\n") # CSV 형식으로 저장 (예: 조조, 152)
print("-완-")