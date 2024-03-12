member = []

# 입력 : 이름, 점수 (input)
# 3명의 정보를 member리스트에 넣으세요

# for i in range(3):
#     name = input('이름을 입력하세요 > ')
#     score = int(input('점수를 입력하세요 > '))
#     m = [name,score]
#     member.append(m)
# print(member)

member = [['홍길동',55],['유관순',80],['이순신',90]]
# 60점 이상이면 합격, 미만이면 불합격
for i in range(len(member)):
    n = member[i][0]
    s = member[i][1]
    if s >= 60:
        print('{}님 합격입니다.'.format(n))
    else:
        print('{}님 불합격입니다.'.format(n))
        

