import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
# numpy
#    cmd = pip install numpy


fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

# matplotlib에서는 일반적으로 Numpy에 있는 Array를 이용
# Numpy를 사용하지 않더라도, 내부적으로 Array로 변환을 해서 사용

yData = np.array([12, 31, 1, 2]) # Numpy의 Array를 사용
xData = [1, 2, 3, 4] # Numpy를 사용하지 않아도 내부적으로 변환

# 선 그래프 
# plt.plot(yData)
# plt.show()


# x, y 축
# plt.plot(xData, yData)
# plt.show()

#축
# plt.plot(xData, yData)
plt.xlabel("x축")
plt.ylabel("y축")
#plt.axis([0, 10, 0, 50]) # [xmin, xmax, ymin, ymax]

#title
# plt.plot(xData, yData)
f = {"fontsize" : 15 , "fontweight" : "bold"} # bold(굵게), light, ultralight,...
plt.title("ㅋㅋ", loc="left")
#plt.title("ㅋㅋ", loc="right")
#plt.title("ㅋㅋ", loc="center")
# plt.show()

# plt.plot(xData, yData, 'c-.h')
# plt.show()

# 색 / 선의 모양 / 마커의 모양

# 색
#    b : blue / g : green / r : red / y : yellow
#    k : black / w : white / c : cyan(청록) / + RGB 지정 가능

# 선의 모양 (' ' 생략)
# ' : ' : 점선 / ' - ' : 실선 / ' -- ' : dashed line / ' -.' : 실선

# 마커의 모양 (' ' 생략)
#   ' . ' : 점 / ' o ' : 동그라미 / ' v ' : 아래 삼각형
#   ' ^ ' : 위 삼각형 / ' < ', ' > ' : 삼각형 왼쪽, 오른쪽
#   ' s ' : 사각형 / ' p ' : 오각형 / ' h ' : 육각형
#   ' * ' : 별 / ' + ' : + 모양 / ' x ' : x 모양

# plt.plot(xData, yData, color="r", linestyle="--",
#          marker = "*", linewidth=5, markersize=10)


# grid (격자)
#plt.plot(xData, yData)
#plt.grid(axis="both", color = "#997700", linestyle="-.")
#plt.show()


# 눈금
plt.plot(xData, yData)
plt.xticks(xData, ["일", "이", "삼", "사"])
plt.yticks(np.arange(0, 41, 10), ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
plt.tick_params(axis="x", direction="inout", length=10, pad=15,
                color = "r", labelsize=20, labelcolor="#F15F5F")
#axis : 옵션을 어디에 적용할지 (x, y, both)
#direction : in, out, inout / 눈금의 방향
#length : 눈금의 길이 
#pad : 눈금과 라벨의 거리

#plt.show()

yData = np.array([12, 31, 1, 2])
xData = [1, 2, 3, 4]


# plt.plot(xData, yData, "r-")
# plt.plot(xData, yData2, "g:")
# plt.legend(['초록데이터', '빨강데이터'])
# plt.show()

# 선 여러개2 (y축을 나눠서)
yData2 = [500, 600, 100, 1000]

x1 = plt.subplot()
p1 = x1.plot(xData, yData, "r-")
x1.set_xlabel("X축")
x1.set_ylabel("Y축")

x2 = x1.twinx() #x축을 공유

p2 = x2.plot(xData, yData2, "g:")
x2.set_ylabel("Y축2")
x1.legend(p1 + p2, ["Red", "Green"])

plt.show()

