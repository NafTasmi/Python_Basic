from datetime import date
day1=int(input("Enter day: "))
month1=int(input("Enter month: "))
year1=int(input("Enter year: "))
f_date=date(year1,month1,day1)
day2=int(input("Enter day: "))
month2=int(input("Enter month: "))
year2=int(input("Enter year: "))
l_date=date(year2,month2,day2)
diff = l_date - f_date
print("Difference between 2 days: ",diff.days)