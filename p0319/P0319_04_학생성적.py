# Student 클래스 생성
class Student:
    count = 1
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float('{:.2f}'.format(self.total / 3))
        self.rank = rank      
        
    def __str__(self): # 객체 호출
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"     

#파일 불러와서 클래스에 저장
students = []
f = open('stu.txt','r',encoding='utf8')

while True:
    txt = f.readline()
    if txt == '' : break
    txt_list = txt.split(',')
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),
                int(txt_list[0]),int(txt_list[7]))
    students.append(s) # 리스트에 클래스 저장함 (주소값으로 저장되어 있음)

f.close()
# 파일 불러온 후 학생수에서 1추가
Student.count = len(students)+1
# for stu in students: # 객체 출력 !! // students엔 주소값이 저장되어 있음 -> stu = 객체
#     print(stu)

#-----------------------함 수 부 분---------------------------
search_txt =[
    '',
    '찾고자 하는 학생의 이름을 입력하세요. > ',
    '몆 점 이상을 검색하겠습니까? > ',
    '몆 점 이하를 검색하겠습니까? > ',
]

def main_title_print():
    print("-"*60)
    print("\t\t  [ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("0. 종료")
    print("-"*60)
    choice = input("원하는 번호를 입력하세요.>> ")
    choice = int(choice)
    return choice

def stu_main_print():
    print('\t\t  [ 학생 성적 출력 ]')
    print('-'*60)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*60)

def stu_insult():
    while True :
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if name == "0":
            print("학생 입력을 취소합니다.")
            break
        kor = int(input("국어점수를 입력하세요."))
        eng = int(input("영어점수를 입력하세요."))
        math = int(input("수학점수를 입력하세요."))
        # list에 추가
        s = Student(name,kor,eng,math)
        students.append(s)
        print("입력 데이터 :",s) 

def stu_print():
    stu_main_print()
        # 데이터 출력
    for i in students:
        print(i) # 객체 출력 (i = 객체)

def search_title_print():
    print('\t\t[ 학생성적검색 ]')
    print('-'*60)
    print('1. 학생 이름으로 검색')
    print('2. 총점 이상 검색')
    print('3. 총점 이하 검색')
    print('0. 이전으로')
    choice = int(input('원하는 번호를 입력하세요. > '))
    return choice

def stu_search(choice):
    if choice == 1:
        search = input(search_txt[choice])
    else:
        search = int(input(search_txt[choice]))
    # 전체 리스트에서 학생검색
    s_list = []
    for i in students:
        if choice == 1:
            if i.name.find(search) != -1:
                s_list.append(i)
        
        elif choice == 2:
            if i.total >= search:
                s_list.append(i)
        
        elif choice == 3:
            if i.total <= search:
                s_list.append(i)
    if len(s_list) != 0:
        # print(f'{search}점 이상 검색된 사람 :')
        stu_main_print()
        for j in s_list:
            print(j)
    else:
        print(f'{search}(으)로 검색된 사람이 없습니다.')


# 시작-------------------------------------------------------
while True:
    choice = main_title_print() # 메인화면
    
    if choice == 1: # 학생 성적 입력
        stu_insult()

    elif choice == 2: # 학생 성적 전체 출력
        stu_print()
    
    elif choice == 3: # 학생 검색
        while True:
            choice = search_title_print()
            if choice == 0:
                print('이전화면으로 이동합니다.')
                break
            # 학생검색 프로그램 부분
            stu_search(choice)
    
    elif choice == 4: # 학생 수정
        while True:
            search = input('수정할 학생의 이름을 입력하세요.(0. 취소) > ')
            cnt = 0
            for i in students:
                if search == i.name:
                    break
                cnt += 1
            
            if cnt != len(students):
                print(f'{i.name}학생 찾음')
                while True:
                    s_input = int(input('수정할 과목 선택 1.국어 2.영어 3.수학 0.취소 '))
                    if s_input == 1:
                        pass
                        
            else:
                print('못찾음')
                
            
            


'''
def stu_main_print():
    print('-'*60)
    print('\t\t[학생성적입력프로그램]')
    print('-'*60)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7. 학생성적 파일 저장')
    print('0. 프로그램 종료')
    print('-'*60)
    choice = input('원하는 번호를 입력하세요. > ')
    print('-'*60)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
    choice = int(choice)
'''
    
    
    
    
    