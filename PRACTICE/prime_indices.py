def prime(n):

    if n<0 or n==0 or n==1:
        #print(f"{n} is not a prime number")
        return 0

    else:
        for i in range(2,n+1):
        
            if n%i==0 and i!=n:
                #print("Not a prime number")
                return 0
                


            elif n%i==0 and i==n:
                #print("Prime number")
                return 1

s=input("Enter anything:")
res=""
for i in range(0,len(s)):

    if prime(i)==1:
        pass
    else:
        res+=s[i] 
print(res)