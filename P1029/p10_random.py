import random

# 로또번호 맞추기 프로그램
# 1. 변수선언, 로또번호 생성
my_list = []
c_list = []
count = 0
lotto = random.sample(range(1,46), 6)

print(lotto)
# 2. 숫자 입력
for i in range(6):
    num = int(input("숫자를 입력하세요"))
    my_list.append(num)


# 3. 당첨번호 확인
for i in lotto: # [24, 14, 28, 5, 33, 41]
    for j in my_list: # [40, 21, 35, 26, 41, 12] 
        if i == j: # 24 == 35
            count = count + 1
            c_list.append(i)
            break


# 4. 결과화면 출력
print("[   결과 화면 출력   ]")
print("-"*55)
print("-"*55)
print("로또번호공개 :", lotto)
print("입력하신번호 :", my_list)
print("-"*55)
print("-"*55)
print("맞춘 번호 :", c_list)
print("정답개수 :", count)

# 5. 당청금 출력
if count==0 or count==1:
    print("당첨금액 : 0원")
elif count==2:
    print("당첨금액 : 5000원")
elif count==3:
    print("당첨금 : 50,000원")
elif count==4:
    print("당첨금 : 1000,000원")
elif count==5:
    print("당첨금 : 50,000,000원")
elif count==6:
    print("당첨금 : 2,000,000,000원")