students = {'stuNo':1,'stuName':'홍길동','tel':'010-0000-0000',
            'gender':'male','id':'aaa','pw':1111}

# 키 값이 없는 데이터를 가져오려고 할 때는 에러
if 'studentNo' in students:
    print('있다.')
    students['studentNo'] = students['studentNo'] +1
    print(students['studentNo'])
else:
    print('없다.')

