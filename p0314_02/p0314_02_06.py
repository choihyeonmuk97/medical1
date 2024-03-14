txt = '파이썬 파일 중에 a.txt 가 파이썬 폴더에 존재합니다.hwp'
print(txt.find('자바')) # .find()는 없으면 -1을 출력 
print(txt.find('.')) # 있으면 위치값 리턴
print(txt.count('파이썬')) # 값이 몇개 있는지 개수
print(txt.count('.py')) # .count()는 없으면 0
print(txt.endswith('.hwp')) # 제일 끝에 해당 문자열로 끝나면 True
print(txt.endswith('.')) # 제일 끝에 해당 문자열로 끝나지 않으면 False


