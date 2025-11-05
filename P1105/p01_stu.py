

# stu_list = [
#     [10101,'홍길동',80,80,80,240,80.00,0],
#     [10102,'유관순',90,90,90,280,90.00,0],
#     [10103,'이순신',100,100,100,300,100.00,0]
# ]

# print(stu_list[1][1])


# stu_list = [
#     {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
#         'total':240,'avg':80.00,'rank':0},
#     {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
#         'total':270,'avg':90.00,'rank':0},
#     {'stuno':10102,'name':'이순신','kor':100,'eng':100,'math':100,\
#         'total':300,'avg':100.00,'rank':0},
# ]



# stu_str = f"{stu_list[0]['stuno']},{stu_list[0]['name']},{stu_list[0]['kor']},{stu_list[0]['eng']},\
# {stu_list[0]['math']},{stu_list[0]['total']},{stu_list[0]['avg']},{stu_list[0]['rank']}"

# print(stu_str)





# # print(stu_list[1]['name'])

# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\
# \t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']}\t{stu['rank']}\t")




# ----------------------------------------------------------------------이미 있는 데이터 .txt로 이동

stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
]



stu_str = f"{stu_list[0]['stuno']},{stu_list[0]['name']},{stu_list[0]['kor']},{stu_list[0]['eng']},\
{stu_list[0]['math']},{stu_list[0]['total']},{stu_list[0]['avg']},{stu_list[0]['rank']}\n"
stu_st1 = f"{stu_list[1]['stuno']},{stu_list[1]['name']},{stu_list[1]['kor']},{stu_list[1]['eng']},\
{stu_list[1]['math']},{stu_list[1]['total']},{stu_list[1]['avg']},{stu_list[1]['rank']}\n"
stu_str2 = f"{stu_list[2]['stuno']},{stu_list[2]['name']},{stu_list[2]['kor']},{stu_list[2]['eng']},\
{stu_list[2]['math']},{stu_list[2]['total']},{stu_list[2]['avg']},{stu_list[2]['rank']}\n"

print(stu_str)



# dict 타입 -> 문자열로 변환
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},{stu_list[i]['eng']},\
{stu_list[i]['math']},{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"
    stu_str +=  "\n"

print(stu_str)

f = open("c:/down/aaa.txt","w")
f.write(stu_str)
f.close()
print("완료!")
















