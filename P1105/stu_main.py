
# stu_list = [
#     {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
#         'total':240,'avg':80.00,'rank':0},
#     {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
#         'total':270,'avg':90.00,'rank':0},
#     {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
#         'total':300,'avg':100.00,'rank':0},
# ]



# 파일 읽어오기


stu_list = []
f = open("c:/down/aaa.txt","r")
while True:
    txt = f.readline()
    if txt == "": break
    t_list = txt.strip().split(",") # 문자열을 딕셔너리 타입으로 변경명령어
    print(t_list)
    # 딕셔너리 형태 변경
    t_dic = {'stuno':int(t_list[0]), 'name':t_list[1], 'kor':int(t_list[2]),\
        'eng':int(t_list[3]), 'math':int(t_list[4]), 'total':int(t_list[5]), \
            'avg':float(t_list[6]), 'rank':int(t_list[7])}
    stu_list.append(t_dic)

print(stu_list)

# t_dic = ast.:eiiter_eval(tx)




# 파일 -> 리스트[딕셔너리타입] -> 파일
f = open("c:/down/aaa.txt","w", encoding="utf8")
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},{stu_list[i]['eng']},\
{stu_list[i]['math']},{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"




f = open("c:/down/aaa.txt","w", encoding="utf8")
f.write(stu_str)
f.close()