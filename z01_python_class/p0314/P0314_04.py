# 파일 1개 저장

# file open
file = open('memo.txt','w',encoding='utf-8')
try:
    # file write
    file.write('안녕하세요1.\n')
    file.write('안녕하세요2.\n')
    print(1/0)
    file.write('안녕하세요3.\n')
    file.write('안녕하세요4.\n')
except Exception as e: # Exception : 예외 발생 이유 설명
    print('저장 시 에러가 발생했습니다.')
    print(e)
finally: # 예외 발생 상관없이 무조건 실행
    file.close()
    # file close