#SUM O FELEMENTS AT EVEN AND ODD PLACES SEPERATELY 

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()
i=0
sume=0
sumo=0

while i<len(l1):
    if (i+1)%2==0:
        sume+=l1[i]
    else:
        sumo+=l1[i]
    i+=1

print(f"The sum of digits at odd places is {sumo}")
print(f"The sum of digits at even places is {sume}")