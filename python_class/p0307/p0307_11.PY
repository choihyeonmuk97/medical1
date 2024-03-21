# list = [[1,2,3],[4,5,6],[7,8,9]]

# 1차원 리스트에 1~9까지 숫자 입력
list =[]
for i in range(9):
    list.append(i+1)
print(list)

list2 =[n+1 for n in range(9)] # 컴프리헨션
print(list2)

list3 = [[0]*3 for n in range(3)]
for i in list3:
    pass    

numList =[num*num for num in range(1,6)]


# 1~9까지 2차원 리스트
# [[1,2,3],[4,5,6],[7,8,9]] 처럼 출력
# a_lists = []
# for i in range(3):
#     a_list = []
#     for j in range(3):
#         a_list.append((3*i)+j+1)
#     a_lists.append(a_list)

# print(a_lists)
        
    




# for i in list:
#     for f in i:
#         print(f,end='\t')
#     print()