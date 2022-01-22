# Add a week (7 days) and 12 hours to a given date

# 2020-03-22 10:00:00
from datetime import datetime,timedelta
given_date = datetime(2020, 3, 22, 10, 0, 0)
days_to_add=7
new_date=given_date+timedelta(days=days_to_add)
print(new_date)

