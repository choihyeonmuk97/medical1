a_list = [
    1,2,[3,4],5,[6,7,8,9],[10,11]
]
# 1,2,3,4,5,6,7,8,9,10,11 로 풀어서 출력

aa_list = []
for a in a_list:
    if type(a) == list:
        for i in a:
            aa_list.append(i)
            print(i,end=' ')
    else:
        aa_list.append(a)
        print(a,end=' ')
print()
print('-'*50)
print(aa_list)