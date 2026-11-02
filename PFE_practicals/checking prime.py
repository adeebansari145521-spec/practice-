n=int(input("Enter any number:"))
if n<=1 :
    print("Number is not prime.")
else:
    for i in range(1,n):
        if n==2 :
            print("Number is prime.")

            break
        elif n%i==0 and i!=1:
            print("Number is not prime.")