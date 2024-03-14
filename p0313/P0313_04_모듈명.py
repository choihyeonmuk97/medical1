# 다른 파일에 있는 함수를 사용할 떄 

# import math -> math.ceil() 이름.함수명()
# from math import * # from 이름 import *(함수) -> 이름 생략가능
import math as m # 모듈명을 줄여서 사용가능 (별칭 부여)
# # ceil : 올림
print(m.ceil(12.2))
# # floor : 버림 (내림)
print(m.floor(12.9))
# # round : 반올림 (import.math 불필요)
print(round(12.6))
print(dir(m))

# import lotto
# from lotto import *
import lotto as lo # 모듈명을 줄여서 사용가능 (별칭 부여)

l = [0]*45

lo.screen()   
lo.num_generate(l)

