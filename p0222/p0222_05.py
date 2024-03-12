# 국어 영어 수학 점수 입력받아 평균을 출력하세요
# 평균운 ??점 입니다.
# 변수 : kor, eng, math

kor = input('국어 점수 >> ')
kor = int(kor)
eng = input('영어 점수 >> ')
eng = int(eng)
math = input('수학 점수 >> ')
math = int(math)

print('평균은 {}점 입니다.'.format((kor+eng+math)/3))

avg = (kor+eng+math)/3

print('평균은 {}점 입니다.'.format(avg))
