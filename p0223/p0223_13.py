'''
# 빈 리스트 생성
cont = []

c1 = input('1. 나라를 입력해주세요 >> ')
c2 = input('2. 나라를 입력해주세요 >> ')
c3 = input('3. 나라를 입력해주세요 >> ')
c4 = input('4. 나라를 입력해주세요 >> ')

print(cont)
cont.append(c1)
cont.append(c2)
cont.append(c3)
cont.append(c4)
print(cont)

# 미국 - 영국 - 프랑스 - 이탈리아
print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3]))
'''
f = []
f1 = input('과일 이름을 입력하세요 > ')
f2 = input('과일 이름을 입력하세요 > ')
f3 = input('과일 이름을 입력하세요 > ')
f4 = input('과일 이름을 입력하세요 > ')

f.append(f1)
f.append(f2)
f.append(f3)
f.append(f4)

print('{}-{}-{}-{}'.format(f[0],f[1],f[2],f[3]))
print('내가 좋아하는 과일은 {},{},{},{}입니다.'.format(f[0],f[1],f[2],f[3]))



