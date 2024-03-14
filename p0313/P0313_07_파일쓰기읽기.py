import os

# 파일 생성
# f = open('students.txt','w',encoding='utf-8') 
# f.write("1,'홍길동',100,99,87,286,95.33,2\n")
# f.write("2,'유관순',98,93,87,278,92.67,3")
# f.close() # 파일 닫기

# # 파일 생성 - with를 사용하면 f.close() 사용하지 않아도 됨.
# with open('students.rxr','w') as f:
#     f.write("1,'홍길동',100,99,87,286,95.33,2")
    

# 파일 읽어오기
t_list = []
out_f = open('students.txt','r',encoding='utf-8')
while True:
    txt = out_f.readline() # 1줄씩 읽어오기
    # print(type(txt))
    if txt == '':
        break
    print(txt,end='')
    t_list.append(txt)
print()
print(t_list)
out_f.close()

# 파일 삭제
os.remove('students.txt')



# 폴더가 존재하는지 확인
# if not os.path.exists('hello'):
#     os.mkdir('hello')
# else:
#     print('폴더가 존재합니다.')

#os.rmdir('hello')
