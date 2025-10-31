# a_list = [1,1,2,3,4,2,3,1,5,4]
# a_dic = {}
# # 1: 2:
# # 딕셔너리에 저장하시오

# print(a_dic.keys())
# print(list(a_dic.keys()))

# for i in a_list:
#     a_dic[1] = 1
#     a_dic[2] = 1
#     a_dic[3] = 1
#     a_dic[1] = 2
    
#     # {1:2, 2:1, 3:1}

# b_dic = {}
# # 없는 키 입력 시 추가
# b_dic['홍길동'] = 100
# # 있는 키 입력 시 수정
# b_dic['홍길동'] = 50





# a_list = [1,1,2,3,4,2,3,1,5,4]
# # a_dic = {}
# # a_dic[1] = 1
# # a_dic[2] = 1
# # a_dic[3] = 1
# # a_dic[1] = 2
# # print(a_dic)


# a_list = [1,1,2,3,4,2,3,1,5,4]
# a_dic = {}
# a_dic['홍길동'] = 100
# print(a_dic)
# # {'홍길동' : 100}

# b_dic = {}
# b_dic[1] = 1
# b_dic[2] = 1
# b_dic[1] = 10
# print(b_dic)
# # {1:10. 2:1}



a_list = [1,1,2,3,4,2,3,1,5,4]
a_dic = {}
for i in a_list:
    if i not in a_dic:
       a_dic[i] = 1
    else:
        a_dic[i] += 1
    
print(a_dic)
# {1:3, 2:2, 3:2, 4:2, 5:1ss}