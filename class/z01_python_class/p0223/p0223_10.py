# 넹
# 성별 키를 입력받아서 남자면 m, 172.5이상이면 평균이상 이하면 평균이하
# 여자일 경우 F, 159.6 이상이면 평균이상, 이하면 평균 이하

gender = input('성별을 입력하세요 >> ')
height = float(input('키를 입력하세요 >> '))

if gender == '남자':
    print('M')
    if height >= 172.5:
        print('평균 이상')
    else:
        print('평균 이하')
elif gender == '여자':
    print('F')
    if height >= 159.6:
        print('평균 이상')
    else :
        print('평균 이하')
else:
    print('잘못 입력하셨습니다.')
    
  
