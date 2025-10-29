# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list)
# b_list = list(range(1,10))
# print(b_list)
# c_list = [i for i in range(1,11)]
# print(c_list)

# d_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
# print(d_list)
# e_list = list('0'*9)
# print(e_list)
# f_list = ['0' for i in range(9)]
# print(f_list)



################################
## 연습
################################


# a_list = list(range(1,10))
# print(a_list)
# # for i in a_list:
# #     print(i,end="1") # end는 옆으로 출력
    
# for i in a_list:
#     print(i,end="\t")
#     if i%3 ==0:
#         print()
        
# print()
# print("-"*50)


# a_list = list(range(1,17))
# for i in a_list:
#     print(i,end="\t")
#     if i%4 ==0:
#         print()
# print()        
# print("-"*50)


# a_list = list(range(1,26))  
# for i in a_list:
#     print(i,end="\t")
#     if i%5 ==0:
#         print()
        
        
        
        
        
# print(a_list[0])
# b_list = [1,2,3]
# print(b_list[0])       

a_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# #[ [1,2,3], [4,5,6], [7,8,9] ]
# # 3*3 형태로 출력하시오.
for aa in a_list: #  [1,2,3]     [4,5,6] [7,8,9]
    for a in aa: # [1,2,3]
        print(a,end="\t")
    print()
        
        
        
a_list = [9,1,2,5,6,8,3,4,7]
for i,val in enumerate(a_list):
    print(val,end="\t")
    if (i+1)%3 == 0 :
        print()
        
        
import random
a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)
for i,val in enumerate(a_list):  # (0,9),(1,1),(2,2),(3,5)
    print(val,end="\t")
    if (i+1)%4 == 0 :
        print()