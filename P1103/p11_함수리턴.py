# return : 함수호출로 값을 전달할때 사용

def cal(a,b):
    return a+b # 함수호출로 값을 전달

sum = cal(1,2) # 함수호출

def func(a,b):
    a+b
    return # return 값이 없으면 함수종료

def big(a,b):
    c=0
    if a>b :
        c = a
    else :
        c = -1
        
    return c


def big(a,b):  # 위와 같은 식
    c=0
    if a>b :
        return a
    else :
        return -1