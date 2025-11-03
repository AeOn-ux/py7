# 문자열
# 문자열 슬라이싱
a = '안녕하세요'
# 하세를 출력하시오
print(a[2:4])
print('안녕'*3)
print('안녕'+'하세요') # 연결연산자


# 문자열 함수
# upper() - 대문자로 변경
# lower() - 소문자로 변경
# swapcase() - 대문자는 소문자로, 소문자는 대문자로 변경
# title() - 첫글자를 대문자로 변경

a = 'abc'
#대문자로 변경
a.upper()
print(a)
print(a.upper())

b = 'aBBccdF'
print(b.upper())
print(b.lower())

c = 'the sea is dark'
print(c.title())

# 문자열 찾가
# count() - 해당되는 문자 개수
# find() - 왼쪽에서 해당 문자 위치 검색, 없을 때 -1 리턴
# rfine() - 오른쪽에서 해당 문자 위치 검색
# index() - 해당 문자 위치 검색, 없을 때는 에러
# startwith() - 해당 문자로 시작되는지 확인 true, false
# endwith() -  해당 문자로 끝나는지 확인


a = '112233333445'
print(a.count('3')) # 3 - 5개 존재

bb = '프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그램)'
print(bb.find('파이선'))
print(bb.rfind('파이썬'))
print(bb.index('파이썬'))

# 공백 제거
# strip() - 좌우 공백제거, 문자 사이 공백은 제거되지 않음
# rstrip() - 오른쪽 공백제거
# lstrip() - 왼쪽 공백제거

a = '    abc '
print(a.strip()) 

input1 = input("이름을 입력하세요.>> ")
if '홍길동' == input1 : 
    print("맞습니다.", input1)
else:
    print("틀립니다.", input1)
    
a = '    abc '
print(a.strip()) 
print(a.replace(' ', ''))
# replace(변경전문자, 변경 후 문지) - 문자열 변경
# ' ',''은 빈공백 제거
a == "홍길동은 키가 180, 홍길동은 몸무게 70, 홍길동은 사는 곳은 서울입니다."
a.replace('홍길동','홍길자')
print(a)

# splist() -  문자열 분리 :  타입은 리스트로 분리 해줌
a = '홍길동, 100, 100, 1000, 300'
a_list = a.splist(',')
print(a_list[2])
b = '홍길동 유관순 이순신 김구'
b_list = b.splist(' ')
print(b_list[1])







a = "1, '홍길동', 80,80,80,240,80.00"
title = ['학번','이름','국어','영어','수학','합계','평균']

a_list = a.split(",")

print(*title, sep='\t') # sep 사이 간격 출력
print("-"*50)
print(*a_list, sep='\t')

# print(sep : 변수 사이사이 모두 적용, end : 마지막에 한 번 적용)

# join() - 문자열 결합
ss = "-"
print(ss.join('파이썬'))

# map() : 리스트를 입력 받아 처리하는 함수
a = ['100','90','80'] # 문자열
b = []
for i in a :
    print(b.append(int(i))) # 문자열을 int로 변경
    
print(a)
print(b)


# map() : 리스트를 입력 받아 처리하는 함수
a = ['100','90','80'] 
print(map(int,a))
b = list(map(int,a)) # map타입객체로 저장

print(a)
print(b)


aa = [1,2,3]
bb = list(map(aa*2,aa))
print(bb)
# map (function 함수 부분, 리스트데이터)

# 국어점수를 입력하세요.
while True:
    kor = input('국어점수를 입력하세요')
    if kor.isdigit():  # 숫자인지 확인
       
       break
    else:
        print("숫자가 아닙니다. 다시 입력하세요")

print("숫자로 변경 :", int(kor))

# isdigit() : 숫자인지 확인
# isalpha() : 문자인지 확인
# isalnum() : 문자, 숫자인지 확인
# islower() : 소문자 확인
# isupper() : 대문자 확인

















# def multi(x):
#     return x**2

# a = [1,2,3]
# b = list(map(multi,a))
# print(a)
# print(b)