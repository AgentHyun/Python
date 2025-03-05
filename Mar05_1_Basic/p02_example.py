import random

# UP/DOWN 게임 (함수)


# 유저의 이름을 입력받고 환영하는 인사를 출력
def getName():
    name = input("이름을 입력하세요")
    print(name + "님 환영합니다!")
# (컴퓨터) 1 ~ 100사이의 랜덤한 정수를 하나 뽑아서
def getRandomNumber():
    randomNumber = random.randint(1,100)
    return randomNumber

# 유저에게 정답을 입력하게했을 때
# 범위 내의 숫자가 아니면 다시입력하도록

def getAnswer():
    answer = int(input("숫자를 입력하세요"))
    if(not(1 <= answer <= 100)):
        getAnswer()
    return answer

# 입력한 숫자가 정답보다 작으면 'UP' / 크면 'DOWN' 출력

def judgeUpDown():
    count = 0
    getName()
    
    computerAnswer = getRandomNumber()
    while True:
        answer = getAnswer()
        if(answer < computerAnswer):
            print("UP!")
            count+=1
        elif(answer > computerAnswer):
            print("DOWN!")
            count+=1
        if(count == 10): # 정답 기회는 총 10번
            print("정답기회 소진😥")
            break
        elif(answer == computerAnswer):
            print("축하드립니다 정답입니다!")
            print("시도횟수 : %d" %count )
    
            break
    # 정답을 맞췄을 때는 몇 번만에 맞췄는지 출력 + 종료    
    print("정답 : %d" %computerAnswer)
   
         
     
    






judgeUpDown()




