h=int(input("Enter the number of hours passed :"))
m=int(input("Enter the number of minutes passed :"))
s=int(input("Enter the number of seconds passed :"))

if (h<24 and m<60 and s<60):
    print(f"Total secons passed is {(s)+(m*60)+(h*3600)}")
else:
    print("Please enter a valid choice. ")
