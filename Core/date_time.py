import datetime
from datetime import  timedelta, datetime


print((datetime.now() + timedelta(hours=5, minutes=30)).replace(hour=0, minute=0, second=0, microsecond=0))

#today date
date = datetime.today()
date
print(date)
print(date.day)
print(date.year)
print(date.month)

#change  date objct into  str
datetime.today().strftime('%Y-%m-%d')
print(datetime.today().strftime('%Y-%m-%d'))

#change string to date object
datetime.strptime('20/02/2018','%d/%m/%Y')
print(datetime.strptime('20/02/2018','%d/%m/%Y'))

# add days in date object
to_date = datetime.today() + timedelta(days=1)
