##

stu_list = [
    ['이재명', 100,90,95,285,95.00],
    ['트럼프', 100,100,100,300,100.00],
    ['김정은', 90,90,90,270, 90.00]
]

title = ['이름', '국어', '영어', '수학', '합계', '평균']

# 각 학생의 이름을 출력해보시오.
# 이재명
print(stu_list[0][0])
# 트럼프
print(stu_list[1][0])
# 김정은
print(stu_list[2][0])

for i in range(3):
    print(stu_list[i][0])
    
for stus in stu_list:
    print(stus[0])
    
# 국어점수까지 출력하시오.
for stus in stu_list:
    print(stus[0], stus[1])

for stus in stu_list:
    print("{}\t{}".format(stus[0], stus[1]))
    
# 0. 이재명
# 1. 트럼프
# 2. 김정은
while True:
    print("-"*50)
    print(" "*10, "[ 학생성적 삭제 리스트 ]")
    print("-"*50)
    for i, stus in enumerate(stu_list):
        print("{}, {}".format(i+1, *stus))
    print("-"*50)
    num = int(input(" 삭제하려는 번호를 입력하세요 >> "))

    # 1. 이재명
    # 2. 트럼프
    # 0. 김정은
    # 1-0
    del stu_list[num-1]
    print(stu_list)
