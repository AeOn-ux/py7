print("%10.2f" % (10/3)) # 10자리 공간확보
print("%010.2f" % (10/3)) # 빈공백을 0으로 처리

# 숫자 3개를 입력받아서, 2025년 10월 27일 형태로 출력하시오
# % print를 사용해서 출력할 것
# 2025, 10, 27
# 2002, 10 , 11
year = input(2025)
month = input(10)
day = input(11)
print(year, "년", month, "월", day, "일")
print ("%s 년 %s 월 %s 일" + year + month + day)
