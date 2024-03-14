f = open('k001.csv','r',encoding='utf8')
cnt = 0
sum = 0
while True:
    content = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content == '': break
    
    c_list = content.split(',')
    c_list[4] = int(c_list[4])
    sum += c_list[4]
    print(c_list,len(c_list))

print(sum)
f.close()

    # print(content,end='')