import datetime

x = datetime.datetime.now()

x = x - datetime.timedelta(days = 1)
print(x.strftime("%A"))
x = x + datetime.timedelta(days = 1)
print(x.strftime("%A"))
x = x + datetime.timedelta(days = 1)
print(x.strftime("%A"))

