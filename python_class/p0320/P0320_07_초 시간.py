from datetime import datetime
import time


for i in range(10):
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S')) # 날짜를 스트링 타입으로 출력
    time.sleep(1)   
 