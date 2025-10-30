# a_list = [1,2,3,4,5,6,7,8,9]
# b_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # 1차원 리스트 출력
# for a in a_list:
#     print(a,end="\t")
# print()
# print("-"*50)
# for bs in b_list:P1030/p05_수정.py
#     for b in bs:
#         print(b,end="\t")
# print()        
# # b_list의 값 4를 100으로 변경         
# b_list[1][0] = 100
# print(b_list)
# b_list[2][1] = 50
# print(b_list)


# stu_list = [
#     ['이마크', 100,99,99,298],
#     ['정해온', 100,100,100,300],
#     ['나재민', 90,90,90,270, 90.00]
# ]

# # 좌표를 입력하고 값을 수정해서 변경하시오
# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list)
# stu_list[2][4] = 260
# print(stu_list)

# stu_list[2][4] = stu_list[2][1] + stu_list[2][2] + stu_list[2][3]
# stu_list[2][5] = stu_list[2][4]/3
# print(stu_list)


# 수정하고 싶은 학생번호를 입력하세요
# 국어점수를 변경하는 프로그램을 구현하시오.

# stu_list = [
#     ['이마크', 100,90,95,285,95.00],
#     ['정해온', 100,100,100,300,100.00],
#     ['나재민', 90,90,90,270, 90.00]
# ]
# print('''\
#     [ 수정할 학생 번호]
#     0, 이마크
#     1, 정해온
#     2, 나재민
#     '''
# )
# num = int(input("수정할 학생 번호를 입력하시오 >> "))
# # 1번 선택
# # 국어점수를 70점으로 변경하고, 합계, 평균을 변경해서 출력하시오.

# stu_list[1][1] = 70
# # stu_list[0][4] = stu_list[0][1] + stu_list[0][2] + stu_list[0][3]
# # stu_list[0][5] = stu_list[0][4]/3
# stu_list[1][4] = stu_list[1][1] + stu_list[1][2] + stu_list[1][3]
# stu_list[1][5] = stu_list[1][4]/3
# stu_list[2][4] = stu_list[2][1] + stu_list[2][2] + stu_list[2][3]
# stu_list[2][5] = stu_list[2][4]/3


# stu_list[1][1] = 70
# print(stu_list)



# stu_list = [
#     ['이마크', 100,90,95,285,95.00],
#     ['정해온', 100,100,100,300,100.00],
#     ['나재민', 90,90,90,270, 90.00]
# ]
# print("[학생성적수정]")
# print("0. 이마크")
# print("1. 정해온")
# print("2. 나재민")
# print("-"*50)

# # 수정할 대상 선정
# num = int(input("수정하려는 학생 번호를 입력하세요 >> "))
# print("[ {}학생 선택 ]".format(stu_list[num][0]))
# print("[ {}학생 국어점수 수정 ]".format(stu_list[num][0]))
# print("현재 국어점수 :", stu_list[num][1])

# # 국어점수입력
# score = int(input("수정할 국어점수를 입력하세요. >> "))
# print(score)
# stu_list[num][1] = score #국어점수 변경
# stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]
# stu_list[num][5] = stu_list[num][4]/3
# print(stu_list)

# # 영어점수입력
# num = int(input("수정하려는 학생 번호를 입력하세요 >> "))
# print("[ {}학생 영어점수 수정 ]".format(stu_list[num][0]))
# print("현재 영어점수 :", stu_list[num][2])

# score = int(input("수정할 국어점수를 입력하세요. >> "))
# print(score)
# stu_list[num][2] = score #영어점수 변경
# stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]
# stu_list[num][5] = stu_list[num][4]/3
# print(stu_list)

####################################################################################################
####################################################################################################




stu_list = [
    ['이마크', 100,90,95,285,95.00],
    ['정해온', 100,100,100,300,100.00],
    ['나재민', 90,90,90,270, 90.00]
]

title = ['이름', '국어', '영어', '수학', '합계', '평균']

while True:
    print("[학생성적수정]")
    print("0. 이마크")
    print("1. 정해온")
    print("2. 나재민")
    print("-"*50)

    # 수정할 대상 선정
    num = int(input("수정하려는 학생 번호를 입력하세요 >> "))
    print("[ {}학생 선택 ]".format(stu_list[num][0]))
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    print("-"*50)
    subject = int(input("수정할 과목을 선택하세요."))

    print("[ {} 학생 {}점수 수정 ]".format(stu_list[num][0], title[subject]))
    print("현재 {}점수 : {}".format(title[subject], stu_list[num][subject]))


    score = int(input("수정할 {}점수를 입력하세요. >> ". format(title[subject])))
    print(score)
    stu_list[num][subject] = score 
    stu_list[num][4] = stu_list[num][1] + stu_list[num][2] + stu_list[num][3]
    stu_list[num][5] = stu_list[num][4]/3
    print(stu_list)

