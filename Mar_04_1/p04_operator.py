# 정수 2개를 입력 받아서, 사칙연산에 대한 결과와
# 앞의 수를 뒤의 수로 나눴을 때의 나머지 값을 출력

input1 = int(input("첫번째 정수 입력"))
input2 = int(input("두번째 정수 입력"))

print('{} + {} = {}'.format(input1, input2,input1+input2))
print('{} - {} = {}'.format(input1, input2,input1-input2))
print('{} * {} = {}'.format(input1, input2,input1*input2))
print('{} / {} = {}'.format(input1, input2,input1/input2))
print('{} % {} = {}'.format(input1, input2,input1%input2))

z = 'ㅋㅋㅋ'
c = str(input1) + z
print(c)

# x = x + 3
x= 1
x += 3
print(x)
# ++, -- 불가능
###################################3

e = x < 10
print(e)


##########################

# && : and , || : or

f = (x > 10) and (input2 < 3)
print(f)

# !  : not

g = not f
print(g)

# h : y가 5 이상 ~ 10 이하 : true / 아니면 False

h = (input2 <= input2 <= 10)

print(h)

#3항 연산자...
# Python에는 있다고 하는 사람도 있고, 없다고 하는 사람도 있음
# [참일때의 값] if [조건식] else [거짓일때의 값]
# 정수하나 입력받아서 => 짝수면 '짝수' 홀수면 '홀수'

a = int(input('정수 하나 입력'))
a = '짝수' if (a % 2 == 0) else '홀수'
print(a)


# 위의 버전이 너무 가독성이 안좋아서 python 3.8버전 이후로
# [조건식] and [참일떄의 값] or [거짓일때의 값]

a = (a%2 == 0 and '짝수' or '홀수')
print(a)











