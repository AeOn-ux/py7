# 로또 맞추기 프로그램을 구현하시오

import random
#1. 변수 선언
my_list = []
c_list = []
count = 0
lotto = random.sample(range(1, 46), 6)

#2. 6개 번호 생성
for i in range(6):
    num = int(input("숫자를 입력하시오."))
    my_list.append(num)

#3. 6개 번호 입력
# for i in lotto:
#     for j in my_list:
#         if i == j:
#             count = count + 1
#             c_list.append(i)
#             break
        

for i in my_list:
    if i in lotto:
        count = count + 1
        c_list.append(i)
       

#4. 번호 확인
print("[ 결과확인 ]")
print("-"*50)
print("로또번호 공개 :", lotto)
print("입력한 번호 :", my_list)
print("-"*50)
print("맞춘 번호 :", c_list)
print("맞춘 개수 :", count)


#5. 결과 출력
if count == 0 or count == 1:
    print("당첨금액 : 0원")
elif count == 2:
    print("당첨금액 : 5천원")
elif count == 3:
    print("당첨금액 : 5만원")
elif count == 4:
    print("당첨금액 : 100만원")
elif count == 5:
    print("당첨금액 : 5천만원")
else:
    print("당첨금액 : 20억원")