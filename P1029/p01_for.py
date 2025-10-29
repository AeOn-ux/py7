# for 변수 in 범위 : 

for i in range(10):
    pass # 아무것도 일어나지 않음
    print ("프로그램 종료")
    break # 이 시점에서 반복문을 종료

# continue - 1회 반복문 제외시켜줌./ if와 짝궁
for i in range(10):
    if i ==3:
        continue  # 3만 제외
    print(i)


for i in range(10):
    if i%2 ==0:
        continue  # 홀수만 출력
    print(i)
    
for i in range(10):
    if i%2 ==0:
       print(i)
    continue  # continue의 위치에 따라 달라짐. 짝수만 출력


sum=1
for i in range(2,10):
    for j in range(1,10):
        print("숫자 :")
        
for i in range(2,10):
    print(i)
    for j in range(1,10):
        pass
    print("-"*50)
    
for i in range(2,10): #1,2,3,4,5,6,7,8
    print(i)
for i in range(8): #-0,1,2,3,4,5,6,7
    print(i)

for i in range(5,22):
    print(i)
for i in range(1,11):
    print(i)
for i in range(10):  #(0,9)
    print(i)
for i in range(10):
    if i%2!=0:
        print(i)
        
        
# 구구단을 출력하시오
for i in range(1,10):
    if i%2==0:
        continue
    print("[{}단]".format(i))
    for j in range(2,10):
        print("{}*{}={}".format(i,j,i*j))
        
names = ['홍길동', '유관순', '이순신', '김구','강김찬']
# for 변수 in 범위: -> range, list, 문자열, 딕셔너리, 튜플
for name in names:
    print(name)
for name in enumerate(names): # index번호, 값을 리턴
    print(name[0], name[1])
for i,name in enumerate(names): # index번호, 값을 리턴
    print("{},{}".format(i+1,name))
    
n_list = [
    [1,'홍길동'],
    [2,'유관순'],
    [3,'이순신']
]
for ns in n_list:
    for n in ns:
        print(n,end=".")
    print()
    
    
    
a_list = []
# for문을 사용해서 '0'을 10개 들어가는 리스트를 만드시오.
# append
for i in range(10):
    a_list.append('0')
print(a_list)
# 리스트 타입 변환
a_list = list('0'*10)
print(a_list)
# 리스트 내포
a_list = ['0' for _ in range(10)]
print(a_list)

a_list = [i*i for i in range(1,10)]
print(a_list)
