# 점수를 입력받아서 90점 이상 A , 80점 이상 B, 70점 이상 C, 나머지 F

score = int(input('점수를 입력하세요 : '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
    
# 98점 이상은 A+, 90~93 A-, B+, B-, C+, C-

if score >= 90:  
    if score >= 98:
        print('A+')
    if 93 < score < 98:
        print('A')
    if 90 < score <= 93:
        print('A-')
elif score >= 80:
    if score >= 88:
        print('B+')
    if 83 < score < 88:
        print('B')
    if 80 < score <= 83:
        print('B-')
elif score >= 70:
    if score >= 78:
        print('C+')
    if 73 < score <78:
        print('C')
    if 70 < score <= 73:
        print('C-')
else:
    print('F')




if score >= 90:  
    if score >= 98:
        print('A+')
    elif score > 93:
        print('A')
    else:
        print('A-')
elif score >= 80:
    if score >= 88:
        print('B+')
    elif score > 83:
        print('B')
    else:
        print('B-')
elif score >= 70:
    if score >= 78:
        print('C+')
    elif score >73:
        print('C')
    else:
        print('C-')
else:
    print('F')
    