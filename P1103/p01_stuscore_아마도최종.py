import random
stu_list = []
stu_count = 10101
title = ['학번','이름','국어','영어','수학','합계','평균']

stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]

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
    
    
    # 학생 입력 부분
    choice = int(input("실행할 목록을 고르시오."))
    if choice == 1:
        print("-"*50)
        print(" "*14, ">> 학생 성적 입력 <<")
        print("-"*50)
        name = input("{} 학생 이름을 입력하시오.".format(stu_count))
        kor = int(input("국어 성적을 입력하시오."))
        eng = int(input("영어 성적을 입력하시오."))
        math = int(input("수학 성적을 입력하시오.")) 
        total = kor+eng+math
        evg = total/3
        
        stu_list. append([stu_count, name, kor, eng, math, total, evg])
        stu_count = stu_count + 1
        print(">> 성적 입력이 완료되었습니다. ")
        print()
        
        
    # 학생 출력 부분
    if choice == 2 :
        print("-"*50)
        print(" "*14, ">> 학생 성적 입력 <<")
        print("-"*50)
        print(" "*13, ">{ 학생 성적 리스트 }<")
        print("-"*50)
        print()
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))
        print()
        





