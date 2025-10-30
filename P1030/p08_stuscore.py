# 학생 성적 프로그램
import random

stu_list = [
    [10101,'이재명', 100,90,95,285,95.00],
    [10102,'트럼프', 100,100,100,300,100.00],
    [10103,'김정은', 90,90,90,270, 90.00]
]
stu_count = 10101 #학생번호
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']


while True:
    print("-"*50)
    print(" "*10, "[ 학생 성적 프로그램 ]")
    print("-"*50)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("0. 프로그램 종료")
    print("-"*50)
    choice = int(input("실행하실 번호를 입력하시오 >> "))
    
    
    if choice == 1: #1. 학생 성적 입력
        print()
        print("-"*50)
        print('> 학생성적입력 <')
        name = input("{}번 학생 이름을 입력하시오. >> ".format(stu_count))
        #10101번 학생 이름을 입력하시오. >>
        
        kor = int(input("국어 점수를 입력하시오."))
        eng = int(input("영어 점수를 입력하시오."))
        math = int(input("수학 점수를 입력하시오."))
        total = kor+eng+math
        avg = total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count = stu_count + 1 # 학생번호 1 증가
        print("> ! 성적 입력이 완료되었습니다.")
        print()
        
    elif choice == 2: #학생성적출력
        print()
        print("-"*50)
        print(" "*10, "[ 학생 성적 리스트 ]")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*stus))
        print()
        
    elif choice == 3: #3. 학생 성적 수정
        print()
        print("-"*50)
        print(" "*10, "[ 학생 성적 수정 ]")
        print("-"*50)
        for stus in stu_list:
            print("{}. {}".format(stus[0],stus[1]))
        print("-"*50)
        for i, stus in enumerate(stu_list):
            print("{}. {} {}".format(i+1, stus[0], stus[1]))
        print("-"*50)
        print()
        choice = int(input(" 수정하실 번호를 입력하시오. >> "))
        print("-"*50)
        print(" [ {} 학생 수정 과목 선택 ]".format(stu_list[choice-1][1]))
        print("1. 국어 성적 수정")
        print("2. 영어 성적 수정")
        print("3. 수학 성적 수정")
        print("-"*50)
        print()
        print("-> 점수 수정 ")
        subject = int(input("점수 수정을 위한 과목을 선택하시오."))
        # print("[ {} 학생 {} 점수 수정 ]".\
        #     format((stu_list[choice-1][1]), (title[subject+1])))
        print("현재 {} 점수 : {}".\
            format(title[subject+1], stu_list[choice-1][subject+1]))
        # 현재 {[(3+1)] : (0학번,1이름,2국,3영,4수,5합,6통)에서 수학의 데이터번호는 4} 
        # 점수 :{[(3-1):(0이재명,1트럼프,2김정은)에서 3번째 김정은의 데이터 번호는 2], 
        #                              [김정은의 데이터에서 수학의 데이터 번호는 4] = n점}
        print()
        
        # 점수 수정
        score = int(input("수정할 점수를 입력하세요."))
        stu_list[choice-1][subject+1] = score
        # 내가 입력한 '수정할 점수'를 기존에 있던 n점 자리에 넣는다.
    
        # 합계 수정
        stu_list[choice-1][5] = \
            stu_list[choice-1][2] + stu_list[choice-1][3] + stu_list[choice-1][4]
        # 평균 수정
        stu_list[choice-1][6] = stu_list[choice-1][5]/3
        print("{} 점수를 {}점으로 수정이 완료되었습니다.".\
                format(title[subject+1],score))
        print()
        print(stu_list)
        print("-"*50)
        print()
    
    elif choice == 4: #4. 학생 성적 삭제
        for i, stus in enumerate(stu_list):
            print("{}. {} {}".format(i+1, stus[0], stus[1]))
        print("-"*50)
        choice = int(input(" 삭제하실 번호를 입력하세요. >> "))
        flag = int(input("{} {} 학생이 맞습니까? (1:Yes/2:No) ".\
            format(stu_list[choice-1][0], stu_list[choice-1][1])))
        if flag == 2:
            print("삭제가 취소 되었습니다.")
            continue
        #삭제부분
        del stu_list[choice-1]
        print("삭제가 완료되었습니다. ")
        print()
    
    
    elif choice == 0:
        print("-"*50)
        print("^"*50)
        print(" "*9, "[ 프로그램을 종료합니다. ]")
        print()
        break



