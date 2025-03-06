# 좋아하는 음료이름, 마시는 횟수 => 입력 받아서 그 내용을 출력
from _datetime import datetime

drink = input("좋아하는 음료는?")
count = int(input("몇번이나 마셔?"))

print("저는 %s를 좋아하고, 한달에 %d번 정도 마셔요." % (drink, count))

print(f"저는 {drink}를 좋아하고, 한달에 {count}잔을 마십니다.")

# Python 3.6.X 부터 f-string이라고 부르는
# 포맷팅을 좀 더 쉽게 할 수 있는 방법이 추가됨

# f-string은 f와 {}만 알면 되는데,
# f"문자열 {변수명} 문자열 ..."의 형태입니다.
# 소수점 반올림 표현
#기본적으로 % 포맷팅과 거의 유사함
# 하지만 {}를 사용해서 포맷팅 할 때는,
# 포맷팅하는 값의 자료형에 상관없이 {}를 사용하면 됨



#f = 1.125
f = 1.135
print(f"{f}")  # 1.125 , 1.135
print(f"{f:.1f}") # 1.1, 1.1
print(f"{f:.2f}") # 1.13 , 1.14 반올림처리

#Python의 반올림은 반올림하려는 수가 올림, 내림했을 때
#동일하게 차이가 나는 경우에는 (5가 기준이 될 때)
#0, 1, 2만 반올림이 안됨...

s1 = "left"
result1 = f"|{s1:<10}|"
print(result1)


s2 = "mid"
result2 = f"|{s2:^10}|"
print(result2)

s3 = "right"
result3 = f"|{s3:>10}|"
print(result3)

#중괄호 {}안에 있는 변수 뒤에 콜론(:) 붙인 후

# < 는 왼쪽 정렬/ ^ 는 가운데 정렬/  > 는 오른쪽 정렬을 의미합니다.
#
# 각 기호 뒤에 오는 숫자는 자릿수를 의미합니다.

# f-string에서 중괄호를 출력하려면
num = 10
result4 = f"my age : {num}, {{num}}, {{{num}}}"
print(result4)

#중괄호를 연속해서 2개를 사용하면 ({{}}),
# 중괄호 자체를 출력할 수 있고,
# f-string의 값과 중괄호를 같이 표현하려면,
# {{{}}} 중괄호 3개를 입력하면 num을 변수로 인식을 하게 됨

# f-string과 dict

d = {
       "name" : "Puft",
       "gender" : "남자",
       "age"   : 100
    }

result5 = f"name : {d['name']}, gender: {d['gender']}, age {d['age']}"
print(result5)

# f-string과 list
n = [100, 200, 300]

# 각 요소를 출력
print(f"list : {n[0]},{n[1]}, {n[2]}")

for v in n:
    print(f"리스트 요소 : {v}")

# 기존에 리스트에 접근하는 방법과 동일하게 {}안에
# 리스트에 대한 접근을 활용하면 됨!
print("------------------------------")

num2 = 1234567890
print(num2)


print(f"{num2:,}")
print("------------------------")
date1 = datetime.today()

print(date1)

#연-월-일 => 요일

print(f"{date1:%Y-%m-%d} is on a {date1:%A}")

#정리
# 1. 문자열 맨 앞에 (따옴표 앞) 'f'를 붙인다.
# 2. 사용하고 싶은 변수, 값을 중괄호 안에 넣는다.
# 3. 예쁘게 출력한다...


