import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

n = 50
# 0 ~ 1 범위의 난수를 50 개 생성
x = np.random.rand(n)
y = np.random.rand(n)

##################################
# <기본>
# x, y 데이터를 순서대로 scatter() 함수에 입력을 하면
# 해당 위치(좌표)에 마커가 표시됨 (산점도, 분포도)

# plt.scatter(x, y)
#
#
#
# #############################################
# # <마커 크기, 색상>
# area = (30 * np.random.rand(n)) ** 2
# colors = np.random.rand(n) # 0 ~ 1까지의 숫자를 임의의 색으로 지정하게 됨
#
# #print(colors, type(colors))
#
# plt.scatter(x,y, s=area, c=colors)
#plt.show()

#< 투명도, 컬러맵 >
# area = (30 * np.random.rand(n)) ** 2
# colors = np.random.rand(n)
#
# import matplotlib.cm
# print(matplotlib.cm._colormaps) # cmap 종류
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
# plt.show()

############################################
# 다차원 랜덤 배열 생성...
np.random.seed(0)
arr = np.random.standard_normal((8,100)) # (8, 100) 형태의 난수 배열
print(arr)

plt.subplot(2, 2, 1) # 2 X 2 size 중에서 1번째
plt.scatter(arr[0], arr[1], c=arr[1])
plt.spring()
plt.title("Spring")
plt.subplot(2, 2, 2) # 2 X 2 size 중에서 1번째
plt.scatter(arr[2], arr[3], c=arr[3])
plt.summer()
plt.title("Summer")
plt.subplot(2, 2, 3) # 2 X 2 size 중에서 1번째
plt.scatter(arr[4], arr[5], c=arr[5])
plt.autumn()
plt.title("Autumn")
plt.subplot(2, 2, 4) # 2 X 2 size 중에서 1번째
plt.scatter(arr[6], arr[7], c=arr[7])
plt.winter()
plt.title("Winter")

plt.tight_layout() # 자동으로 여백에 관련된 파라미터 조정

plt.show()






