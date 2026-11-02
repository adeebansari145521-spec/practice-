# SHIFTING THE LIST TO THE RIGHT BY ONE ELEMENT 

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()

def shift_right(list):

    n=len(list)
    a=list.pop(n-1)
    list.insert(0,a)

    return list

shift_list=shift_right(l1)
print(f"The list after shifting is {shift_list}")