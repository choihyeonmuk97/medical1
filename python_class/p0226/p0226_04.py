# 
stu = ['홍길동', '유관순', '이순신', '김구', '강감찬']

# 1. 이순신 학생 출력
print(stu[2])
print(stu[-3])

# 2. 김구 이름을 안창호로 변경
stu[3] = '안창호'
print(stu)

# 3. 유관순 부터 강감찬 출력
print(stu[1:])
print(stu[1:4+1])

# 4. 왕건을 추가
stu.append('왕건')
print(stu)

# 5. 홍길동 삭제
stu.remove('홍길동')
print(stu)
# del(stu[0])
# print(stu)