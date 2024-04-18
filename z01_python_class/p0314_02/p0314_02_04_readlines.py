# 파일 읽기

# 1. 파일 열기
# read() : 모든 문자열을 가져옴
# readline() : 한 줄씩 가져옴 / type - str
# readlines() : 한 줄씩 리스트 타입으로 저장하여 가져옴 / type - list
# 3. 파일 닫기 / .close()

# 파일 확인
import os
if os.path.exists('str1.txt'): # 파일이 존재하는지 확인
   
    with open('str.txt','r',encoding='utf8') as f: # 변수명을 뒤에 씀
        txt_list = f.readlines()

        for txt in txt_list:
            print(txt,end='')
        print()
    # with open ~ 사용 시f.close() 생략 가능

else:
    print('파일이 존재하지 않습니다.')


# readlines
# f = open('str.txt','r',encoding='utf8')
# txt_list = f.readlines() # 한 줄씩 리스트 타입으로 가져옴
# print(txt_list)

# print(txt_list[0])
# f.close()




# readline 한 줄만 str 타입으로 가져옴
# f = open('str.txt','r',encoding='utf8')
# while True:
#     txt = f.readline()
#     if txt == '':
#         break
#     print(txt,end='')
#f.close()
    