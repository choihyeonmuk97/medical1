class Tv:
    channel = 0
    color = 'black'
    size = 65
    volume = 0
    
    #생성자
    def __init__(self,channel=0,color='',size=0,volume=0):
        self.channel = channel
        self.color = color
        self.size = size
        self.volume = volume
    
    def up_volume(self,volume):
        self.volume += volume
        
    def down_volume(self,volume):
        self.volume -= volume
        
    def up_channel(self,channel):
        self.channel += channel
    
    def down_channel(self,channel):
        self.channel -= channel


# 키워드 매개변수
# 철수 - 10번으로 변경 -> 2 증가, 흰색
t1=Tv(10,'white',65,0)
print('철수 TV :',t1.channel,t1.color,t1.size,t1.volume)
t1.up_channel(2)
print('철수 TV :',t1.channel,t1.color,t1.size,t1.volume)

t1 = Tv()
t1.channel = 10
t1.color = 'white'
t1.size = 65
t1.volume = 0

t1.up_channel(2)

print('철수 TV :',t1.channel,t1.color,t1.size,t1.volume)

# 영희 - 7번 -> 5 증가, 핑크
t2=Tv(7,'pink',65,0)
print('영희 TV :',t2.channel,t2.color,t2.size,t2.volume)
t2.up_channel(5)
print('영희 TV :',t2.channel,t2.color,t2.size,t2.volume)

t2=Tv()
t2.channel = 7
t2.color = 'pink'
t2.size = 65
t2.volume = 0

t2.up_channel(5)

# print('영희 TV :',t2.channel,t2.color,t2.size,t2.volume)

# 반장 - 1번 -> 3 증가, 실버
t3=Tv(1,'silver',65,0)
print('반장 TV :',t3.channel,t3.color,t3.size,t3.volume)
t3.up_channel(3)
print('반장 TV :',t3.channel,t3.color,t3.size,t3.volume)

t3=Tv()
t3.channel = 1
t3.color = 'silver'
t3.size = 65
t3.volume = 0

t3.up_channel(3)

# print('반장 TV :',t3.channel,t3.color,t3.size,t3.volume)