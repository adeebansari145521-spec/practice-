a,b=input("Enter the start and end of the range seperatd by comma :").split(",")
a=int(a)
b=int(b)
count=0
for j in range(a,b+1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        if j==1:
            pass
        else:
            print(f"{j} is a prime number.")
            count +=1


print(f"The number of prime number in the range {a},{b} is {count}.")