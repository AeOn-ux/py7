# print("%d" % (100, 200)) 에러. %개수와 뒤의 개수가 맞아야 한다.
# print ("%d, %d" % (100, 200)) 옳은 표식.


str1 = "이름"
str2 = "국어"
str3 = "영어"
str4 = "수학"
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
print(str1, str2, str3, str4)
print("%s, %s, %s, %s" % (str1, str2, str3, str4))
# \t 탭키적용, \n 줄바꿈
print("%s" % (name))
print("%s\t%d" % (name, kor))