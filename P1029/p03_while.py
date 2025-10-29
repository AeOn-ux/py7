# 1~10까지 합을 구하시오
# for
sum = 0
for i in range(1,11): #자동증감이 됨
    sum = sum + i
print(sum)


# while
sum = 0 
i = 1
while i<11:
    sum = sum + i
    i = i + 1 # 증감식 - 추가
print(sum)


# 5번 동안 숫자를 입력 받아 합계를 출력하시오.
# for문, while문
sum = 0
for _ in range(5):
    num = int(input("숫자를 입력하세요"))
    sum = sum + num
print("합계 :", sum)

sum = 0
i = 0
while i<5:
    num = int(input("숫자를 입력하세요."))
    sum = sum + num
    i = i + 1
print("합계 :", sum)





while True :
    print("[ 학생 성적 프로그램 ]")
    print("1. 학생 성적 입력 ")
    print("2. 학생 성적 출력 ")
    print("3. 학생 성적 수정 ")
    print("0. 프로그램 종료 ")
    print("="*30)
    num = int(input("원하는 번호를 입력하세요."))
    if num == 0:
        break
    elif num == 1 :
        # 학생성적입력
        print("[ 학생 성적 입력 ]")
    print()
        
    
    
# while True :
#     print("[ 학생 성적 프로그램 ]")
#     print("1. 학생 성적 입력 ")
#     print("2. 학생 성적 출력 ")
#     print("3. 학생 성적 수정 ")
#     print("0. 프로그램 종료 ")
#     print("="*30)
#     no = int(input("원하는 번호를 입력하세요."))
#     # no == 0 비교
#     if no == 0:
#         break
#     elif no == 1 :
#         # 학생성적입력
#         print("[ 학생 성적 입력 ]")
#     print()