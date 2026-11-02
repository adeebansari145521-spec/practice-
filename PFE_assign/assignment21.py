#CALCULATE FACTORIAL OF A NUMBER

n=int(input("Enter any number :"))
factorial=1

if n<=0:
    print("Enter a positive integer")

else :
    for i in range(1,n+1):
        factorial*=i

print(f"Factorial is {factorial}")