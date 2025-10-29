# 이름, 국어
# 입력받아 출력하시오
# 이름 : 홍길동, 국어 : 100

print("[ 학생성적입력 ]")
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total = kor+eng+math
avg = total/3
print("이름 : {}".format(name))
print("국어 : {}".format(kor))
print("영어 : {}".format(kor))
print("수학 : {}".format(kor))
print("합계 : {}".format(kor))
print("평균 : {}".format(kor))

print("이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,math,total,avg))