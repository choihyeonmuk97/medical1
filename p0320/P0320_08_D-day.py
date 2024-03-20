from datetime import datetime
import time


now = datetime.now()
end_time = datetime(2024,6,24)

print((end_time - now).days)
print((end_time - now))