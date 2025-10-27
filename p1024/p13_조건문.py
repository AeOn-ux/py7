# if문은 꼭 :으로 닫아줘야 한다.
# if문은 꼭 들여쓰기로 해야한다.
if 10>5:
    print("정상입니다.")
else:
    print("비정상입니다.")
    
# 숫자를 입력 받아 100보다 큰 수인지 아닌지 출력하시오.
# 100보다 큰 수 입니다. 100보다 작은 수 입니다.
num1 = 200
num2 = 25
if(num1>100):
    print("100보다 큰 수 입니다.")
else:
    print("100보다 작은 수 입니다.")
    
if(num2>100):
    print("100보다 큰 수 입니다.")
else:
    print("100보다 작은 수 입니다.")
    
    
num3 = int(input("숫자를 입력하세요."))
if(num3>100):
    print("100보다 큰 수 입니다.")
else:
    print("100보다 작은 수 입니다.")
    
# 입력된 숫자가 짝수인지 홀수인지 출력하시오.
# 짝수입니다. 홀수입니다.
# num%2 == 0
# if(num>100):
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")

num = 7456
num%2==0
if(num>100):
    print("짝수입니다.")
   
# 내부 모듈 - 외워두기
import datetime
now = datetime.datetime.now()
print(now) # 시간 전체 출력

print(now.year,"년도")
print(now.month,"월")
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# 입력한 주민번호의 월을 파악해서 현재 날짜와 같은 월이면 이벤트 대상입니다.
# 이벤트 대상입니다., 이벤트 대상이 아닙니다. 를 출력하시오.
jumin = input("주민번호를 입력하시오.")
if int(jumin[2:4])==now.month:
    print("이벤트 대상입니다.")
else:
    print("이벤트 대상이 아닙니다.")