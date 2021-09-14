# import datetime
from datetime import date, datetime, timedelta


now = datetime.now()
result = now.date()
result = now.year
result = now.day
result = now.hour

result = datetime.ctime(now)
result = datetime.strftime(now,"%Y")
result = datetime.strftime(now,"%X")
result = datetime.strftime(now,"%A")
result = datetime.strftime(now,"%d")
result = datetime.strftime(now,"%Y %B %A")

t = "2 August 2021 hour 10:21:43"
result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")

birthday = datetime(2001,4,5)
result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0) # saniye

result = now - birthday
print(now)
result = now + timedelta(days=30)

print(result)