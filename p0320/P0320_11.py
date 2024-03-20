def jegob(val):
    return val**2

def func(val):
    return val >= 3

def int_change(val):
    return int (val)



a_list= [1,2,3,4,5]
str_list = ['1','2','3','4','5']

map_list = list(map(jegob,a_list)) # 리스트 전체 값의 변경이 필요할때
print(map_list)

ss_list = list(map(int_change,str_list))
print(str_list)
print(ss_list)

ss_list2 = list(map(lambda val,:int(val),str_list))
print(ss_list2)

f_list = list(filter(func,a_list)) # -> 특정값만 추출할 때
print(f_list)