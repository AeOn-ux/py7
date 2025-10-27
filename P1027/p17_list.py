stu_data = []
stu_data.append("이민형")
stu_data.append("나재민")
stu_data.append("이장현")
stu_data.append("오세훈")
print(stu_data)
# -> ['이민형', '나재민', '이장현', '오세훈']

stu_datas = []

name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하시오."))
eng = int(input("영어점수를 입력하시오."))
math = int(input("수학점수를 입력하시오."))
total = kor+eng+math
avg = total/3
stu_data = [name, kor, eng, math, total, avg]
stu_datas.append(stu_data)

name2 = input("이름을 입력하세요.")
kor2 = int(input("국어점수를 입력하시오."))
eng2 = int(input("영어점수를 입력하시오."))
math2 = int(input("수학점수를 입력하시오."))
total2 = kor+eng+math
avg2 = total/3
stu_data2 = [name2, kor2, eng2, math2, total2, avg2]
stu_datas.append(stu_data2)


print("-"*50)
print(stu_datas)
