# list
# 변수명 = [요소1,요소2,....]

fruits = ['딸기','사과','배','포도','한라봉']
# 사과 출력
f1 = fruits[1]
print(f1)
# 수박을 리스트에 추가 : .append
fruits.append('수박')
print(fruits)

# if - list
if '귤' in fruits:
    print('귤이 있습니다.')
else:
    print('귤이 없습니다.')
    
for f in fruits: # 변수 in list:
    print(f)

for i in range(len(fruits)): # 리스트의 길이만큼 
    print(i)
    print(fruits[i])
    
num = [[1,2,3],[4,5,6],[7,8,9]]
# 1,4,7 출력
print(num[0][0])
print(num[1][0])
print(num[2][0])

for i in range(len(num)):
    print(num[i][0])

con = ['미국','영국','일본','중국','스페인']
lang = ['영어','영어','일본어','중국어','스페인어']

# 프랑스, 프랑스어 추가
con.append('프랑스')
print(con)
lang.append('프랑스어')
print(lang)

# for 문을 사용하여 미국은 영어를 사용합니다 ~~ 출력
for i in range(len(con)):
    print('{}은 {}를 사용합니다.'.format(con[i],lang[i]))

