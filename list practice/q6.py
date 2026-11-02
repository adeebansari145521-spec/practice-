def creating_list():

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("enter any number:"))
        l.append(n)
    return l

def avg_list(lst):
    avg=sum(lst)/len(lst)
    print(f"The average of elements in the list is : {avg}")
    return avg

lst=creating_list()
choice=input(("Enter y/n if you want to find the average of list:"))
if choice.lower()=="y":
    avg_list(lst)
else:
    print("Program end.")

