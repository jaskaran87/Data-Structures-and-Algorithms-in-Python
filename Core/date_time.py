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
datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(datetime.today().strftime('%Y-%m-%d'))

#change string to date object
datetime.strptime('20/02/2018','%d/%m/%Y')
print(datetime.strptime('20/02/2018','%d/%m/%Y'))

# add days in date object
to_date = datetime.today() + timedelta(days=1)

datetime.now().strftime('%Y%m%d%H%M%S')

#timespan

totsec = 14356
h = totsec//3600
m = (totsec%3600) // 60
sec =(totsec%3600)%60 #just for reference
print "%d:%d" %(h,m)


date_time = datetime.datetime.now()
date = date_time.day + date_time.month + date_time.year  + date_time.hour + date_time.second + date_time.minute + date_time.microsecond