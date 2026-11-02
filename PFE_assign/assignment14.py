d=int(input("Enter the day:"))
m=int(input("Enter the month:"))
y=int(input("Enter the year:"))

def leap_year(y):
    
    if ((y%4==0) and (y%100!=00)) or (y%400==0):
        print(f"{y} is a leap year.")
        return 1
    else:
        print(f"{y} is not a leap year.")
        return 0

Y=leap_year(y)

if Y==1:
    if (d>31) or (m>12):
        print("The date is invalid.")
    elif (m==2) and (d>29):
        print("The date is invalid.")
    elif (m==2 or m==4 or m==6 or m==9 or m==11 ) and (d>30):
        print("The date is invalid.")
    else:
        print("The date is valid.")
else:
    if (d>31) or (m>12):
        print("The date is invalid.")
    elif (m==2) and (d>28):
        print("The date is invalid.")
    elif (m==2 or m==4 or m==6 or m==9 or m==11 ) and (d>30):
       print("The date is invalid.")
    else:
        print("The date is valid.")
        