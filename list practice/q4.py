#APPEARENCE INDEX COUNTER

def aic(list):
    i=0
    n=int(input("Enter the number you want the index of:"))
    print(f"{n} appears at the indices: ",end="")
    
    while i<len(list):
        if list[i]==n:
            print(i,end=",")
        else:
           pass
        i+=1
   
    '''for i in range((len(list))):
        if list[i]==n:
            print(i,end=",")'''

l=[2,2,3,3,1,3,1,3,1,3,13,1]
aic(l)
