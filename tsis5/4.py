import datetime

x = datetime.datetime.today()

y = datetime.datetime(2020, 5, 10,10,40,40,345663)

a = x - y

print(a.days * 24 * 3600 + a.seconds)