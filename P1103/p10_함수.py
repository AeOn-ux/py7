# # 기본매개변수 - 호출함수(매개변수) 개수와 함수 정의 매개변수 개수가 같아야 함
# # 가변매개변수 - 기본매개변수가 앞에 오고, 뒤에 가변매개변수가 오면 매개변수 개수가 달라도 된다. 표기는 *매개변수 라고 한다.

# def func(a,*b):
#     print(a)
#     for i in b:
#         print(i)
        
        
# func(1)

# # 키워드매개변수 - 변수에 미리 값을 할당 b+10, b의 값이 들어오면 들어온 값 할당\
# #                b의 값이 없으면 기본 10값으로 셋팅


# def func(a,b=10): # 키워드 매개변수
#     print(a+b)

# func(20,10)
# func(10) # 할당이 되지 않으면 b=10 라는 초기값을 할당함





def func(*a, b=10):
    print(b)
    for i in a:
        print(i)

func(10,1)







# from Stufunc import *    # StuFunc.py 파일 안의 모든 함수를 가져옴


# # 학생 성적 프로그램

# while True:
#     screen_print() # 함수호출
#     choice = int(input("원하는 번호를 입력하세요>>"))
    
#     if choice == 1: # 학생 성적 입력 부분
#         stu_input()
#         stu_print()  # 함수 호출함으로써 코드 중복을 제거
#     elif choice == 2: # 학생 성적 cnffur 부분
#         stu_print()
        
