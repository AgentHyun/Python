# abstract - X

# Java : 생성자 상속 안됨
# Python : 생성자가 상속이 됨
#    멤버변수를 생성자에서 결정 => 생성자를 상속안해주면
#    => 멤버변수가 상속이 안됨 

class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def attack(self):
        print('공---격')
    def printInfo(self):
        print(self.name)
        print(self.age)
###############################################
class Ironman(Avengers): #상속받을 클래스를 파라미터로 넣어줌
    
    #overloading : 메소드명 같게, 파라미터가 다르게
    #overriding : 상속받은 메소드 기능 바꾸기
    
    def __init__(self, name, age, suitType):
        Avengers.__init__(self, name, age) #overriding
        self.suitType = suitType
    
    def attack(self):
        #Avengers.attack(self)
        super().attack()
        print("탈모빔 발4 ~~~~")
    def printInfo(self):
        Avengers.printInfo(self)
        print(self.suitType)
############################################# 
# 헐크 (어벤져스) / 이름, 나이, 바지사이즈
#   공격 O / 정보 출력

class Hulk(Ironman):
    def __init__(self,name,age,pantSize):
        Avengers.__init__(self, name, age)
        self.pantSize = pantSize
    def attack(self): 
        Avengers.attack(self)
        print("자동차 던지기!")
    def printInfo(self):
        Avengers.printInfo(self)
        print(self.pantSize)      



#############################################  

if __name__ == "__main__":
    i = Ironman("토니스타크", 42, "mk50")
    i.attack()
    i.printInfo()
    print('----------------------')
    
    h = Hulk("안토니", 24, "100")
    h.attack()
    h.printInfo()
    print('----------------')
    
    
    
    
    
    