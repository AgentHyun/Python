#조건문 : 흐름 제어

if True:
    print("와~조건문")
    pass #뭘쓸지 모를때 쓰는 pass
if False:
    print("안나오지")

######################
# 우선순위 (산술, 관계, 논리)
# 산술 > 관계 > 논리
print(10 + 2 > 8 + 3)
print(((10 + 2) > 3) and (6 + 4 == 10))


# 놀이동산 >> A놀이기구 : 성인, 150cm이상 탑승 가능
# 나이와, 키를 입력했을 때 탑승 가능 or 불가능

age = int(input("나이 : "))
height = int(input("키 : "))
if(age >= 20 and height >= 150):
    print("탑 승 가 능")
else:
    print("탑 승 불 가 능")
print((age>=20 and height >= 150) and "탑승 가능" or "탑승 불가")


##############################################################################

# 다중 조건문
# Java : if - else if - else
# Python : if - elif - else

#점수 입력 : 80점 이상은 'A'
#          70점 이상은 'B'
#          60점 이상은 'C'
#          나머지는 'D'를 출력


score = int(input("점수 : "))

if (score >= 80):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 60):
    print('C')
else:
    print('D')

#in, not in
abc = {"name" : "뜨또", "age" : 19, "phone" : "010-1111-2222"}

print("name" in abc)

print(20 in abc.values())

print("height" not in abc)
