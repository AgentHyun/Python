from cx_Oracle import connect

#csv파일로 만들어주세요!
#번호,시간대, 온도, 최고기온, 최저기온 의 형태로


con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe"); 

sql = "select * from mar10_weather";

cur = con.cursor()
cur.execute(sql)
file = open("C:/Users/sdedu/Desktop/메추라기/weather2.csv", "w", encoding="UTF-8")
file.write("번호, 시간대, 기온, 최고기온, 최저기온\n")
for no,time,temp,max,min in cur:
    file.write(f"{no}, {time}, {temp}, {max}, {min} \n")

print("파일 작성 완료")

con.close()

file.close()  







