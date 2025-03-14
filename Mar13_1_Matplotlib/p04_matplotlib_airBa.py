import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=font_path, size=12).get_name()
plt.rc("font", family=fontName)


hc = HTTPConnection("openAPI.seoul.go.kr:8088")
url = "/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/"
hc.request("GET", url)
res = hc.getresponse()
resBody = res.read().decode("utf-8")
air = loads(resBody)


regions = ["도심권", "서남권", "동남권", "서북권", "동북권"]
dust_data = {region: [] for region in regions}
tiny_dust_data = {region: [] for region in regions}

for row in air["RealtimeCityAir"]["row"]:
    city = row["MSRRGN_NM"]
    dust = int(row["PM10"])
    tiny_dust = int(row["PM25"])
    if city in dust_data:
        dust_data[city].append(dust)
        tiny_dust_data[city].append(tiny_dust)


dust_list = [sum(dust_data[region]) / len(dust_data[region]) if dust_data[region] else 0 for region in regions]
tiny_list = [sum(tiny_dust_data[region]) / len(tiny_dust_data[region]) if tiny_dust_data[region] else 0 for region in regions]

print("미세먼지 평균값:", dust_list)
print("초미세먼지 평균값:", tiny_list)

plt.bar(regions, dust_list, color="#FFC19E")


plt.bar(regions, tiny_list, color="#B5B2FF",  bottom=dust_list)
plt.legend(["미세먼지", "초미세먼지"])
plt.show()
