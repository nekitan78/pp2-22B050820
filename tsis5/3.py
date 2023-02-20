import datetime

x = datetime.datetime.today()
delta = datetime.timedelta(microseconds = x.microsecond)

print(x - delta)
