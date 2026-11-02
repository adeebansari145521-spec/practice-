#FUNCTION TO CREATE A LSIT OF NUMBERS

def creating_list():
    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("enter any number:"))
        l.append(n)
    return l

l1=creating_list()
list=[]
for item in l1:
    list.insert(0,item)

print(f"This is the reversed list {list}.")
print(f"This is the original list {l1}.")

        