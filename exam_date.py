from datetime import date, datetime
day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
exam_date=date(year,month,day)
print("Exam date is: ",exam_date)