l=str(input("Enter list: "))
n=str(input("Enter name to search: "))

if n in l:
    print(n, "found at index", l.index(n))
else :
    print(n, "not found in list")
