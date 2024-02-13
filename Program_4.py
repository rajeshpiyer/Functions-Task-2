import datetime

datetime_string = "2020-01-15 09:03:32.744178"
extract = lambda dt: (dt.year, dt.month, dt.day, f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}.{dt.microsecond}")

dt_object = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S.%f')
year, month, day, time = extract(dt_object)

print(datetime_string)
print(year)
print(month)
print(day)
print(time)