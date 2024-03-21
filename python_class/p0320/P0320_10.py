def func(n,*val,a=2):
    for i in range(n):
        for v in val:
            print(v)
            
func(5,"안녕","하세요","")
