a_list = [1,2,3]
# list추가 - append, insert, extend
# append - 제일 뒤에 추가
# 복합변수의 값이 변경이 됨
a_list.append(10)
print(a_list)

# insert - (위치, 값)을 추가
a_list.insert(1, 200)
print(a_list)

a2_list = [5,6,7]
a_list.extend(a2_list) # 리스트 2개를 합침
print(a_list)

a_list = a_list + [10,20,30]
print(a_list)

# list 값 변경 - 위치값을 입력하면 변경됨
a_list[2] = 1000
print(a_list)

# 삭제 - pop()-제일 뒤에삭제, del(해당위치삭제), remove(해당값 삭제), clear - 모두 삭제
aa_list = [1,2,3,4,5,6,7]
aa_list.pop()
print(aa_list)
del aa_list[0]
print(aa_list)
aa_list.remove(5)
print(aa_list)
aa_list.clear()
print(aa_list)

# [] 1개 : 1차원 리스트
# [[]] 2개 : 2차원 리스트
# [[[]]] 3개 : 3차원 리스트
