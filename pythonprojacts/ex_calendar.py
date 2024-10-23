import calendar

year=int(input("Enter the year : "))
month = int(input("Enter the month : "))
if 12>=month>=1:
    c = calendar.TextCalendar(calendar.SUNDAY)
    p=c.formatmonth(year,month)
    print(p)
else:
    print("Invalid month| Please enter the month between 1 and 12")
    