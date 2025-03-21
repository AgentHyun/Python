# 변수 (Varible)
# Java : 값을 표현하기 위해서 최적의 자료형을 개발자가 직접 선정
#     => 메모리 사용량이 최적화
#     자료형 변수명 = 값;
#     int a = 10;
from pickle import TRUE, FALSE

# Python : Python이 알아서 자료형을 선정
#    '자료형'이라는 것 자체를 공부할 필요가 없음
#    => 개발자가 편함
#    자동으로 선정하는 시간을 메모리가 잡아먹어서
#     메모리 사용량 컨트롤이 불가능함
#    기본형이 없고, 다 참조형 >> 메모리 사용량이 많음
#     변수형 = 값 

a = 10
print(a)
print(type(a))
print(id(a))

print('######################')
#Java 버전 값 바꾸기
# int b = 10;
# b = 20;
a = 20;
print (a)
print(type(a))
print(id(a))

#Python의 Data Type(자료형)

p_str = 'puft'  # str : 문자열
print(p_str, type(p_str))
p_int = 10    #int : 정수
print(p_int,type(p_int))
p_float = 1.234  # float : 실수
print(p_float,type(p_float))
p_bool = True    # boolean : 논리 (True, False)
print(p_bool, type(p_bool))

p_list = [3, 7, 5] # list : 리스트
print(p_list, type(p_list))

#각기 다른 자료형이 들어와도 상관없음

p_dict = {
    'name' : 'puft',
    'age' : 100
    }   # dict : 사전(dictionary)
#key값과 value형식으로 이루어져 있음

print(p_dict, type(p_dict))


p_set = {3,6,7} # set : 집합
print(p_set, type(p_set))#값의 중복 X
p_tuple = (5, 7, 6) # tuple : 튜플
#소괄호 안에 여러 값을 집어 넣음
print(p_tuple, type(p_tuple))

#################################

# 형 변환 (Type Casting)

d = 1
print(type(d), id(d))

d = str(d)

e = False

e = int(e) # False = 0 / True = 1

#키보드 입력받기

k1 = input('입력')
print(k1)


#기본적으로 문자형이기 때문에
#숫자를 사용하려면 형변환이 필요함




