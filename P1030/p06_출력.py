##

stu_list = [
    ['이마크', 100,90,95,285,95.00],
    ['정해온', 100,100,100,300,100.00],
    ['나재민', 90,90,90,270, 90.00]
]

title = ['이름', '국어', '영어', '수학', '합계', '평균']

print("-"*50)
print(" " * 15, "[ 학생 성적 프로그램 ]" )
print("-"*50)
print("1. 학생성적입력 ")
print("2. 학생성적출력 ")
print("-"*50)
choice = int(input("원하는 번호를 입력하세요 >> "))
print()

# 학생 성적 출력
print(" "*15, "[ 학생 성적 리스트 ]")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
print("-"*50)
for stus in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))