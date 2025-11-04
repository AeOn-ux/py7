# 람다식 함수 - 함수 축약 / 변수 = lambda 매개변수 : 수식
# map 함수 - 여러개를 함수 적용시킬 때 사용 리스트 = map(함수, 리스트)
my_list = [1,2,3,4,5]
m_list = list(map(lambda a:"{}원".format(a*1425),my_list))
print(m_list)
m_list = list(map(lambda a:a*10, my_list))
print(m_list)

my_list = ['1','2','3','4','5']
m_list = list(map(lambda a:int(a), my_list))
print(m_list)