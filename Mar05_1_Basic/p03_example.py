# 가위바위보 => 한번 질때까지 => 총 몇 번 이겼는지 출력
# Java (null) = Python (None)
import random
import time

def userGreet():
    userName = input("유저 이름을 입력하세요 : ")
    print("안녕하세요", userName)
    
def getComRSP():
    rsp = random.randint(1,3)
    return rsp 

def getUserRsp():
    
    userRSP = int(input("1.가위 2.바위 3.보 중 하나를 입력하세요"))
    if(1 <= userRSP <= 3):
        return userRSP
    else:
        getUserRsp()
        
def whatisComputer(comRSP):
    if(comRSP == 1):
                print("컴퓨터가 낸 것은 가위!")
    elif(comRSP == 2):
                print("컴퓨터가 낸 것은 바위!")
    else:
                print("컴퓨터가 낸 것은 보!")    
handTable = [None, "가위", "바위", "보"]
def printRule():
    print('------------')
    for i, h in enumerate(handTable):
        if(i != 0):
            print("[%d] %s", i, h)
def playRSP():
    count = 0
    while True:
       
        comRSP = getComRSP()
        userRSP = getUserRsp()
       
        if(userRSP - comRSP == -1 or userRSP - comRSP == 2 ):
            whatisComputer(comRSP)
            print("유저 패배 ☠")
            print("이긴 횟수 : %d" %count)
            break
        elif(userRSP==comRSP):
            whatisComputer(comRSP)
            print("비겼습니다.")
        else:
            
            whatisComputer(comRSP)
            time.sleep(1)
            print("이겼습니다!")
            count += 1

userGreet()
playRSP()














