aa = [[1,[2,3],4],[5,6],[7,8,9]]
for i in aa:
    for j in i:
        print(j) # 2차원
print('-'*50)
aaa = [[[1,2],[3,4,5]],[[6],[7,8,9]]]
for i in aa:
    for j in i:
        if isinstance(j,list):
            print(j)
        else:
            for k in j:
                print(k)


