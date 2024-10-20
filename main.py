import modules
from datetime import datetime

today = datetime.today()
req = int(str(today.year) + str(today.month) + str(today.day))

print(f'today: {req}')
print(modules.requestAPI(req))