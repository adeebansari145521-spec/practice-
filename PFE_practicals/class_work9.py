for i in range(1,4):
    a=int(input("Enter the angle :"))
    sum=0
    if a<180:
        sum+=a

    else:
        print("Please enter a valid choice.")
if sum==180:
    print("Trianlge is valid")
else:
        print("Trianlge is invalid")