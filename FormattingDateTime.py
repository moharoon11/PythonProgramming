from datetime import datetime
from datetime import date

now = datetime.now()

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%Y %H:%M:%S"))
print(now.strftime("%d/%b/%Y %H:%M:%S"))
print(now.strftime("%d/%A/%Y %H:%M:%S"))
print(now.strftime("%d/%a/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%A/%Y %H:%M:%S"))
print(now.strftime("%d/%b/%a/%Y %H:%M:%S"))


