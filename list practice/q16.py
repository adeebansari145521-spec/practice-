#COUNT OF ALL ELEMENTS IN A LIST

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()
l2=[]
for item in l1:
    if item in l2:
        pass
    else:
        l2.append(item)
        print(f"{item} appears {l1.count(item)} times in the list")

print(f"This is the list without any duplicates {l2}")