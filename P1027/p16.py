fruit = ['사과', '딸기', '망고']

# 해당하는 과일을 삭제하시오
ff = input("삭제할 과일을 입력하세요")
if ff in fruit:
    fruit.remove(ff)
else:
    print("해당하는 과일이 없습니다.")
    
print("과일종류 리스트 :", fruit)


ff = input("좋아하는 과일을 입력하세요.")
fruit.append(ff)
print("과일종류 리스트 :", fruit)

    
    
# str1 = "안녕하세요"
# if "하" in str1:
#     print("하라는 글자가 존재합니다.")
# else :
#     print("존재하지 않음.")
    

str2 = "안녕하세요, 반갑습니다. 저는 바다를 좋아합니다."
# 1개 글자를 입력받아, str2 변수에 존재하는지 확인하시오.
input5 = input("1개의 글자를 입력하세요")
if input5 in str2:
    print("입력한 문자 :", input5, "-> 존재함")
else :
    print("존재하지 않음.")