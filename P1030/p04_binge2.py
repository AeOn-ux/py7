a_list = [1,2,3,4,5]
b_list = list(range(1,6))
c_list = [i for i in range(1,6)] # 리스트 내포
print(a_list)
print(b_list)
print(c_list)

# append,insert, extend
# pop, del, remove, clear
# 수정 : a_list[index] = 값
# index : 해당위치값 리턴
aa_list = [10,5,15,7,9]
print(aa_list.index(10))



# 1. 비교
print(aa_list) # [10,5,X,7,9]
num = int(input("원하는 번호를 입력하세요 >> ")) # 15
for idx, aa in enumerate(aa_list): # (2,15)
    if aa == num:   # 10 == 15, 5 == 15, 15 == 15
        aa_list[idx] = "x"  #aa_list[2] = 'X'
print(aa_list)
        
# 2. 비교
aa_list = [10,5,15,7,9]
print(aa_list)
num = int(input("원하는 번호를 입력하세요 >> "))
if num in aa_list:
    aa_list[aa_list.index(num)] = "X"
print(aa_list)
        


# 5*5의 2차원 형태 리스트를 생성
# 좌표만들기
import random
a_list = list(range(1,26))
random.shuffle(a_list)
print(a_list)

while True:
    print("-"*50)
    print("   [ 좌표 맞추기 게임]   ")
    print("-"*50)
    for i, a in enumerate(a_list):
        print(a,end="\t")
        if(i+1)%5 == 0:
            print()
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요 >> "))
    print()
    
    for i, a in enumerate(a_list):
        if num in a_list:
            a_list[a_list.index(num)] = "X"
            break
