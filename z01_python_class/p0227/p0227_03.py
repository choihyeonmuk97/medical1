# list
# 리스트 = [요소1,요소2,요소3]
# 요소 하나하나가 변수 (int, bool, float, string, list)
l1 = ['홍길동', 100]
l2 = [[2,4,6],[1,3,5]]
l3 = [True, False, 3.14, 'hello', [1,2], 5]

# index : 리스트 검색, 접근
# index는 0부터 시작
# 홍길동
print(l1[0])
# l2에서 3
print(l2[1][1])

# l3 에서 
# False
print(l3[1])
# hello
print(l3[3])
# 1
print(l3[4][0])
# 5
print(l3[5])

# index를 이용하여 요소값 수정
# l3에서
# True > False
l3[0] = False
print(l3)

# 3.14 > 31.4
l3[2] = 31.4
print(l3)

# 'hello' > 'hi'
l3[3] = 'hi'
print(l3)

# 2 > 20
l3[4][1] = 20
print(l3)

# 리스트 슬라이스 : 자르기
# 리스트명[시작인덱스:끝인덱스+1]
num = [0,1,2,3,4,5,6,7]
print(num[1:6]) # 1 이상 6 미만

str1 = ['a','b','c','d','e','f']
# c,d
print(str1[2:4])
# b,c,d,e,f
print(str1[1:])
# a,b,c
print(str1[0:3])
# a,b,c,d,e,f
print(str1[:])
print(str1[0:7])
# b,c,d,e
print(str1[1:5])

# 리스트의 길이 len(리스트명)
print(l1, len(l1))
print(l2, len(l2))
print(len(l2[0]))
print(l3, len(l3))
print(str1, len(str1))

# 리스트 값 추가 : .append()
num.append(8)
num.append('숫자')
num.append([0,1,2])
print(num)

# str1에 ㄱ,ㄴ,ㄷ, [1,2,3] 추가
str1.append('ㄱ')
str1.append('ㄴ')
str1.append('ㄷ')
str1.append([1,2,3])
print(str1)

# 리스트 값 삭제 : .remove()
num.remove(7)
print(num)

# str1 에서 a,c,f 삭제
str1.remove('a')
str1.remove('c')
str1.remove('f')
print(str1)

# 요소 확인 : 내부에 포함된 요소를 확인 in, not in
print(1 in num) # > T , F
print(10 not in num) # > T, F

lan = ['영어','한국어','일본어','스페인어','중국어']
print('영어' in lan)
print('한글' in lan)

if '일본어' in lan:
    print('True')
else:
    print('False')
    
tmp=[['미국','영국','일본','중국','스페인'],
     ['영어','영어','일본어',',중국어','스페인어']]
# 일본어 출력
print(tmp[1][2])
# 중국을 대만으로 변경
tmp[0][3] = '대만'
print(tmp)
# 일본부터 스페인
print(tmp[0][2:])
# 프랑스, 프랑스어 추가
tmp[0].append('프랑스')
tmp[1].append('프랑스어')
print(tmp)






