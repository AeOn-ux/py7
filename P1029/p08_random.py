import random
# randrange() 1~10까지의 랜덤숫자를 3개를 출력하시오.
print(random.randrange(1,11))
print(random.randrange(1,11))
print(random.randrange(1,11))
print(random.sample([1,2,3,4,5,6,7,8,9,10],3))
print(random.sample(range(1,11),3))


# # 1~10 사이에 있는 랜덤숫자 생성
# r_num = random.randrange(1,11)
# for i in range(5):
#     my_num = int(input("숫자를 입력하세요."))
#     if r_num == my_num:
#         print("당첨되었습니다.")
#         break
#     else:
#         print("땡!!!")
        
r_num = random.randrange(1,101)
n_list = []
for i in range(7):
    my_num = int(input("숫자를 입력하세요."))
    n_list.append(my_num) # 리스트 추가
    if r_num == my_num:
        print("당첨되었습니다.")
        break
    elif r_num > my_num:
        print("땡!!! 더 크지롱~")
    elif r_num < my_num:
        print("땡!!! 더 작지롱~")
        
print("당첨번호 :",r_num)
print("입력번호 :", n_list )