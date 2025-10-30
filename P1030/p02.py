import random
# 4*4 출력
a_list = list(range(1,10))
print(a_list)

# for a in a_list:
#     print(a)
    
# for a in a_list:
#     print(a,end="\t")
#     if a%3 == 0:
#         print()
        
# 무한 반복 실행
while True:      
    print("[  좌표맞추기게임  ]")   
    print("-"*50)     
    random.shuffle(a_list)
    print(a_list)
    for i, a in enumerate(a_list):
        print(a,end="\t")
        if(i+1)%3 == 0:
            print()
    print("-"*50)  
    num = int(input("원하는 번호를 입력하세요 >> "))
    # 9번을 입력하면 9자리가 X표시가 되어야함.
    for i, a in enumerate(a_list):
        if a == num:
            a_list[i] = "X"
