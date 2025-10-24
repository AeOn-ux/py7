# 자료형 - 변수 : 값을 저장하는 공간
# 타입 - 숫자(정수, 실수), 문자열, bool(true, False)
# 문자열 + 숫자 : 더하기를 할 수 없다.
# print("합계:"+100)는 에러
print("합계:", 100) # 쉼표로 구분하면 다른 타입도 넣을 수 있다.
print(100, 200, 300, 400, 500)
print("합계", 100, True) # 다른 타입도 출력 가능

# 숫자를 입력해서 출력하시오.
num = input("숫자를 입력하세요.") # input타입 : 문자열
print("숫자:", int(num))
num2 = input("숫자를 입력하세요.")
print("숫자:", int(num2))

# 숫자를 입력해서 출력하시오.
num = input("숫자를 입력하세요.") # input타입 : 문자열
print("숫자:", float(num)) # 문자열 -> 정수타입으로 변경 : int
num2 = input("숫자를 입력하세요.")
print("숫자:", float(num2))