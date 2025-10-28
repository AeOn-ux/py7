year = 2025
month = 10
day = 28
print("%d년 %d월 %d일" % (year, month, day))
day_format = "{:d} 년 {:0d} 월 {} 일" .format(year, month, day)
print(day_format)

# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# 1000원 이상 입력하세요.
# 총금액 : 1,000,000원
n1 = int(input("금액을 입력하세요."))
n2 = int(input("금액을 입력하세요."))
n3 = int(input("금액을 입력하세요."))
total = n1+n2+n3
print("%d 원, %d 원, %d 원" % (n1, n2, n3))
print("총금액 : {:,d} 원".format(total))
print("1번 금액 : {:,d} 원, 총금액 : {:,d} 원".format(n1, total))

# 홍길동, 국어, 영어, 수학, 합계, 평균
name = input("이름을 입력하시오")
kor = int(input("국어 점수를 입력하시오."))
eng = int(input("영어 점수를 입력하시오."))
math = int(input("수학 점수를 입력하시오."))
a_list = ['홍길동', 100, 100, 100, 300, 100.0]
print("이름:{},국어:{},영어:{},수학:{}". format\
    (a_list[0], a_list[1], a_list[2], a_list[3]))
print("이름:{},국어:{},영어:{},수학:{}". format\
    (*a_list))

ㅁ =10
ㅠ = 20