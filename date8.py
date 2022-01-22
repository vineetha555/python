# Convert the following datetime into a string

from datetime import datetime
given_date = datetime(2020, 2, 25)
res_date=given_date.strftime("%Y-%m-%d %H:%M:%S")
print(res_date)