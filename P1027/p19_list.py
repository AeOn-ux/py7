# 이름, 국어, 영어, 수학, 합계, 평균
# 3명의 학생의 이름을 입력 받아 성적을 저장해서 출력하시오

# stus = []
# stus.append(['이마크', 100, 100, 100, 300, 100.0])

stu_data = []
stu_datas = []
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하시오."))
eng = int(input("영어점수를 입력하시오."))
math = int(input("수학점수를 입력하시오."))
total = kor+eng+math
avg = total/3
stu_data = [name, kor, eng, math, total, avg]


name1 = input("이름을 입력하세요.")
kor1 = int(input("국어점수를 입력하시오."))
eng1 = int(input("영어점수를 입력하시오."))
math1 = int(input("수학점수를 입력하시오."))
total1 = kor+eng+math
avg1 = total/3
stu_data1 = [name1, kor1, eng1, math1, total1, avg1]

name2 = input("이름을 입력하세요.")
kor2 = int(input("국어점수를 입력하시오."))
eng2 = int(input("영어점수를 입력하시오."))
math2 = int(input("수학점수를 입력하시오."))
total2 = kor+eng+math
avg2 = total/3
stu_data2 = [name2, kor2, eng2, math2, total2, avg2]

stu_datas = []
# stu_datas.append(stu_data, stu_data1, stu_data2)
stu_datas.append(stu_data)
stu_datas.append(stu_data1)
stu_datas.append(stu_data2)
print(stu_datas)



