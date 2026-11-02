a,b=input("Enter the range sperated by a space :").split()
count=0
a=int(a)
b=int(b)

for i in range(a,b+1):
    I=str(i)
    arn=0
    
    for j in range(0,len(I)):
        k=I[j]
        k=int(k)
        arn+=(k**len(I))

    if i==arn:
        print(f"{i} is an armstrong number ")
        count+=1
    
print(f"There are {count} armstrong number in the range {a},{b} ")

