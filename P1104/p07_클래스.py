# 클래스
# 클래스 내 변수, 함수를 사용하려면, 무조건 객체 선언을 해야 사용할 수 있음
# 객체선언 : 참조변수 = 클래스명

# class Car:
#     color = "" # 전역변수
#     speed = 0
    
    
    
    
#     # 생성자 : 객체선언 시 값을 바로 할당할 수 있도록 해줌
#     def __init__(self, color, speed): # 지역변수
#         self.color = color # self.변수명 시 없으면 클래스에 변수 추가해 줌
#         self.speed = speed
#         self.tire = 4  # 변수가 없으면 자동생성
#         pass
    
    
    # 생성자 생략
    # 클래스 내 함수(self) : 함수 밖에 변수를 찾아서 변경하기 위해 사용
    # 클래스 내 함수 첫 매개변수로 self
    # def upspeed(self, num):
    #     # 함수 내 변수를 선택
    #     self.speed += num
        
    # def downspeed(self, num):
    #     self.speed -= num
        
# c1 = Car()     # 객체선언 = 변수, 함수 사용
# # 사용방법 - 참조변수. 변수명
# # 함수 - 참조변수. 함수명
# print(c1.speed)
# c1.upspeed(10) # 클래스 내 함수 호출 - 참조변수.함수명()
# print("스피드 :", c1.speed)

# 속도 50으로 증가, 속도 30 감소, 속도 100 
# 속도 출력
# 색상 => 파랑 변경하시오

class car:
    color = ""
    speed = 0
    
    def __init__(self, color, speed): # 지역변수
        self.color = color # self.변수명 시 없으면 클래스에 변수 추가해 줌
        self.speed = speed
        self.tire = 4  # 변수가 없으면 자동생성
        pass
    
    def upspeed(self, num):
        self.speed += num
        
    def downspeed(self, num):
        self.speed -= num
        
    # def color(self,cc):
    #     self.color == cc
        
# c2 = car()
# print(c2.speed)
# c2.upspeed(50)
# print("스피드 :", c2.speed)
# c2.downspeed(30)
# print("스피드 :", c2.speed)
# c2.upspeed(100)
# print("스피드 :", c2.speed)

# c2.color = '파랑'
# print("색상 :", c2.color)




# # 1. 객체선언 후 값 지정하는 방법
# c1 = car() # 객체지정
# c1.color = '파랑' # 변수값지정
# c1.speed = 100 # 변수값지정
# print(c1.color)
# print(c1.speed)
    
# 2. 생성자를 통해 값지정 = 생성자를 사용해서 프로그램을 함
c2 = car('파랑',100) # 생성자의 매개변수 개수를 맞춰야 함
print(c2.color)
print(c2.speed)
c2.door = 5 # 클래스에 변수가 없으면 클래스에 자동으로 추가됨
print(c2.door)