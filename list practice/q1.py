#PRINTING THE FIRST,MIDDLE, AND TEH LAST ELEMENT OF A

list=[]
for i in range(5):
    n=int(input("Enter any number:"))
    list.append(n)

l=len(list)
middle=int((l+1)/2)

print(f"The first element is",list[0] )
print(f"The middle element is",list[middle-1])
print(f"The last element is",list[l-1])
