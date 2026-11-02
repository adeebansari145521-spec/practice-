# ROTATING A LIST LEFT BY ONE POSITION

def creating_list():  #Returns l 

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l
l1=creating_list()

def rotation(list):

    i=int(input("Enter the index of rotation: "))

    list_first=[]
    list_sec=[]
    R_list=[]

    for n in range(i):
        list_sec.append(list[n])

    for n in range(i+1,len(list)):
        list_first.append(list[n])

    R_list.extend(list_first)
    R_list.append(list[i])
    R_list.extend(list_sec)

    return R_list

Rl=rotation(l1)
print("The list after rotation is ",Rl)