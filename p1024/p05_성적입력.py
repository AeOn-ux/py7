# 이름 입력 - str %s
# 국어점수 입력 - int
# 영어점수 입력 - int
# 수학점수 입력 - int
# 합계 - int %d
# 평균 - int %f

# % print 출력
name = input("이름을 입력하세요.")
# print(name)
# print("%s" % name)

kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
print("%s   %d" % (name, kor)) # 위에 int를 붙인이유:이름(%s)는 문자지만 점수(%d)는 숫자.
print("%s   %d, %d, %d" % (name, kor, eng, math))
total = kor+eng+math
print("%s   %d, %d, %d, %d" % (name, kor, eng, math, total))
print("합계:%d" % total)
avg = (total)/3 # 실수(f)
print("%s   %d, %d, %d, %d, %f" % (name, kor, eng, math, total, avg))
print("%s   %d, %d, %d, %d, %.2f" % (name, kor, eng, math, total, avg))