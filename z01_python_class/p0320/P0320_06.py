# input으로 입력받은 데이터를
# p0320.txt 파일을 생성해서 저장하기
# p_0320은 현재 날짜를 사용
import datetime

now = datetime.datetime.now()
# print(now.month)
# print(now.day)
print(now.strftime('%m%d')) #.strftime : 날짜, 시간을 str 타입으로 바꿔줌 


# search = input('파일명을 입력하세요. ')

fileName = 'p_' + now.strftime('%m%d') + '.txt'
# f = open(search,'w',encoding='utf8')
with open(fileName,'w',encoding='utf8') as f: # f.close 생략가능함
    print('데이터 입력 : ')

    while True:
        txt_input = input('')
        if txt_input == '-1':
            print('저장되었습니다.')
            break
        f.write(txt_input+'\n')

