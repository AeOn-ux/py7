
# # 입력한 글자를 입력한 숫자만큼 반복 출력
# # 안녕하세요 3

# str1 = input("글자를 입력하세요>> ")
# num = int(input("반복횟수를 입력하세요>> "))
# for i in range(num):
#     print(str1)
    
    
# # 입력한 글자를 입력한 숫자만큼 반복 출력
# # 안녕하세요 3
# def s_print(str1,num):
#     for i in range(num):
#         print(str1)
        
# str1 = input("글자를 입력하세요>> ")
# num = int(input("반복횟수를 입력하세요>> "))
# s_print(str1,num)





# 함수를 사용 cal(3개)
# 두 수와 +,-,*,/ 4개 중에 1개를 입력받아 두 수의 결과를 출력하시오

# 함수선언(정의)
num1 = int(input("숫자를 입력하세요>> "))
num2 = int(input("숫자를 입력하세요>> "))
str1 = input("원하는 사칙연산 기호를 입력하세요(+,-,*,/)>> ")

# 10 + 2 = 12
# 결과값을 출력하시오

def cal(num1, num2,str1) : # 함수정의
    if str1 == '+':
        print(num1+num2)
    elif str1 == '-':
        print(num1-num2)
    elif str1 == '*':
        print(num1*num2)
    else:
        print(num1/num2)
    

cal(num1, num2, str1)



# cal(1,10)
# 1에서 10까지의 합이 출력되도록 구성하시오
# 함수 사용 목적 -  반복제거, 유지보수 편의성, 코드 관리 평의성
# 함수정의



def cal(num1,num2):
    sum = 0
    for i in range(num1, num2+1):
        sum += i
    print(sum)



# 함수호출
# 값을 호출하시오


num1 = int(input("숫자를 입력하세요>> "))
num2 = int(input("숫자를 입력하세요>> "))
cal(num1,num2)

cal(2,10)
cal(5,9)
cal(11,20)