#! python 3
# import time 

# print("The epoch in this system starts at: " + time.strftime("%c", time.gmtime(0)))

# print("The current timezone is {0} with an offset of {1}. ".format(time.tzname[0], time.timezone))

# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST Timezone is " + time.tzname[1])

# print("Local time is: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC time is: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# import datetime

# print(datetime.datetime.today())


import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz = tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))


for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])