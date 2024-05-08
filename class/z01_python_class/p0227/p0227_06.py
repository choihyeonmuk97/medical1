# 입력 : 이름, 아이디, 비밀번호 (input)
# 5명을 입력받아 member 리스트 만들기

member = [] 
for i in range(5):
    
    name = input(('이름을 입력하세요 > '))
    id = input(('ID를 입력하세요 > '))
    pw = input(('PW를 입력하세요 > '))
    m = [name,id, pw]
    member.append(m)

print(member)
    
print(' 이름\t아이디\t비밀번호')
# for i in range(5):
#     print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))
   
for i in range(len(member)):
    print(' {}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))


