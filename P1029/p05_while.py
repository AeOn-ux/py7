# stu_list = []
# # ['홍길동', 100,90,80,270,90.00]
# name = input("이름을 입력하세요.")
# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# print("이름 : {}".format(name))
# print("국어 : {}".format(kor))
# print("영어 : {}".format(kor))
# print("수학 : {}".format(kor))
# print("합계 : {}".format(kor))
# print("평균 : {}".format(kor))

# print("{}, {}, {}, {}, {}, {:.2f}".format(name,kor,eng,math,total,avg))



# # append 를 이용하시오
# name = input("이름을 입력하세요.")
# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# stu_list = []
# stu_list.append(name)
# stu_list.append(kor)
# stu_list.append(eng)
# stu_list.append(math)
# stu_list.append(total)
# stu_list.append(avg)
# # 위는 너무 길기 때문에, 코드를 줄이려면,\
#     #stu_list = [name,kor,eng,math,total,avg]
# print("이름 : {}".format(stu_list[0]))
# print("이름 : {}".format(stu_list[1]))
# print("이름 : {}".format(stu_list[2]))
# print("이름 : {}".format(stu_list[3]))
# print("이름 : {}".format(stu_list[4]))
# print("이름 : {}".format(stu_list[5]))
# print("{}, {}, {}, {}, {}, {:.2f}".format(stu_list[0],stu_list[1],stu_list[2],stu_list[3],stu_list[4],stu_list[5]))



stu_list = []
while True:
    print("[ 학생성적입력 ]")
    name = input("이름을 입력하세요.")
    kor = int(input("국어점수를 입력하세요."))
    eng = int(input("영어점수를 입력하세요."))
    math = int(input("수학점수를 입력하세요."))
    total = kor+eng+math
    avg = total/3
    # stu_list.append(name)
    # stu_list.append(kor)
    # stu_list.append(eng)
    # stu_list.append(math)
    # stu_list.append(total)
    # stu_list.append(avg)
    # 위는 너무 길기 때문에, 코드를 줄이려면,\
        #stu_list = [name,kor,eng,math,total,avg]
    stu_list.append([name,kor,eng,math,total,avg])
    # print("이름 : {}".format(stu_list[0][0]))
    # print("이름 : {}".format(stu_list[0][1]))
    # print("이름 : {}".format(stu_list[0][2]))
    # print("이름 : {}".format(stu_list[0][3]))
    # print("이름 : {}".format(stu_list[0][4]))
    # print("이름 : {}".format(stu_list[0][5]))
    print("{}, {}, {}, {}, {}, {:.2f}".format(name,kor,eng,math,total,avg))
    if stu_list == 0:
        break
    elif stu_list== 1 :
        # 학생성적입력
        print("[ 학생 성적 입력 ]")
print()
print(stu_list)