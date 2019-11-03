import datetime
today = datetime.date.today()
print(today)

def age_and_remain(birthday):
    now = datetime.datetime.now()
    age = (now - birthday).days // 365
    this_birthday = datetime.datetime(now.year,birthday.month,birthday.day,birthday.hour,birthday.minute,birthday.second)
    next_birthday = this_birthday + datetime.timedelta(days = 365)
    remain =  next_birthday - now
    return (age,remain)


birthday = datetime.datetime(2007,6,20,10,12,18)
print(age_and_remain(birthday))