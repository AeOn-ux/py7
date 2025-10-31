# 세트 : 키만 있음. 키 중복 불가 = 중복 제거할 때 사용
set1 = {1,1,2,3,4,2,5,4,4,4,1}
print(set(set1))

a_list = [1,2,3,1,1,2,6,7,3]
print(set(a_list))

names = ['홍길동','유관순','이순신','홍길동','홍길동','유관순']
print(set(names))
nset = set(names) # 변수 저장
print(nset)