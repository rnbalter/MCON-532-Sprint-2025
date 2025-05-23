from datetime import datetime, timedelta
import pytz
from pytz import timezone
from dateutil import parser

#exercise 1
d1 = datetime.strptime("07-05-2025", "%d-%m-%Y")
d2 = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
d3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")

print(d1, d2, d3)


#exercise 2
now = datetime.now()
print("Current Date and Time:", now)
print("Month-Day-Year:", now.strftime("%m-%d-%Y"))
print("Hour:Minute AM/PM:", now.strftime("%I:%M %p"))
print("Log Timestamp:", now.strftime("[%d/%b/%Y:%H:%M:%S]"))

#exercise 3
utc_now = datetime.now(pytz.utc)
print("UTC Time:", utc_now)

LA = timezone('America/Los_Angeles') #US/Los Angeles isnt its own tz acc to wikipedia
local_time = utc_now.astimezone(LA)
print("LA Time:", local_time)

#exercise 4
dt1 = parser.parse("2025-05-07")
dt2 = parser.parse("2025-12-25")
print(dt1, dt2)
from dateutil.relativedelta import relativedelta

diff = relativedelta(dt2, dt1)
print(f"Difference of calendar dates: {diff.months} months, {diff.days} days")
print(f"Difference of total days: {(dt2-dt1).days}")

#exercise 5
Tokyo = timezone('Asia/Tokyo') #US/Los Angeles isnt its own tz acc to wikipedia
local_time = utc_now.astimezone(Tokyo)
print("Tokyo Time:", local_time)

Paris = timezone('Europe/Paris') #US/Los Angeles isnt its own tz acc to wikipedia
local_time = utc_now.astimezone(Paris)
print("Paris Time:", local_time)

#exercise 6
iso1 = "2025-01-22T15:10:45"
iso2 = "2025-01-22T14:12:00"

def later_dat (iso1, iso2):
    d1 = datetime.fromisoformat(iso1)
    d2 = datetime.fromisoformat(iso2)
    return d1 if d1 > d2 else d2

print(f"The later time is: {later_dat(iso1, iso2)}")

#exercise 7
now = datetime.now(pytz.utc)
threewks = now + timedelta(weeks = 3)
print(f"Now: {now.isoformat()}, \n Three Weeks: {threewks.isoformat()}")

#threemth = now + timedelta(weeks = -12)
#timedelta() does not have months parameter - this assumes that each month is perfectly 28 days??
threemth = now - relativedelta(months = 3)
print(f"Now: {now.isoformat()}, \n Three Months Ago: {threemth.isoformat()}")