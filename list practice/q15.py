#COMMON ELEMENTS IN ALIST

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()
l2=creating_list()
l3=[]       #COMMON ELEMENT LIST
i=0

while i<len(l1):
    a=l1[i]
    if a in l2:
        l3.append(a)
    i+=1

print(f"The common elements are {l3}")
    


