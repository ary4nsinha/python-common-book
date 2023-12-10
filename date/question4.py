#write a python program to add some days to your present date and print the date added

import datetime

one = datetime.date.today()
two = datetime.timedelta(days=7)
print(one + two)