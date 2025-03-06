# Java : 강제 => 언제 해야하는지 몰라도 됨
#            하기 싫은데도 해야하는...
#            직접 : try - catch - finally  => 메인
#            미루기 : throws => main이외


# Python : 하기 싫으면 안해도 됨
#      직접 : try - except(catch) - else - finally

# error : 컴파일할때 (소스를 기계어로 바꿀떄)
#              컴파일작업을 실행하지 못하는 상황
# warning : 정리가 안된 소스 
# (ex: 쓸모없는 변수 설정, close(); 를 안한 상황)
# exception : 실행하다가 예외적인 상황이 발생해서
# 정상적으로 돌아가지 않는 상황

# Python은 인터프리터 방식 : 
#     실행하면 그 때부터 한줄씩 기계어로 바꿔서 실행
# error ? exception? 경계가 모호함...
##############################################
# 정수 2개를 입력받아서 앞의 숫자를 뒤의 숫자로 나눴을 때의 몫
try:
    a = int(input("첫번째 숫자 : "))
    b = int(input("두번째 숫자 : "))
    result = a // b
    print("몫은 %d" % result)
    
    
    l = [1, 23, 456]
    print(l[b])
# except ZeroDivisionError:
#   print("y에 0? 이거 맞습니까")
# except IndexError:
#     print("list에 없음")

except Exception as asdf:  #모든 에러
    print(asdf)            #무슨 내용인지 알고 싶을 때


#try문에서 else를 사용하는 이유는,
#단순히 성능적인 것을 넘어서
#에러가 발생할 가능성이 있는 부분과 그렇지 않은 부분을
#정확히 구분을 지어서 작성자의 의도를 명확하게 하기 위함


else:
    print("문제가 없으면 실행")


finally:
    print("문제가 있든 없든 무조건 실행(return보다 먼저)")
    
    
    
    
    
    
    
    
    
    
    

