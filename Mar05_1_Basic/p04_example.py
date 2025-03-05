import random

# 숫자야구 (3자리) (함수) (각 자릿수의 숫자는 중복 X)
# 012 ~ 987 중에 랜덤한 정수가 정답
# (각자리의 값들은 list에 담기)
# 유저가 입력 => 자릿수와 값까지 같으면 S,
#          => 자릿수는 다른데 값이 같으면 B,
# S가 3개 나오면 정답 => 종료

def getComputerAnswer():
    answer = random.randint(12, 987)
    answerList = []
    answerFirst = int(answer / 100)
    answerSecond = int((answer % 100) / 10)
    answerThird = (answer % 100) % 10
    answerList.insert(0, answerFirst)
    answerList.insert(1, answerSecond)
    answerList.insert(2, answerThird)
    
    return answerList

def getUserAnswer():
    answer = int(input("12 ~ 987까지의 숫자 입력"))
    if(12 <= answer <= 987):
        return answer
    else:
        getUserAnswer()

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = random.randint(0,9)
        if num not in numbers:
            numbers.append(num)
    print("번호 뽑기 완료 !")
    return numbers

def get_userAns():
    userAns = input("답 입력 :")
    # int로 받으면 백의자리가 0인 것들은 가져올 수 없음            
    if len(userAns) != 3:
        print("절대 3자리 숫자를 입력하지마!")
        return get_userAns()
    elif ((userAns[0] == userAns[1]) or
          (userAns[0] == userAns[2]) or
          (userAns[1] == userAns[2] )):
        print("절대 중복된 숫자르 입력해!")
        return get_userAns()
    return userAns
def check(gu, ua):
    strike, ball = 0, 0
    for i in range(0, 3):
        for j in range(0, 3):
            if(gu[i] == int(ua[j])):
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball    

def playGame():
    gn = generate_numbers()
    turn = 0
    s = 0
    b = 0
    
    print(gn)
    
    while s != 3 :
        s, b = check(gn, get_userAns())
        turn += 1
        print("{}S! {}B!".format(s, b))
        if s == 3:
            print("%d번 만에 맞췄습니다 !" % turn)
            print("정답은", end = " ")
            for a in gn:
                print(a, end = " ")
            print("입니다!!!")

def judgeStrike():
   
   
    comAnswer = getComputerAnswer()
    
        
    while True:
            userAnswer = getUserAnswer()
            userAnswerFirst = int(userAnswer / 100)
            userAnswerSecond = int(userAnswer % 100 / 10)
            userAnswerThird = userAnswer % 100 % 10
            strike = 0;
            ball = 0;
            for i, h in enumerate(comAnswer):
                
           
                if(comAnswer[i] == userAnswerFirst and i == 0 ):
                    strike += 1
                  
                elif(comAnswer[i] == userAnswerFirst):
                    ball += 1
                    
                elif(comAnswer[i] == userAnswerSecond and i == 1 ):
                    strike += 1
                  
                elif(comAnswer[i] == userAnswerSecond):
                    ball += 1
                    
                elif(comAnswer[i] == userAnswerThird and i == 2 ):
                    strike += 1
            
                elif(comAnswer[i] == userAnswerThird):
                    ball += 1
                 
                if(strike == 3):
                    print("정답은 %d" % userAnswer)
                    print("유저 승리!")
                    break
            print("%d 스트라이크" %strike)
            print("%d 볼" %ball)
            if(strike == 0 and ball == 0):
                    print("맞춘게 없네요..")  
                
     
                        
playGame()       
#judgeStrike()













