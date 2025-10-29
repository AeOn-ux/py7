# n_list = []
# # # 반복시작
# # while True:
# #     name = input("이름을 입력하세요.")
# #     n_list.append(name) # 이렇게 넣어야지 옆으로 이름이 추가됨!
# #     print(n_list)
# #     # print("이름")
# #     # print("-"*50)
# #     # print("{}".format(name))

# n_list.append(1)
# n_list.append(2)
# n_list.append(3)
# n_list.insert(0,0)
# n_list.extend([4,5,6]) # extend는 list 타입으로 추가
# n_list.append(['홍길동',100])
# print(n_list)



# n_list = []
# while True : 
#     name = input("이름을 입력하세요")
#     n_list.append(name)
#     print(n_list)
 
 
 
 
 
 
 
 
 
    

# 
# n_list = []
# while True : 
#     name = input("{}번째 이름을 입력하세요".format(len(n_list)+1))
#     n_list.append(name)
#     print(n_list)


n_list = []
i = 0
while True : 
    if i<4:
        name = input("{}번째 이름을 입력하세요".format(len(n_list)+1))
        kor = int(input("{}번째 국어점수를 입력하세요".format(len(n_list)+1)))
        eng = int(input("{}번째 영어점수를 입력하세요".format(len(n_list)+1)))
        math = int(input("{}번째 수학점수를 입력하세요".format(len(n_list)+1)))
        n_list.append([name,kor,eng,math])
        print(n_list)
        i = i + 1
    else:
        break    
    
# 전체출력
print("이름\t국어\t영어\t수학")
print("-"*50)
# for i in range(4):
#     print("{}\t{}".format(*n_list[i]))
for i in range(len(n_list)):
    print("{}\t{}\t{}\t{}".format(*n_list[i]))