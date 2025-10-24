# input() 함수
# a = input("숫자를 입력하세요") # input=str타입 - 입력받는 모든것이 문자열타입
# print(a+200)
# 위에는 에러 입력값
print("100")
# print("100"+200) # 문자열+숫자
# print(int(a)+200) # 에러

# input() 함수
# 문자열을 입력받는 함수, 입력받는 모든 것이 문자열 타입
# 문자열 + 숫자 : 불가능


### num, num2 2개를 입력받아 숫자타입으로 변경 후 사칙연산 결과를 출력하시오.
### int(num)

num1 = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

input1 = input("이름을 입력하세요.")
input2 = input("나이를 입력하세요.") # 이 경우에도 숫자를 입력하면 문자열 타입.
print(input1, input2)
