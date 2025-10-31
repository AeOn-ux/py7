# 학생 성적 프로그램
import random
stu_list = []
stu_count = 10101
title = ['학번','이름','국어','영어','수학','합계','평균']

while True:
    print("-"*50)
    print(" "*11, " [ 학생 성적 프로그램 ]")
    print("-"*50)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("0. 프로그램 종료")
    print("-"*50)
    print()
    
    choice = int(input("실행할 목록을 고르시오."))
    if choice == 1:
        print("-"*50)
        print(" "*14, ">> 학생 성적 입력 <<")
        print("-"*50)
        name = input("{}번 학생 이름을 입력하시오.".format(stu_count))
        kor = int(input("국어 성적을 입력하시오."))
        eng = int(input("영어 성적을 입력하시오."))
        math = int(input("수학 성적을 입력하시오."))
        total = kor + eng + math
        evg = total/3
        
        stu_list.append([stu_count, name, kor, eng, math, total, evg])
        stu_count = stu_count + 1
        print(">> 성적 입력이 완료되었습니다.")
        print()
        
    if choice == 2:
        print("-"*50)
        print(" "*14, ">> 학생 성적 출력 <<")
        print("-"*50)
        print(" "*13, ">[ 학생 성적 리스트 ]<")
        print("-"*50)
        print()
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t". format(*title))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t". format(*stus))
        print()
        
    if choice == 3:
        print("-"*50)
        print(" "*13, ">> 학생 성적 수정 <<")
        print("-"*50)
        print(" "*15, ">[ 학생 리스트 ]<")
        print("-"*50)
        
        for i, stus in enumerate(stu_list):
            print("{}, {} {}".format(i+1, stus[0], stus[1])) # <보기>
        print() 
        choice = int(input("수정을 진행할 학생을 선택하시오."))
        print("[{} 학생 수정 과목 선택]".format(stu_list[choice-1][1]))
        print("-"*50)
        print("1. 국어 성적 입력")
        print("2. 영어 성적 입력")
        print("3. 수학 성적 입력")
        print("-"*50)
        subject = int(input("수정을 진행할 과목을 선택하시오."))
        print()
        print("현재 {} 학생 {} 점수 : {}".\
            format(stu_list[choice-1][1], title[subject+1], \
                stu_list[choice-1][subject+1] ))
        print()
        
        # 점수 수정
        score = int(input("수정할 점수를 입력하시오."))
        pre_score = stu_list[choice-1][subject+1] # 현재점수 80
        stu_list[choice-1][subject+1] = score     # 변경점수 90
        # 합계 수정
        stu_list[choice-1][5] = \
            stu_list[choice-1][2] + stu_list[choice-1][3] + stu_list[choice-1][4]
        # 평균 수정
        stu_list[choice-1][6] = stu_list[choice-1][5]/3
        
        print("{} 점을 {} 점으로 수정이 완료되었습니다.".\
            format(pre_score,score))
        print ()
        print(stu_list)
        print()
    
    if choice == 4:
        for i, stus in enumerate(stu_list):
            print("{}, {} {}".format(i+1, stus[0], stus[1])) #<보기 입력>
        print("-"*50)
        
        choice = int(input("삭제할 번호를 선택하시오. "))
        flag = int(input("{} {} 학생이 맞으십니까? (1.Y/2.N)".\
            format(stu_list[choice-1][0], stu_list[choice-1][1])))
        if flag == 2:
            print("삭제가 취소 되었습니다.")
            continue
        del stu_list[choice-1]
        print("삭제가 완료 되었습니다.")
        print()
        
    elif choice == 0:
        print("^"*50)
        print("^"*50)
        print(" "*13, "프로그램을 종료합니다.")
        print()
        break
    
    