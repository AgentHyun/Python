# 인원수 관련 => 정수형태로 저장
from http.client import HTTPConnection
from json import loads
#/json/CardBusStatisticsServiceNew/1/5/20151101/
hc = HTTPConnection("openapi.seoul.go.kr:8088")

y = 2024
f = open(f"C:/Users/sdedu/Desktop/threekingdoms/bus_pro_{y}.csv", "a", encoding="UTF-8")

for m in range(1, 13):    # 월 : 1 ~ 12
    for d in range(1, 32): # 일 : 1 ~ 31
        for start in range(1, 42000, 1000): # 한 페이지에 보여지는 데이터 1000개씩
            url = "/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/"
            url += f"{start}/{start+999}/{y}{m:02d}{d:02d}/"
            
            hc.request("GET", url)
            resBody = hc.getresponse().read()
            busData = loads(resBody)
            
            if "CardBusStatisticsServiceNew" in busData:
                for b in busData['CardBusStatisticsServiceNew']['row']:
                    f.write(f"{y},{m},{d},")
                    f.write(f"{b['RTE_NO'].replace(',', '.')},")
                    f.write(f"{b['SBWY_STNS_NM'].replace(',', '.')},")
                    f.write(f"{b['GTON_TNOPE']:.0f},") 
                    f.write(f"{b['GTOFF_TNOPE']:.0f}\n")
                                
                           
        print(y, m, d)
        
        
        
        
f.close()    
            
        
    













