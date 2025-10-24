# 변수 - 파일을 저장하는 공간
# 타입 - 숫자(점수, 실수), 문자열, 불(True, False)
# 문자 + 숫자 : 불가능

num = None
print(type(num))
num = 100
print(type(num))

astr = 100
astr = "dkssud" # 마지막값이 타입으로 지정됨
astr = True
print (type(astr))

result = 100
result2 = result
result = result+200
print(result2) # 값은 얼마일까요? = 100