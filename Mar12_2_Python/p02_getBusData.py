from http.client import HTTPConnection
from datetime import datetime, timedelta
from json import loads
# http://openapi.seoul.go.kr:8088/4f626857416f6c6c3632586a416843
#/json/CardBusStatisticsServiceNew/1/5/20151101/






#1000건 이상 불가


# 2022/1/1 ~ 2024/12/31 3년치의 데이터를
# 연,월,일,노선번호, 정류장명(역명),승차총승객수, 하차총승객수
# 연도별로 csv파일에 저장

# 정류장명(역명) => 혹시, 가 들어가있을 수 있으니
            # => ,를 .로바꿔서 저장
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime("%Y%m%d")
    

    hc = HTTPConnection("openapi.seoul.go.kr:8088")
    url = f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/1/5/{date_str}/"
    hc.request("GET", url)
    res = hc.getresponse()
    resBody = res.read()
    datas = loads(resBody)

  
    try:
        datas = datas['CardBusStatisticsServiceNew']['row'][0]
    except (KeyError, IndexError):
        print(f"날짜 {date_str} 데이터 없음")
        current_date += timedelta(days=1)
        continue


    d = datetime.strptime(datas['USE_YMD'], "%Y%m%d")
    year = d.year
    month = f"{d.month:02d}"
    day = f"{d.day:02d}"


    name = datas['SBWY_STNS_NM'].replace(",", ".")
    no = datas['RTE_NO']
    up = int(datas['GTON_TNOPE'])
    down = int(datas['GTOFF_TNOPE'])


    file_path = f"C:/Users/sdedu/Desktop/threekingdoms/bus_{year}.csv"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{year},{month},{day},{no},{name},{up},{down}\n")
        print(f"{date_str} 데이터 저장 완료!")

  
    current_date += timedelta(days=1)
