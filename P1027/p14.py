num = int(input("숫자를 입력하세요."))
print("입력한 숫자 :", num)

# 0보다 큰 수 입니다. 0보다 작은 수 입니다.
if num>0:
    print("0보다 큰 수 입니다.")
if num ==0:
    print("0입니다.")
if num <0:
    print("0보다 작은 수 입니다.")
    
if num>=0:
    print("0보다 큰 수 입니다.")
elif num ==0:
    print("0입니다.")
else:
    print("0보다 작은 수 입니다.")
    
    
    
# 70점 이상 통과, 60점 이상은 재시험, 60점 미만은 낙제
score = 70

if score >= 70:
    print("통과")
elif score >=60:
    print("재시험")
else:
    print("낙제")
    
    
# 90점 이상은 A, 80점 이상은 B, 70점 이상은 C, 60점 이상은 D, 60점 미만은 F
score = int(input("점수를 입력하세요."))

if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
    
result = "합격" if score>=60 else result="불합격"