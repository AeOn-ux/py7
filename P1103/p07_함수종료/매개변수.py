
# return : 함수를 호출한 곳으로 값을 전달할때 사용
def cal(a,b): # a,b 타입  - int, int
    return (a+b)
    # return a+b # 함수끝을 만나면 함수 종료됨
    # return     # return을 만나면 함수 종료
    
num1 = cal(10,5)
num2 = cal(2,7)
num3 = cal(3,5)
# num4 = cal("a",b) # 에러, 타입을 꼭 일치시켜야 한다

# 3개의 계산 더하기, 빼기를 구하시오
print(num1+num2+num3)
print(num1-num2-num3)