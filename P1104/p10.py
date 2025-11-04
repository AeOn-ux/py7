class Student:
    def __init__(self, stuno, name, kor, eng, math):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank =0
        
    # 합계
    def total_f(self):
        self.total = self.kor+self.eng+self.math
        
    # 평균
    def avg_f(self):
        self.avg = self.total/3
            
            
s = Student(10101,'홍길동',80,80,80)
print("국어 :", s.kor)
print("합계 : ",s.total)
s.kor = 100
print("국어 :", s.kor)
s.total_f()
s.avg_f()
print("합계 : ",s.total)
print("평균 : ",s.avg)