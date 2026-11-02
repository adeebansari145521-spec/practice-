#DISPLAY NUMBER IN REVERSE ORDER

n=int(input("Enter any number:"))
#print(list(range(n,0,-1)))
for i in range(0,n):
    print(n-i,end=",")