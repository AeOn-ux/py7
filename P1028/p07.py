# for문
# 구조- for 변수 in 범위(range, list, 문자열) : 

for i in range(5):
    print("반갑습니다.")
    
a_list = []
for i in range(5):
    num = int(input("숫자를 입력하세요"))
    if num%2 == 0:
        break #반복문을 중지시키는 명령어
    #append
    a_list.append(num)
 
print("리스트 :", a_list)   


# 1~5 for문을 사용해서 출력하시오.
for i in range(5): # for :
    print          # 반복해야 할 내용 들여쓰기를 해야 함
    

# 숫자를 입력 받아, 입력받은 값을 출력하는 것을 5번 반복하시오
for i in range(5):
    num = int(input("숫자를 입력하세요"))
    print(num)
    
# 1~10까지 숫자의 합을 출력하시오. 반복 10번
sum=0
for i in range(10): # 0~9
    sum = sum + i
    print("합계 :", sum)
    
sum=0    
for i in range(1,11): # 1~10
    sum = sum + i
    print("합계 :", sum)
    
    
# 1~10까지 홀수 합계를 구하시오
# range와 if를 사용해서 할 것
sum = 0
for i in range(1,11):
    if i%2 ==1:
        sum = sum + 1
print("합계 :", sum)