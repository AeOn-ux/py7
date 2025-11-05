
#----------------------------------------------------------------------

# # r : 읽기 모드

# import os

# # 1. 통로(stream) : 파일 열기
# # r : 읽기모드, W : 쓰기모드, a : 추가모드
# f = open("C:/down/aaa.txt", "r", encoding="utf8")
# # euc-kr : 국내표준, utf-8(=utf8) : 국제표준




# while True:
#     txt = f.read()
#     if txt == "":break
#     print(txt, end="")

# # while True:
# #     txt = f.readline()  # read()-한글자씩:속도느림,  readline()-한문장씩, readlines()-전체
# #     if txt == "" : break
# #     print(txt,end="") # print 완료 후 줄바꿈을 해줌
    

# # readlines() : 전체 가져오기    
# # txt_list = f.readlines() # 1줄씩 리스트에 담아서 가져옴
# # for txt in txt_list:
# #     print(txt, end="")
    
    
# f.close()



#----------------------------------------------------------------------

# w : 쓰기 모드 - 안에 있는 모든 것 지우고 쓰기
# a : 추가 모드 - (안에 있는 것 그대로 두고) 마지막에 쓰기
# f = open("c:/down/ccc.txt","w")  # 파일이 없으면 W:모드는 파일을 생성
# stu_data = ""
# for i in range(1):
#     txt = input("글자를 입력하세요.>> \n")
#     stu_data += txt + "\n"
    
# f.write(stu_data)
# f.close()
# print("완료!")




#----------------------------------------------------------------------


# # a : 추가 모드 - (안에 있는 것 그대로 두고) 마지막에 쓰기
# f = open("c:/down/ccc.txt","a")  # a : 모드
# for i in range(5):
#     f.write(f"안녕하세요. {i} \n")
    
# f.close()
# print("완료!!")




#----------------------------------------------------------------------

# # with open() 파일입출력
# with open("c:/down/bbb.txt","r",encoding="utf-8") as f:
#     while True:
#         txt = f.readline()
#         if txt == "":break
#         print(txt.strip())
# # f.close() # 위 경우에만 생략 가능해도 출력됨.
        
        

# f = open("c:/down/aaa.txt", "r", encoding="utf-8")
# while True:
#     txt = f.readline()
#     if txt == "":break
#     print(txt.strip())
# f.close()


#----------------------------------------------------------------------

# 파일 복사
# 파일 읽기:rb. 파일 쓰기:wb
f = open("c:/down/마크.jpg","rb")
f2 = open("c:/aaa/마크.jpg","wb")

while True:
    markfile = f.read(1) # read():파일읽기, # readline, readlines(): 문자읽기
    if not markfile : break
    f2.write(markfile)
    
f.close()
f2.close()
print("복사완료!!")






