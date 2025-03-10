# str
s = "Can't tuna kkk"
print(s)
print(s[0])    # indedxing

print(s[0:6]) # (0번째부터 (6-1)번째까지의 문자열)
              # slicing
print(s[2:10:2])# (2번째부터 (10-1)번쨰까지의 문자열을
                # 2칸씩 건너서
print("------------------")

# List : 리스트 (순서 O, 중복 O, 수정 O, 삭제 O)

a = [123, 4, 56 ,789, 1011]
print(a, type(a))
print(a[0])
print(a[0:3])
print(a[0:5:2])
print(a[-1])

print(len(a)) #요소의 갯수
a.append(1213) #끝에 요소 추가
a.insert(2, 1415) #중간에 요소 추가
a[4] = 7788 # 수정
del a[0] # 삭제
print(a)

a.sort() # 오름차순 정렬
a.sort(reverse=True)
print(a)

# Tuple : 순서 O, 중복 O, 수정 X, 삭제 X
tuple1 = ('1', '2','3')
# del tuple1[0] 삭제 안됨
print(tuple1)
# tuple[0] = 'c' 수정 안됨

t = (1,2,3,4,5,4,4)
print(t)
print(t.index(5)) #index 해당 위치에 있는 값을 반환
print(t.count(4)) #index안의 요소가 튜플 안에 몇개가 있는지
# 그 갯수를 반환

a1 = 10
b1 = 20

(a1, b1) = (10, 20) # 값을 줄 대 튜플로 묶어서 O
                    # 괄호 생략 가능
print(a1)
print(b1)

#int c1 = a1;
# a1 = b1;
# b1 = c1;

(a1, b1) = (b1, a1) # 튜플에 넣어서 서로의 값 바꾸기

print(a1, b1)

x, y, z = 10, 20, 30
x, y, z = z, x, y
print(x, y, z)

# Set(집합) : 중복 제거, 순서는 랜덤
s = {"ㅋ", "ㅋ", "ㄹ", "ㅃ", "ㅃ"}
print(len(s))
print(s)
print('------------------')

# Dict (=map)

d = {"name" : "김이름", "age" : 12}
print(type(d))


print(d["name"])
print(d["age"])

#Range
r = range(10)      # 0~ (10 - 1)까지의 범위
r = range(2,10)    # 2 ~ (10 - 1)까지의 범위
r = range(2,10,3)  # 2 ~ (10 - 1)까지, 3씩 건너서
print(r, type(r))

# 0 ~ 9까지 있는 list

r2 = range(10)
r2 = list(r2)
print(r2, type(r2))



# 1 ~ 20까지의 정수 중에서 홀수만 있는 list 출력

r3 = range(1, 21 ,2)
r3 = list(r3)

print(r3)



























