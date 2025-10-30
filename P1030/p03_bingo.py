import random

# [5*5 = 25]
# 리스트 생성
a_list = list(range(1,26))
# 리스트 섞기
random.shuffle(a_list)
print(a_list)


while True:
    # 리스트 화면 출력
    print("-"*50)
    print("   [좌표 맞추기 게임]   ")
    print("-"*50)
    for i, a in enumerate(a_list):
        print(a,end="\t")
        if(i+1)%5 == 0:
            print()
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요 >> "))
    print()
    
    # 번호 비교
    for i, a in enumerate(a_list):
        if num == a:
            a_list[i] = "X"
            break