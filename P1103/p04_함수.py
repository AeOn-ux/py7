# 함수정의
# def 함수이름(매개변수):
   # pass
# 함수 호출 - 함수이름()

def kor_hello():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

def eng_hello():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")


eng_hello()
kor_hello()
eng_hello()
kor_hello()
eng_hello()
kor_hello()
for i in range(10):
    kor_hello()
    
    
    
    
    
def calculate(a,b) : # 함수정의
    print("덧셈", a+b)
    print("빼기", a-b)
    print("곱하기", a*b)
    print("나누기", a/b)

a,b = 10,2
calculate(a,b)  # 함수호출
a,b = 5,3
calculate(a,b)
a,b = 2,1
calculate(a,b)