# 구구단을 출력하시오
for i in range(2,10):
    for j in range (1,10):
        print(i, "*", j)
        
for i in range(2,10):
    for j in range (1,10):
        print("[{}단]".format(i))
        print(i, "*", j, "=", i*j)
        print("{}*{}={}". format(i,j,i*j))
        
for i in range(2,10):
    for j in range (1,10):
        print("{}*{}={}". format(i,j,i*j))
        
# 짝수만     
for i in range(2,10):
    if i%2 !=0:
        break
    for j in range (1,10):
        print("{}*{}={}". format(i,j,i*j))
        
for i in range(2,10):
    if i%2 !=0:
        continue #1번만 제외, break는 완전 중지
    for j in range (1,10):
        print("{}*{}={}". format(i,j,i*j))
        
        
 
 # 중첩 for문을 사용해서 00,01,02,03....99     
for i in range(0,10):
    for j in range(0,10):
        print("{}{}".format(i,j))

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
           print("KB번호표 : {}{}{}".format(i,j,k))
           
           
           
           
# 구구단 최종!
for i in range(2,10):
    if i%2 !=0:
        continue #1번만 제외, break는 완전 중지
    print("[{}단]".format(i))
    for j in range (1,10):
        print("{}*{}={}". format(i,j,i*j))
        


# 501~1000 까지 홀수의 합을 출력하시오
sum = 0
for i in range(501,1001):
    if i%2 == 1:
        sum = sum + i
print("합계 :", sum)
        
        

# 1~100까지 3의 배수의 합을 출력하시오
sum = 0
for i in range(1,101):
    if i%3 == 1:
        sum = sum + i
print("합계 :", sum)



fruits = ['망고', '딸기', '메론', '복숭아']
for fruit in enumerate(fruits):
    print(fruit) 
    
    
# enumerate(리스트) - 리스트번호, 리스트값
print("[과일리스트]")    
for i,fruit in enumerate(fruits):   # enumerate()함수 : index번호 리턴
    print("{},{}".format(i+1,fruit)) 
    
for i in range(len(fruits)):
    print("{},{}".format(i+1,fruits[i])) 