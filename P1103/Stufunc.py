def screen_print():
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

import random

stu_list = [
    [10101,'이재명', 100,90,95,285,95.00],
    [10102,'트럼프', 100,100,100,300,100.00],
    [10103,'김정은', 90,90,90,270, 90.00]
]
stu_count = 10104 #학생번호
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']




def stu_input():
    # 단순변수가 선언 되면 함수에서는 변수를 새롭게 생성
    global stu_count  # 전역변수
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
    
    
    
def stu_print():
    print("-"*50)
    print(" "*14, ">> 학생 성적 출력 <<")
    print("-"*50)
    print(" "*13, ">[ 학생 성적 리스트 ]<")
    print("-"*50)
    print()
    print(*title,sep="\t")
    print("-"*50)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t". format(*stus))
    print()