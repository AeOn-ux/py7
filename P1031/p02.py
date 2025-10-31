a = 10
aa = a
b = [1,2,3,4]
bbb =b # 얕은 복사 - 주소값복사
bb = b[:] # 깊은 복사 - 값복사 = # bb[1,2,3,4]
bb[0] = 20
print(a) # 10
print(b) # [1,2,3,4]

stu_list = [
    # 이름, 합계, 등수
    ['홍길동',288,0],
    ['유관순',299,0],
    ['이순신',300,0],
    ['김구',295,0],
    ['강감찬',298,0]
]

r_count = 1 # 등수카운트
for i in stu_list:
    r_count = 1
    for j in stu_list:
        if i[1] < j[1] :
            r_count = r_count + 1
    # 비교가 완료되는 시점
    i[2] = r_count
    
print(stu_list)