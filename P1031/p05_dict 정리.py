# {키:값}
stu_dic = {'no':1, 'name':'홍길동', 'kor' : 100}


#dict 추가
stu_dic['eng'] = 90
print(stu_dic)
# dict 수정
stu_dic['kor'] = 10
print(stu_dic)
#dict 수정
# dict 삭제
del stu_dic ['name']
print("-"*50)

# key 출력 : 키
print(stu_dic.keys())
print(list(stu_dic.keys()))
for k in stu_dic.keys():
    print("{}:{}".format(k,stu_dic[k]))
print("-"*50)

# values() 출력 : 값
print(stu_dic.values())
print(list(stu_dic.values()))
for i, v in enumerate(stu_dic.values()):
    print("{}, {}".format(i,v))
print("-"*50)

# items() 출력 - k,v
print(stu_dic.items()) # 튜플형태로 출력
print(list(stu_dic.items()))
for k, v in stu_dic.items():
    print("{}:{}".format(k,v))
print("-"*50)

# 딕셔너리 출력
print(stu_dic['no'])

print(stu_dic['name'])
print(stu_dic['kor'])
# print(stu_dic['math']) # 없는 key를 출력 시 에러 발생

print(stu_dic.get('kor'))
print(stu_dic.get('math')) # 없는 key를 출력 시 실행됨.
print("-"*50)


# # 어려우니까 넘어가라고 하심
# # 딕셔너리 정렬 : sorted
# import operator
# names = {"홍길동":100, "유관순":80, "이순신":90, "김구":99, "강감찬":95}
# names2 = sorted(names.items(),key=operator.itemgetter(0))

# reverse = True : 역순정렬, reverse=False : 순차정렬
# itemgetter(0):키, itemgetter(1): 값
# names2 = sorted(names.items(),key=operator.itemgetter(0))
# print(names)
# print(names2)
# print("-"*50)


# 리스트 정렬
a_list = [1,5,9,4,3]
# sort() -> 해당리스트 자체를 정렬, 원본 변경
a_list.sort()
a_list.reverse() # 1,2,3,4,5 -> 5,4,3,2,1 처럼 순서가 변경
# sorted() -> 다른 변수에 저장 가능, 원본은 변경 불가
b_list = sorted(a_list)
b_list = sorted(a_list,reverse=True)
#reverse = True : 역순정렬
print(a_list)
print(b_list)

# 리스트 최대값 - max : 리스트에서 최대값 출력
print(max(a_list))
print(min(a_list))