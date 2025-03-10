
# 파일처리
# 1. 파일로부터 데이터를 읽어와서 프로그램에서 활용하기 위함
# 2. 프로그램에서 만든 데이터를 파일형태로 저장하기 위함

# 파일 열기 => 작업(읽기, 쓰기) => 파일 닫기 (필수 !!!)

# .txt파일 / .csv파일

# 1. 파일에 내용 쓰기(write)
# 폴더는 미리 만들어놔야 함 
# 파일은 존재하지 않아도 실행시에 파일을 만들어줌

# w : 덮어쓰기 
# file = open("C:/Users/sdedu/Desktop/메추라기/test.txt", "w", encoding="UTF-8")
# file.write("조금만 지나면 점심시간 ㅎ_ㅎㅇ_ㅇ")
# print("완료!")
# file.close()

# 2. 파일에 내용을 추가(append)
# file = open("C:/Users/sdedu/Desktop/메추라기/test.txt", "a", encoding="UTF-8")
# file.write("\n저녁은 부대찌개...\n ㅎㅎㅎ....")
# print("완료!")
# file.close()

# 3. 파일 읽어오기 (Read)
# file = open("C:/Users/sdedu/Desktop/메추라기/test.txt", "r", encoding="UTF-8")
# data = file.read()
# print(data)
# file.close()

# 3-2. 파일을 한줄씩 읽기
file = open("C:/Users/sdedu/Desktop/메추라기/test.txt", "r", encoding="UTF-8")
while True: #해당 파일의 내용이 언제 끝날지 모르기 때문에 True
    data = file.readline()
    print(data, end = "")
    #readline()의 결과가 공백인 상황 (파일의 맨 마지막 줄까지 끝난 상황)
    if data == "":
        break # 종료
file.close()
    









