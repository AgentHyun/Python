from pip._vendor.typing_extensions import Self
from os import name
from pickle import NONE


class Book():
    #def __init__(self):
    #    print("기본생성자 - 책 생성")
    
    
    # 생성자 : 객체가 메모리상에 만들어질 때 호출하는 메소드
    def __init__(self, title, price):
        print("오버로딩 된 생성자 ?!?!?!")
        self.title = title
        self.price = price
    
    def printInfo(self):
        print(self.title, self.price)
    
    #소멸자 (destructor) : 객체가 메모리상에서 사라질 때 호출
    
    def __del__(self):
        print("책 삭제")
    
#######################################3

#사람 클래스 : 이름, 나이 / 그 속성들 출력하는 기능/ 생성자, 소멸자

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printInfo(self):
        print(self.name,self.age)
    def __del__(self):
        print("사람 삭제")



    
#######################################3
#b1 = Book()
b2 = Book("원피스", 7000)
b2.printInfo()
print("-------------")
#######################################3
# 생성자 생성 -> 생성자의 printInfo() -> 프로그램이 끝나면서 소멸자 발동
# Garbage Collection:
# 그 객체를 가리키는 변수가 없게 되면 Heap영역을 자동으로 정리

h1 = Human("김래현", 27)
h1.printInfo()
print('-----------')
h2 = Human("박휴먼", 20)
h2.printInfo()
print('-----------')


h3 = h1

h1 = None
h3 = None

print(" !@#@!#!#@!#@#$%@@#%")


