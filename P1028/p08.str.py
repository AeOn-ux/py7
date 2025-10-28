# 교재 45p~ 참고
a = "안녕"
b = '안녕'
print(type(a))

# n_list.sort() # 순차정렬 - 낮은 값부터 정렬
# n_list.reverse 정렬이 아닌 순서를 역순으로 출력
# n_list.sort(reverse=True) 역순정렬 -  높은 값부터 정렬

# tuple 수식은 수정 불가. 읽어오기만 가능

# 조건문에 pass를 넣으면 아무 일도 일어나지 않음


score = 99
hak = ""
if score>=99:
    print("A+")
if score>=90:
    hak = "A"
    if score>=99:
        hak = hak + "+"
    elif score<93:
        hak = hak + "-"
if score>=80:
    hak = "B"
    if score>=99:
        hak = hak + "+"
    elif score<93:
        hak = hak + "-"
print(hak)

# 값에 10을 곱하여 순차적으로 출력하시오
a_list = [1,2,3,4,5]
for i in a_list:
    print(i*10)
    
a_list = [3,5,9,10,2]
aa_list = []
for i in a_list : 
    aa_list.append(i*10)


# bb_list = [1,2,3,4,5,6~100]
# bb_list = list(range(100))