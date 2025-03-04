# Java vs Python
# Java : 규칙의 언어 => 완벽한 객체지향 언어
#    명확하고, 혼란스럽지가 않은 코드

# Python : 사람이 쓰기 편하게 => 자유의 언어 => hybrid한 객체지향 언어
# 코드가 짧다
# 코드가 길어지면... => 헷갈릴 여지가 있음
#########################################
# 기본적인 출력 방식
print('wa 파이썬!') # enter 기능 포함
print('wa 파이썬!2')

#seperator
print('내', '일', '수', '요', '일', sep = " ")
#어떠한 값으로 각각의 값을 구분 지을지

#메일주소 출력
#전화번호 출력

print('ekdh390404', 'naver.com', sep = '@')
print('010','9370','3904', sep = "-")


#end
print('파이썬이', end = ' ')
print('본격적으로', end = ' ')
print('시작되었습니다.')

#출력 형식 (format)
print('{} and {}'.format('1번', '2번'))

print('{1} and {0} and {0}'.format('1번', '2번')) # 인덱스 지정 가능
print('{p1} is {p2}'.format(p1 = 'life', p2 = 'egg'))#변수 지정 가능

# %d, %f, %s
# System.out.printf("%d", 123);


print('%d' % 123)
print('%.2f' % 123.4567)








