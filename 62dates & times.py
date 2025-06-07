# (08:48:29)

# dates & times

import datetime
that_date = datetime.date(2025 , 8 , 25)
today_date = datetime.date.today()
that_time = datetime.time(12,30,0)
today_time = datetime.datetime.now()
now = today_time.strftime("%H:%M:%S %d-%m-%Y")

# print(that_date)
# print(today_date)
# print(that_time)
# print(today_time)
# print(now)

# To check weather a date has passed or not

target_datetime  = datetime.datetime(2026,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
