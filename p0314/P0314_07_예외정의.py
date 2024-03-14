# 예외 : 프로그램 실행 시 알 수 없는 오류로 인한 프로그램 종료를 방지
# 프로그램 에러 : 프로그램을 실행하면서 수정 해야함

# try: 프로그램에서 오류가 발생될 것 같은 소스
# except: 예외 발생 시 처리 구문 키워드
# except Exception as e: 예외 발생 시 어떤 예외가 발생되었는지 확인 / print(e)
# 예외 종류별로 except 처리 가능
# ValueError, IndexError, ZeroDivisionError
# else : 예외 발생하지 않을 시 처리하는 키워드
# finally : 예외 발생 상관 없이 무조건 실행하는 키워드
# raise : 강제로 에러를 발생시키는 키워드



print('1. 학생성적입력')
print('2. 학생성적출력')
print('3. 학생성적수정')
num = int(input('숫자를 입력하세요. > '))
if num == 1:
    print('학생성적입력 완성')
    
elif num == 2:
    # print('김과장이 해야 할 부분')    
    raise '김과장에게 소스를 받아야 함' # 강제로 에러를 발생시키는 키워드
elif num == 3:
    # print('이대리가 해야 할 부분')
    pass