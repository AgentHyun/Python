import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from p01_matplotlib_basic import fontFile

font_path = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)


xData = np.array([1,2,3,4])
yData = np.array([12, 31, 7, 17])
yData2 = np.array([1, 51, 23, 10])
c = ['#FFB2D9', '#D941C5', '#B5B2FF', '#FFC19E']

#plt.bar(xData, yData, color=c, edgecolor = "#670000", linewidth=5, width=0.5)
#width : 그래프의 폭
#edgecolor : 테두리 색
#linewidth : 테두리 굵기



#plt.show()

#여러 항목



#plt.bar(xData, yData, color="#FFC19E", width=0.3, align="edge")

#width에 -(음수)를 붙이면 왼쪽으로 붙어서 출력
#plt.bar(xData, yData2, color="#B5B2FF", width=-0.3, align="edge")

#XData에 -(음수)를 붙이면 왼쪽으로 붙어서 출력
#plt.bar(xData - 0.3, yData2, color="#FFB2D9", width=-0.3, align="edge")
#plt.show()

# 누적합
plt.bar(xData, yData, color="#B5B2FF")
plt.bar(xData, yData2, color="#FFC19E", bottom=yData)
plt.show()







