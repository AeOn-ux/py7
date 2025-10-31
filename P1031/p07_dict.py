english = {
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea'
}

# 영어맞추기 프로그램을 구현하시오
while True:
    count = 0
    for k, v in english.items():
        print("{}은/는 영어로 뭘까요?".format(k))
        answer = input(">> ")
        # answer == v
        
        # 정답확인
        if answer == v:
            print("딩동댕~")
            # 맞춘개수
            count = count + 1   # count += 1
            
        else:
            print("땡!!!!!!!!")
        
        #1:정답 2:오답 3:오답 4:정답 5:정답   
        print("정답 :",count)
            
        


# 20문제중에 랜덤으로 5문제를 뽑아서 만드시오.

