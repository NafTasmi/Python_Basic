num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

sum = num1 + num2 + num3
percentage = (sum/300)*100
print("Total marks obtained : ", sum)
print("Percentage: ", percentage)



if (percentage >= 40) and (num1 >= 33) and (num2 >= 33) and (num3 >= 33):
  print("You are PASS")
else:
  print("You are FAIL")


