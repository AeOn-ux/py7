# 숫자 2개를 입력 받아 사칙연산 결과를 출력하시오
# % print()를 사용해서 출력하시오
num1 = input("숫자를 입력하세요") # 문자열
num2 = input("숫자를 입력하세요")
print("%s + %s = %d" % (num1, num2, int(num1)+int(num2)))
print("%s - %s = %d" % (num1, num2, int(num1)-int(num2)))
print("%s * %s = %d" % (num1, num2, int(num1)*int(num2)))
print("%s / %s = %f" % (num1, num2, int(num1)/int(num2)))


num1 = input("숫자를 입력하세요") # 문자열
num2 = input("숫자를 입력하세요")
print(int(num1)+int(num2))


num1 = int(input("숫자를 입력하세요")) # 문자열
num2 = input("숫자를 입력하세요")
print(num1+int(num2))
