# 기본변수 - 1개 값을 저장, int, float, str, bool
# 복합변수 - 여러개 값을 저장
# 클래스 - 여러개의 변수, 여러개의 함수까지 저장

# 클래스 사용시 장점 - 변수, 함수 함게 저장, 변수에 접근하는 제한
# 한번에 여러개의 변수, 여러개의 함수를 바로 사용 가능
# 동일한 변수를 한 묶음



# def 함수명():
#     프로그램

# class 이름: # 첫글자를 대문자
#     프로그램


class Car:
    # color = "white"
    # speed = 0 # 전연벽수
    
    
    
    # Car() 객체선언일때 __init__ 함수 먼저 호출
    def __init__(self,color,speed):
        self.color = color # 변수가 없으면 생성
        self.speed = speed
    
    
    def upSpeed(self, speed): # 지역변수
        self.speed += speed
        
    
# 클래스를 사용하려면(변수를 호출하거나, 값을 입력하려면), 무조건 객체 선언을 해야 한다.
# 객체선언
# 참조변수명 = 클래스명()

c = Car("white",0) #c라는 참조변수
c.color = "white"
# 값읽기 - 참조변수명. 변수명
print(c.color)
# 값수정 - 참조변수명.변수명 = "값입력"
c.color = "red"
print(c.color)


c2 = Car("red",100)
c2.upSpeed(100)
print(c2.speed)












# a = [12,30,20]
# a[0] = 50
# print(a)
# # aa = int(input("시간을 입력하세요.>> "))
# # if aa>>24:
# #     print("에러입니다.")
# #     # 프로그램 종료
# # a[0] = aa

# class cal:
#     __hour = 12 # 접근제한
#     minute = 30
#     second = 20
    
#     def sethour(self, hour):
#         if hour>23:  
#             print("23보다 큰 수는 입력을 할 수 없습니다.")
#             return
#         self.__hour = hour
#     def gethour(self):
#         return self.__hour
    
# time = cal()
# time.minute = 100
# print(time.minute)
# # print(time.__hour) # 클래스의 변수에 직접접근제한
# print(time.sethour(50))
# print(time.gethour())