
a = 1 # 전역변수
def cal():
    global a # 전역변수를 가져올 때 사용
    print("a:",a)
    # a=100 # 지역변수 - 함수가 벗어나면 값이 사라짐
    

cal() # a=100
print(a)










# # 두 수를 입력 받아, 두 수 사이의 합을 출력하시오
# # 1, 20 -> 55가 출력
# # 10, 1 -> 55가 출력
# def cal(n1, n2):
#     sum = 0
#     for i in range(n1,n2): # 앞의 숫자가 클 경우 자리 교환
#         sum += i
#     return sum

# sum = cal(1,10)
# print(sum)



# def cal(n1, n2):
#     if n1>n2:
#         n1,n2 = n2,n1
#     n3 = 0
#     if n1>n2:
#         n3 = n1

# sum = cal(1,10)
# print(sum)