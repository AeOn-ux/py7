# 함수 : 특정명령어를 집합 - 반복을 제거, 유지보수 쉽게, 코드량 감소

print() # 프린트 함수

# 함수 형태
def 함수명(매개변수):
    pass

# 함수호출
# 함수명()

def calculate() : # 함수정의
    print("더하기")
    print("빼기")
    print("곱하기")
    print("나누기")

a,b = 10,2
calculate()  # 함수호출
a,b = 5,3
calculate()
a,b = 2,1
calculate()

# a,b = 10,2
# print("더하기 :", a+b)
# print("빼기 :", a-b)
# print("곱하기 :", a*b)
# print("나누기 :", a/b)
# print(a,b)

# a,b = 5,3
# print("더하기 :", a+b)
# print("빼기 :", a-b)
# print("곱하기 :", a*b)
# print("나누기 :", a/b)

