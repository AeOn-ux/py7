# 반복문 - 여러번 실행
# for문, while()
# 조건문 - if문

# range - 범위, range(10) 10번 반복
# range(시작, 끝-1, 스탭), range(끝):0 ~ 끝-1
for i in range(10):
    print(i)
    
for i in range(5):
    print("안녕하세요.")
    
for i in range(5):
    print("hello.")
    
for i in range(5):
    print(i+1, "번째 안녕")
    
for i in range(1, 6):
    print(i+1, "번째")


# 1~10의 합계를 구하시오    
sum = 0
for i in range(1,11):
    sum = sum + i
print("합계 :", sum)
print("{}번째: {}".format(i, sum))

a_list = ["홍길동", 100, 90, 80]
for a in a_list:
    print(a)
    
# 2차원 리스트 - for문 2번, 3차원 리스트 - for문 3번
name = "현빈남궁민오세훈"
for i in name:
    print(i)
    
# range() 숫자를 입력하세요 10번 출력
for i in range (10):
    print(i+1, "번째 안녕하세요.")
    
num = input("숫자를 입력하세요")
for i in range (10):
    # print(i+1,"번째")
    input(i+1,"번째")
    
# sum = 0
for i in range (10):
    num = input(i+1,"번째".format(i+1))
    sum = sum+num
print("합계 :", sum)