import datetime

mytime = datetime.time(2, 20, 54, 34)
print(mytime)
print(mytime.minute)
print(mytime.hour)
print(mytime.second)
print(mytime.microsecond)
print(type(mytime))

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

from datetime import datetime

mydatetime = datetime(2022, 10, 3, 14, 20, 1)
print(mydatetime)
print(mydatetime.date())
mydatetime = mydatetime.replace(year = 1994)
print(mydatetime.date())

#DATE
from datetime import date
date1 = date(2021, 11, 3)
date2 = date(2025, 11, 3)
print(date1-date2)
print(type(date1-date2))

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2025, 11, 3, 12, 0)

print(datetime1-datetime2)
print(type(date1-date2))
print((datetime1-datetime2).total_seconds())