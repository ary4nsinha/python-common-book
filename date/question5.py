#write a program to find out the number of days left for your birthday
import datetime

today=datetime.date.today()
birthday=datetime.date(2024,1,16)
daysLeft=birthday-today
print(daysLeft)

