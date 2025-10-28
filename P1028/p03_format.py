year = 2025
month = 10
day = 28
# 2025년 10월 28일
print("%d-%d-%d" % (year, month, day))
date1 = "{}년 {}월 {}일".format(year, month, day)
print(date1)

a=10
a_format = "{}".format(a)
a_format1 = "{:5d}".format(a)
a_format2 = "{:05d}".format(a)

print(a_format)


b = 25.23456789
b_format = "{}".format(b)
b_format1 = "{:.2f}".format(b)

print(b_format1)


a =10
print("%d" % a)
print("%5d" % a)
print("%0.5d" % a)

print("이름:{}, 이름:{}, 이름:{}, ".format('홍','길','동ㄴ'))


###
bank = [1, '이마크', 100000]
#1번 홍길동, 100,000원
# format()함수를 사용해서 출력하시오.
print("{}번 {} {:05d}원".format(bank[0], bank[1], bank[2]))

name = "유관순"
rank = 3
result = 98.234567
## 이름 : 유관순, 단계 : 3, 성공률 : 98.23%
print("이름:{}, 이름:{}, 이름:{}%".format(name,rank,result))

print(f"이름 : {name}, 단계 : {rank}, 성공률 : {result:.2f}%")