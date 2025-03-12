import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# Python의 시각화를 위한 library - matplotlib
# cmd => pip install matplotlib

# 등장인물 따로
name = []
# 등장횟수 따로
count = []
with open("C:/Users/sdedu/Desktop/threekingdoms/tkResult.csv", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        # 엔터처리 없애주고, 쉼표를 기준으로 나눔
        line = line.replace("\n", "").split(",")
        
        name.append(line[0])
        count.append(int(line[1]))  # count 값을 숫자로 변환

print(name, count)

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

# 막대그래프 - 절대적인 값 비교 : bar
c = ['yellow', '#B2CCFF', '#FFA7A7']
# x축, y축, 바의 두께(0~1사이), 컬러
# plt.bar(name, count, width=0.4, color=c)
# plt.title('Three Kingdoms')
# plt.xlabel('name')
# plt.ylabel('count')
# # 눈금은 등장인물의 개수만큼, 어떤 값인지
# plt.xticks(range(len(name)), name) # 눈금 설정
# plt.ylim(0, 10000)
# plt.show()

# 파이차트 (pie)

plt.pie(count, labels=name, colors=c, shadow=True, explode=(0.1, 0.1, 0.1))
# explode : 각 항목이 원점에서 어느정도 튀어나와있는지
plt.title('Three Kingdoms')
plt.show()

