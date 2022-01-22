# Subtract a week (7 days)  from a given date in Python
from datetime import datetime,timedelta
given_date = datetime(2020, 2, 25)
days_subtract=7
res_date=given_date-timedelta(days=days_subtract)
print(res_date)
