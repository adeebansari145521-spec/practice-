n1=int(input("Enter any number:"))
n2=int(input("Enter any number:"))
n3=int(input("Enter any number:"))

if n2>n1 and n2<n3 :
    print(f"{n2} is second largest number.")
elif n1>n2 and n1<n3 :
    print(f"{n1} is second largest number.")
else:
    print(f"{n3} is second largest number.")