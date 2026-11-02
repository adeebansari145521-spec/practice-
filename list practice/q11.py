# COUNTING NUMBER OF ODD AND EVEN NUMBERS

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()

list_even=[]
list_odd=[]

for item in l1:
    if item%2==0:
        list_even.append(item)
    else:
        list_odd.append(item)

print(f"The number of even elements in the list is {len(list_even)}")
print(f"The number of odd elements in the list is {len(list_odd)}")

