#(int i = 0 ...)   : X
# (int ii : i) : O (Java의 for-each문에 해당하는 반복문)

l = [123,45,6,78,910]
for ll in l:
    print(ll)
    
    #ㅋ 을 10 번 출력
for i in range(10):
    print('ㅋ')
        
 # 1 ~ 20까지의 정수 중에서 홀수만 출력
for i in range(1,21):
     if(i % 2 == 1):
         print(i)
########################################
#while문 : O
while True:
    y = int(input("y:"))
    if y % 2 == 0:
        print("짝수")
        break    
#
# enumrate() : 반복문을 사용할 때 몇 번 반복되었는지
# 확인이 필요할 때 사용
# (인덱스, 값)의 tuple 형태로 리턴


li = ['컴퓨터', '모니터', '마우스', '키보드']

# for i, v in enumerate(ll):
#     print(i + 1, v)

########################
score = [10,54,56,70,70,87,65,99,91,88]

#1등학생은 몇번째에 ? 점수는 몇점인지?

max = 0
maxv = 0
for i, v in enumerate(score):
    print(i)
    if(v > max):
        max = v
        maxv = i
 
    
print('1등학생 : ' , maxv)
print('1등학생점수 : ' , max)   
    





