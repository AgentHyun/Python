from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rc("font", family=font_prop.get_name())

# 기상청 데이터 요청
hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4122066000")
res = hc.getresponse()
resBody = res.read()


temp_arr = []
reh_arr = []
times = []

for w in fromstring(resBody).iter("data"):
    hour = int(w.find("hour").text) 
    temp = float(w.find("temp").text)  
    reh = int(w.find("reh").text) 

    times.append(hour)
    temp_arr.append(temp)
    reh_arr.append(reh)

indexes = range(len(times))

########################
x1 = plt.subplot()
p1 = x1.plot(indexes, temp_arr, 'r-o')
x1.grid(axis="both", color="black", linestyle="-.")
x1.axis([None, None, None, 39])
x1.set_xlabel("시간")
x1.set_ylabel("기온")

x2 = x1.twinx()
p2 = x2.plot(indexes, reh_arr, 'b:^')
x2.axis([None,None, 0, 100])
x2.set_ylabel("습도")
plt.title("우리동네 실시간 날씨", loc = "center")
x1.legend(p1+p2, ["기온", "습도"])

plt.xticks(indexes, times)

plt.show()



# plt.plot(range(len(temp_arr)), temp_arr, 'r-o', label="기온 (°C)")
# plt.plot(range(len(reh_arr)), reh_arr, 'b-s', label="습도 (%)")
#
# plt.xlabel("시간 (h)")
# plt.ylabel("값")
# plt.xticks(range(len(times)), times)
# plt.title("기상청 3시간 간격 기온 및 습도 변화")
# plt.legend()
#
#
#
# plt.show()
