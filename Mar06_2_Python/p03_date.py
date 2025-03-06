from datetime import datetime



# 현재시간 날짜
now = datetime.today()
print(now)


whiteday = datetime(2025, 3, 14)
print(whiteday)
print(type(whiteday))
print(whiteday.year)
print(whiteday.month)
print(whiteday.day)


# 생일을 입력받아서 나이를 계산해주는 프로그램

birthday = (input("생년월일(yyyy/MM/dd) :  "))
curYear = now.year
print(type(curYear))

print(curYear - int(birthday[0:4]))

#str => datetime : strptime
bd = datetime.strptime(birthday, "%Y/%m/%d")
print(type(bd))


#datetime => str : strftime
bd = datetime.strftime(bd, "%A")
print(bd, type(bd))
########################################
#Pattern
# %Y : 연도 4자리 / %y : 연도 뒤에 2자리
# %m : 월 / %d : 일 / %H : 시간(24시간) / %I : 시간 (12시간)
# %p : AM, PM / %M : 분 / %S : 초 / %a : 요일(짧게) / %A : 요일(길게)

# 특정 날짜를 연/월/일 형태로 입력받아서 => 일/월 형태의 문자열로 출력
print("------------------------------")
day = input("YYYY/mm/dd : ")

d = datetime.strptime(day , "%Y/%m/%d")
d = datetime.strftime(d, "%d/%m")
print(d)

























