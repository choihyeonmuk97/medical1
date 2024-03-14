import os
# str.txt 파일의 내용을 모두 출력
# print(os.listdir())
# for f_name in os.listdir():
#     if f_name.endswith('.txt'):
#         print(f_name)
    
f = open('str.txt','r',encoding='utf8')

while True:
    txt_f = f.readline()
    if txt_f.strip() == '':break
    print(txt_f,end='')
    
    ff = open('str1.txt','a',encoding='utf8')
    ff.write(txt_f + '')

f.close()
ff.close()
print()
print('-'*40)
# str.txt 파일의 내용을 읽어와서
# str1.txt에 그 내용을 추가 ↓


fff = open('str1.txt','r',encoding='utf8')

while True:
    txt_f = fff.readline()
    if txt_f == '':
        break
    print(txt_f,end='')

fff.close()

