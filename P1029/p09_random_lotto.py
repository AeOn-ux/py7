# import random
# # 1~45 중 6개의 랜덤숫자를 출력하시오.
# # 중복은 안됨.
# my_list = []
# lotto = (random.sample(range(1,46), 6))

# # 6개 숫자를 입력 받아 출력하시오.
# for i in range(6):
#     num = int(input("숫자를 입력하시오"))
#     my_list.append(num)
# my_list.sort()    
# print("[  결과화면  ]")
# print("-"*50)
# print(lotto)
# print(my_list)


#################################################

import random
# 1~45 중 6개의 랜덤숫자를 출력하시오.
# 중복은 안됨.
# 1. 변수 선언
my_list = [] # 입력한 번호
c_list = [] # 맞춘번호
count = 0 #맞춘개수
lotto = (random.sample(range(1,46), 6))


# 2. 6개 숫자를 입력 받아 출력하시오.
for i in range(6):
    num = int(input("숫자를 입력하시오"))
    my_list.append(num)

# 3. 당첨번호 확인
for i in lotto:
    for j in my_list:
        if i == j:
            count = count + 1
            c_list.append(i)
            break

        
# 4. 결과화면 출력
print("[  결과화면  ]")
print("-"*50)
print(lotto)
print(my_list)


print("맞춘번호", c_list)        
print("정답개수 :", count)

# 5. 당첨금 출력
# 0,1개 - 0원, 2개 - 5천원, 3개 - 5만원, 4개 - 1백만원, 5개 - 5천만원, 6개 - 20억
if count==0 or count==1 :
    print("당첨금 : 0원")
elif count==2:
    print("당첨금 : 5,000원")
elif count==3:
    print("당첨금 : 50,000원")
elif count==4:
    print("당첨금 : 1000,000원")
elif count==5:
    print("당첨금 : 50,000,000원")
elif count==6:
    print("당첨금 : 2,000,000,000원")
    
    
    