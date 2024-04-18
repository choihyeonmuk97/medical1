# 파일 열기
file = open('memo.txt','r',encoding='utf-8')

# 파일 읽기
content = file.read() # 메모장에 있는 모든 글을 읽어옴 
content = content.strip() # strip() : 문자열 빈 공백 제거
print(content)
# .split() : 문자열을 쉼표로 분리 / type : list
stuNo,name,kor,eng,math = content.split('\n')
c_list = [0]*5
c_list[0] = int(stuNo)
c_list[1] = name
c_list[2] = int(kor)
c_list[3] = int(eng)
c_list[4] = int(math)
 
print(c_list)
# 파일 닫기
file.close()