
# 3항 연산자
# 1. [참일때의 값] if [조건문] else [거짓일떄의 값]

def getWeight():
    weight = float(input("몸무게 : "))
    return weight if weight >= 0 else weight * -1;

# 2. [조건식] and [참일때의 값] or [거짓일때의 값]
 #    return weight >= 0 and weight or weight * -1;
    
    
# 정수를 입력했을 때 짝수인지 홀수인지를 출력해주는 프로그램
number = int(input("정수 입력 : "))
print((number % 2 == 0 and "짝수" or "홀수"))
print('--------------------------------------')

#3항 연산자 중첩
# [참1] if [조건1] else [참2] if [조건2] else .. [거짓]

# 15, 16, 17을 list에 담고
# 리스트 각각의 요소가 2의 배수인지, 3의 배수인지, 아니면 둘다 아닌지
list = [15,16,17]

for i in list:
   print(f"{i}는 2의 배수" if (i % 2 == 0) else f"{i}는 3의 배수" if (i % 3 == 0) else f"{i}는 둘다아님")

print('---------------')
#길어진다면 if - elif - else가 좀더 보기 편함
for i in list:
    if(i % 2== 0):
         print(f"{i}는 2의 배수")
    elif(i % 3 == 0):
         print(f"{i}는 2의 배수")
    else:
         print(f"{i}는 둘다 아님")
             
             









