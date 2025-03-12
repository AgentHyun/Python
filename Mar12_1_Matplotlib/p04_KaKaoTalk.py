#C:/Users/sdedu/Desktop/메추라기


import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
#카카오톡 내용 txt파일 정제
# ㅋ : ? / ㅎ : ? / ㅠ : ? / ? : ? / ! : ? => pie차트

with open("C:/Users/sdedu/Desktop/메추라기/KakaoTalkChats.txt", "r", encoding="UTF-8") as f:
    wc = {"ㅋ" : 0, "ㅎ" : 0, "ㅠ" : 0, "?" : 0, "!" : 0}
    
    for line in f.readlines():
        line = line.replace("\n", "")
        if( " : ") in line:
            parts = line.split(" : ", 1) # 첫번째 " : " 에서만 분리
            print(parts)
            if len(parts) == 2:
                message = parts[-1]
                for w in message:
                    if w in wc:
                        wc[w] += 1
        print(wc)
        

word = []
count = []
for k, v in wc.items():
    word.append(k)
    count.append(v)       
print(word, count)    
   
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

c = ['#BBDDCC', '#B2CCFF', '#FFA7A7', '#E5DDFF', '#DDFFFF']

w = {'width' : 0.7, 'edgecolor' : 'pink', 'linewidth' : 5}
plt.pie(count, labels=word, autopct="%.2f%%", wedgeprops=w)
# autopct : 지분을 %로 나타냄 / wedgeprops : 테두리
plt.title("카톡 단어 사용량")
plt.show()





