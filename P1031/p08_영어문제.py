import random

english = {
    '바다':'ocean',
    '하늘':'sky',
    '비':'rain',
    '사랑':'love',
    '이름':'name',
    '운명':'destiny',
    '문제':'problem',
    '소년':'boy',
    '소녀':'girl',
    '열쇠':'key',
    '물':'water',
    '지구':'earth',
    '공기':'air',
    '운':'luck',
    '차':'tea',
    '커피':'coffee',
    '포옹':'hug',
    '눈':'snow',
    '먼지':'dirt',
    '물':'water'
        }

a_list = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]
quest = random.sample(a_list, 6) # 랜덤 5개 - 20문제 중 5개를 추출
quest.sort()    # 정답, 오답 입력을 위한 저장공간
quest_dic = {}  # 랜덤 5개 - 순서대로 정렬
print(quest)

num = 1 # 문제번호
for i, k in enumerate(english.keys()): #index를 함께 추출, key
    if i in quest:
    #    print(i,k,english[k])
         count = 0
         
         # 정답 입력
         print("{} 은(는) 영어로 뭘까요". format(k))
         answer = input(">> ")
         
         # 정답 확인
         if answer == english[k]:
             print("~딩동댕~")
             count = count +1
             quest_dic[num] = '정답'
        
         else:
            print("땡!!! 정답 :", english[k])
            quest_dic[num] = '오답'
    num = num + 1   
            
print(quest_dic)            
print("정답 :", count)