f = ['사과','복숭아','딸기','배','포도','수박']

# 1. 딸기
print(f[2])

# 2. 포도 -> 망고
f[4] = '망고'
print(f)

# 3. 배 부터 끝까지
print(f[3:])
print(f[3:5+1])

# 복숭아, 딸기 출력
print(f[1:3])

# 4. 사과 추가
f.append('사과')
print(f)

# 5. 감 추가
f.append('감')
print(f)

# 6. 사과 삭제
f.remove('사과')
print(f)

# 7. 수박이 있으면 수박이 있습니다 출력
if '수박' in f:
    print('수박이 있습니다.')
else:
    print('수박이 없습니다.')
    
if '수박' not in f:
    print('수박이 없습니다.')
else:
    print('수박이 있습니다.')
    
num = [10,20,30,40,50]
# 60이 없으면 60 추가
if 60 not in num:
    num.append(60)
    print(num)
else:
    print(num)

# 20이 있으면 70추가, 20삭제
if 20 in num:
    num.append(70)
    num.remove(20)
    print(num)
else:
    print(num)

aa = [[1,2],[3,4]]
print(aa[0][1])
print(aa[1][1])

a1 = [1,2]
a2 = [3,4]
a3 = [a1,a2]

stu1 = ['홍길동',90]
stu2 = ['유관순',100]
student = [stu1, stu2]

# student를 사용해서 유관순 출력
print(student[1][0])

#                   홍길동 점수를 80으로 수정
student[0][1] = 80
print(student)

# 이순신 95점을 student에 추가
stu3 = ['이순신',95]
student.append(stu3)
print(student)

# 유관순 100점이면 100점입니다.
if student[1][1] == 100:
    print('100점 입니다.')
