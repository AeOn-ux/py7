# 모듈 : 함수의 집합
# 다른 파일의 모듈을 사용하려면, import를 해야 사용 가능
# import를 하면 이름.함수명으로 호출해야 한다.

import Func # Func.py 파일의 모든 함수를 가져옴

# import 모듈이름.함수명 으로 사용
# Func.fun1()
# print(Func.func1())

# from 파일명 import 함수를 정의하면 파일명 생략 가능
# 모듈명 생략 가능
# from 모듈명 import 함수, 클래스
# 유사한 함수 그룹에 묶어두면 사용하기 편함
from Func import *
print(func1())
func2()     # 함수사용
s1 = stu()  # 클래스 사용


# 예제
# 수학공식
from math import sin, cos, tan, floor, ceil

# floor 소수점 버림, ceil 소수점 올림, round 반올림
print(floor(1.95))
print(ceil(1.2))
print(round(1.59)) # round 내장함수




# 모듈 이름이 너무 길 때 줄여 사용가능 : as 별칭
import random as r

print(r.randint(1,5))



import math
# dir : 모듈 안에 모든 함수를 보여주는 명령어
print(dir(math)) # math  안에 있는 모든 함수를 보여줌
print(dir(r))    # random 안에 있는 모든 함수를 보여줌


# 날짜와 시간을 가져오는 모듈
# 파이썬 - 날짜, html - 날짜, 자바스크립트 - 날짜, db - 날짜
import datetime
now = datetime.time.now()
print(now)
print(now.year) # tear,month,day,hour,minute,second

import time

print("a")
time.sleep(5) # 5초동안 대기
print("b")







