import urllib.request as req
from pip._vendor.requests.exceptions import HTTPError
from urllib.error import URLError


pathList = ["C:/Users/sdedu/Desktop/메추라기/fireDragon.png",
            "C:/Users/sdedu/Desktop/메추라기/index.html"]

urlList = ["https://th.bing.com/th/id/OIP.Tj79EDRCrdBJjEt9UKLVogHaJ4?w=158&h=210&c=7&r=0&o=5&pid=1.7",
           "https://www.youtube.com/?hl=ko&gl=KR&app=desktop"]


for i,url in enumerate(urlList):
    # 예외 처리
    
    
    try : 
        # web의 수신정보를 확인
        res = req.urlopen(url)
        
        #응답 내용
        content = res.read()
        print("------------------------------------^.^--")
        
        # 상태정보 중간확인
        print(f"헤더 정보 : {i, res.info()}")
        print(f"http status : {res.getcode()}")
        print("-----------------^.^------------------")
        
        # 파일 쓰기
        # with : 파일을 열고 닫는거 같이 해주는 역할
        with open(pathList[i], "wb") as f: # 'b' : binary mode
            f.write(content)
            
    
    except HTTPError as e:
        print("HTTPError Code : ", e.code)
    except URLError as E:
        print("URLError Code : ", e.code)
    else:
        print("★★★★★★★")
        print("성 공!!!")
        print("★★★★★★★")
        



















