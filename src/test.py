import datetime
last_update = 1
x = datetime.datetime.now()
print(x.day)

if last_update != x.day:
    print("boy you dumb")
    last_update = x.day
    print(last_update)
    