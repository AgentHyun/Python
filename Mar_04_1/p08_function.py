# function (함수)
# def 함수명(파라미터명):
#    code



def test():
    print("Test!!!")
    
def test2(): # : 을 썼으면 그 다음줄에는 반드시 들여쓰기 해야함

    pass       # : 뒤에 코드 적을것이 없을 때, 자리 채워주라는 의미   

def add(a=5, b=8):  # 호출할 때 파라미터 값을 안넣어주면
    #함수의 파라미터 값을 기본값으로 사용
    
    print (a + b)    
def add2(a=5, b=8, c = 7): 
    print (a + b + c)       
    
#정수 2개를 넣으면 그 합을 "구하는" 함수

def addReturn(a,b):
    return a + b
    
#정수 2개를 넣으면 사칙연산 결과를 '구하는' 함수

def addReturn2(a,b):
    return([a+b,a-b,a*b,a/b])    

####################################################
help(addReturn2(5, 7))
test()
add(2,4)
add2 (3,5,7)
print(addReturn(5, 7))

print(addReturn2(1,2))




