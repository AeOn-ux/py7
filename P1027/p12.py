# 년도 가져오기
import datetime
now = datetime.datetime.now()
year = now.year



# 주민번호를 입력받아, 나이를 출력하시오.
# jumin = input("주민번호를 입력하시오.")
# jm1 = jumin
# print(jm1[:2])
# print(125-int(jm1[:2]))

jumin = "990802-1111111" 
a1 = jumin[7] #a1타입 - 문자열
num = int(a1) #문자열 -> 정수타입변경
year1 = jumin[:2] #99 문자열
y_num = int(year1) #99 정수타입
# 1900년대생인지, 2000년대생인지 확인하시오
# 조건문
if num==1 or num==2:
    print(2025-(1900+ y_num)) # 2025-1999 = 26
else :
    print(2025-(2000+ y_num))  # 2025-2005 = 20
    
    
# print(125 - year1)
# print(2025-(2000+ y_num))