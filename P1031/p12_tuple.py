# 튜플 - 리스트와 동일하지만 수정은 불가함
a_list = [1,2,3,4,5]
a_tu= (1,2,3,4,5)
print(a_list)
print(a_tu)
print(a_list[2])
print(a_tu[2])
print(a_list)
a_tu = 100
a_tu[0] = 100 # 튜플은 수정 불가
print(a_tu)

del(a_list[0])
print(a_list)

# del(a_tu[0] # 튜플 삭제불가
# print(a_tu)