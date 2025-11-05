
# print("안녕하세요. \"바다\"입니다.") # 따옴표를 중복으로 사용할 때 역슬레시를 사용하면 문자로 인식하겠다는 의미



# f = open("c:/down/aaa.txt", "r", encoding="utf8")

# while True:
#     txt = f.readline()
    
#     if txt == "" : break
#     print(txt.strip()) # 공백제거
#     # print(txt, end="") #(enter키)공백이 존재
    
# f.close()



# txt = f.readline()
# print(txt.strip()) # 문자열타입 = strip : 공백제거
# print(txt.strip().split(",")) # 리스트타입 - strip : 공백제거, split(): 분리
# print(txt.strip().split(",")[5]) # 합계
# f.close()



a_list = []
f2 = open("c:/down/bbb.txt", "r", encoding="utf8")

while True:
    txt = f2.readline()
    if txt == "" : break
    a_list.append(txt.strip().split(","))
   
f2.close()

print(a_list)