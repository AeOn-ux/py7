# 990802-1111111
# 011128-4444444
# 주민번호를 입력받아, 남자인지 여자인지 출력하시오
jumin = input("주민번호를 입력하시오.")
a = jumin[7]
if a ==1:
    print("남자입니다.")
else:
    print("여자입니다.")
    
import datetime
now = datetime.datetime.now()
month= now.year

m = int(jumin[2:4])
if m ==month:
    print("이벤트 대상입니다.")


