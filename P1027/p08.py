# 국어, 영어, 수학 점사를 입력 받아 합계와 평균을 출력하시오/
# kor = int(input("국어점수를 입력하세요")) 
# eng = int(input("영어점수를 입력하세요"))
# math = int(input("수학점수를 입력하세요"))
# print("%s + %s + %s = %d" % (kor, eng, math, (kor+eng+math)))
# print("(%d)/3 = %f" % (kor+eng+math), ((kor+eng+math)/3))



# print("합계 : %d" % (kor+eng+math))
# print("평균 : %f" % ((kor+eng+math)/3))
# print("평균 : %.2f" % ((kor+eng+math)/3))



name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요")) 
eng = int(input("영어점수를 입력하세요"))
math = int(input("수학점수를 입력하세요"))


# name2 = input("이름을 입력하세요")
# kor2 = int(input("국어점수를 입력하세요")) 
# eng2 = int(input("영어점수를 입력하세요"))
# math2 = int(input("수학점수를 입력하세요"))

# name3 = input("이름을 입력하세요")
# kor3 = int(input("국어점수를 입력하세요")) 
# eng3 = int(input("영어점수를 입력하세요"))
# math3 = int(input("수학점수를 입력하세요"))


print("안녕\t하\n세요")
print(" "*20+"학생성적프로그램")
print(" "*10)
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)

# print("%s\t%d\t%d\t%d\t" % (name, kor, eng, math))
# print("%s\t%d\t%d\t%d\t%d\t" % (name, kor, eng, math,(kor+eng+math) ))
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name, kor, eng, math,(kor+eng+math), ((kor+eng+math)/3)))
# print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name2, kor2, eng2, math2,(kor2+eng2+math2), ((kor2+eng2+math2)/3)))
# print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name3, kor3, eng3, math3,(kor3+eng3+math3), ((kor3+eng3+math3)/3)))