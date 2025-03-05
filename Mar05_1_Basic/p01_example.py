import random
# print(i)

#로또번호뽑기 (6개만) (1~45) => 중복없이




    
def getNumber():
    return random.randint(1,45)
    

num_list = [] #랜덤으로 뽑은 숫자를 담을 list

count = 0 #로또뽑은 횟수

while count < 6:
    ran_num = getNumber()
    if ran_num not in num_list:
         # 뽑은 숫자가 list안에 안들어있따면
        num_list.append(ran_num)
        count += 1 
    
for n in num_list:
    print(n, end = ' ')
















