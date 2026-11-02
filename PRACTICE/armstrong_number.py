N=input("Enter any number : ")
n=int(N)
arn=0

for i in range(0,len(N)):
    i=N[i]
    i=int(i)
    arn+=(i**len(N))
    
if arn==n:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not an armstrong number")




