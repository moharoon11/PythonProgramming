import datetime

# from datetime import datetime
# from datetime import date
"""" 
We can avoid writing the same thing again and again like
{datetime.datetime} to avoid that

from datetime import datetime
from datetim import date
"""

# working with time and date
print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())
print(datetime.datetime.now().time().second)
print(datetime.datetime.now().time().microsecond)


# working with date
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)