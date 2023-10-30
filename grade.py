sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
sub5=float(input("Enter marks of the fifth subject: "))
sub6=float(input("Enter marks of the sixth subject: "))

avg=(sub1+sub2+sub3+sub4+sub5+sub6)/6
if(avg>=80)and(avg<100):
    print("Grade: A+")
elif(avg>=70)and(avg<79):
    print("Grade: A")
elif(avg>=60)and(avg<69):
    print("Grade: B")
elif(avg>=50)and(avg<59):
    print("Grade: C")
elif(avg>=40)and(avg<49):
    print("Grade: D")
else:
    print("Grade: F")
