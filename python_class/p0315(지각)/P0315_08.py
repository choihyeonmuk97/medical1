# stu.txt 파일을 읽어 출력

students = []
with open('stu.txt','r',encoding='utf8') as f :
    while True:
        txt = f.readline()
        if txt == '': break
        t_list = txt.split(',')
        s_dic = {
            'stuNo':int(t_list[0]),'name':t_list[1],
            'kor':int(t_list[2]),'eng':int(t_list[3]),'math':int(t_list[4]),
            'total':int(t_list[5]),'avg':float(t_list[6]),'rank':int(t_list[7])
        }
        students.append(s_dic)
        
print(students)


'''
students = []
f = open('stu.txt','r',encoding='utf8')
while True:
    txt = f.readline()
    if txt == '': break
    t_list = txt.split(',')
    # print("{},{},{},{},{},{},{}".format(*t_list))
    s_dic = {
        'stuNo':int(t_list[0]),'name':t_list[1],'kor':int(t_list[2]),'eng':int(t_list[3]),
        'math':int(t_list[4]),'total':int(t_list[5]),'avg':float(t_list[6]),'rank':int(t_list[7])
    }
    students.append(s_dic)
    
print(students)    
        
f.close()
'''







