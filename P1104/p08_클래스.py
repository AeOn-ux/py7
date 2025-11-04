# 클래스가 2개 있음
# student 클래스, Stuscore 클래스

from S_func import *

# s1 = Student(10101,'홍길동',80,80,80)   
# s2 = Student(10102,'유관순',90,90,90)
# s3 = Student(10103,'이순신',100,100,100)
    
# 학생 성적 저장
students = Stuscore() # 객체선언
students.add(Student(10101,'홍길동',80,80,80))
students.add(Student(10102,'유관순',90,90,90))
students.add(Student(10103,'이순신',100,100,100))

students.print()