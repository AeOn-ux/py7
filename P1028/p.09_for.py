# # for 변수 in 범위 :
# # end=""를 붙이면 range값을 역순으로 출력할 수 있음.
# for i in range(10):
#     print(i, end = " ")
    
# # 1부터 100까지 합을 구하시오.
# sum = 0    
# for i in range(1,101):
#     sum = sum + i
# print("합계 :", sum)

# # 10을 넘는 범위와 위치는 얼마를 더할때 일까요?
# sum = 0
# for i in range(1,101):
#     if sum>100:
#         break
#     sum = sum + i
# print("합계 :", i, sum) # 5번째의 15라는 뜻이다.
# print(f"{i-1} 번째 : {sum}")

# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     if sum>100:
#         break
# print("합계 :", i, sum) # 5번째의 15라는 뜻이다.
# print(f"{i} 번째 : {sum}")

# 1*2*3*4*5*6*7*8*9*10 결과값을 출력하시오.
# result = 1
result = 1
for i in range(1,11):
    result = result * i
    print(i, result)
    if result>100:
        break
print(f"{i} 번째 : {result}")