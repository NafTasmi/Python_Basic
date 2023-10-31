list=[]
n=int(input("Enter the number of colors: "))
for i in range(0,n):
    ele=input()
    list.append(ele)
print("\nExpected colors are: " +list[0],list[-1])
