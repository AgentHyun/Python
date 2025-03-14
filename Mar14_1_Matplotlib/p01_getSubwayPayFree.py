#http://openapi.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/xml/CardSubwayPayFree/1/5/201501/
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# 2016 ~ 2024년 월별로 데이터 > 하나의 파일(csv)에 저장
# 연월(ex:202211), 호선명, 지하철역, 유임승차인원, 무임승차인원, 유임하차인원, 무임하차인원


hc = HTTPConnection("openapi.seoul.go.kr:8088")

f = open(f"C:/Users/sdedu/Desktop/threekingdoms/subway.csv", "a", encoding="UTF-8")

for year in range(2016,2025):
    for month in range(1,13):
        url = f"/4f626857416f6c6c3632586a416843/xml/CardSubwayPayFree/1/700/{year}{month:02d}/"
        hc.request("GET", url)
        resBody = hc.getresponse().read()
        
        
        for w in fromstring(resBody).iter("row"):
            s_date = w.find("USE_MM").text
            s_line = w.find("SBWY_ROUT_LN_NM").text
            s_name = w.find("STTN").text
            s_pay_up = w.find("RMIO_GTON_NOPE").text
            s_pay_free_up = w.find("FREECHRG_GTON_NOPE").text
            s_pay_down = w.find("RMIO_GTOFF_NOPE").text
            s_pay_free_down = w.find("FREECHRG_GTOFF_NOPE").text
            f.write(f"{s_date},{s_line},{s_name},{s_pay_up},{s_pay_free_up},{s_pay_down},{s_pay_free_down}\n")
            print(s_date)
        
f.close()
    