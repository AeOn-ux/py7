a = 100
if a>10 :
    print("참입니다.")
else:
    print("거짓입니다.")
    
    
# 문자열 -> 정수타입    
num = int(input("숫자를 입력하세요.>>"))
if num>=0:
    print("양수입니다.")
    
    
# 입력한 숫자에 50을 더해서 100보다 큰 수인지 출력하시오.
num1= int(input("숫자를 입력하시오."))
num1 = num1+50
if num1>100:
    print("100보다 큽니다.")
else:
    print("100보다 작습니다.")
    
if num1>=100:
    print("입력한 값 :", num1-50, "현재값 :", num1, "100보다 큰 수 입니다.")
    print("입력한 값 : %d, 현재값 : %d, %s" % (num1-50, num1, "100보다 큰 수 입니다."))
    
    
# 입력한 값이 짝수인지 홀수인지 출력하시오
num2 = int(input("숫자를 입력하시오."))
if num2 % 2 == 0:
    print("입력한 값 : %d, 짝수입니다."%num2)
else:
    print("입력한 값 : %d, 짝수입니다."%num2)
    
# 문자열 슬라이싱
str1 = "안녕하세요" #안(0)녕(1)하(2)세(3)요(4) #안(-5)녕(-4)하(-3)세(-2)요(-1)
print(str1[3]) #세
print(str1[1:3]) #녕하
print(str1[1:]) #녕하세요
print(str1[:3]) #안녕하
print(str1[:]) #안녕하세요
# [처음번호:끝번호:스탭(증가)]
print(str1[::1]) #안녕하세요
print(str1[::-1]) #요세하녕안
print(str1[1:4:2]) #녕세
print(str1[1:5:3]) #녕요

a =123456789
print(a[::2]) #홀수만
print(a[1::2]) #짝수만
# 3의 배수값만
print(a[2:8:3])

### 입력을 받아, 마지막 글자를 출력하시오.
input1 = input("파일 이름을 입력하세요.") #a.hwp
print("마지막 글자 :", input[-1]) #p
print("마지막 글자 :", input[-3:]) #hwp
