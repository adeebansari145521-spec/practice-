#MERGING TWO LIST WITHOUT HAVING ANY DUPLICATES

def creating_list():

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l

l1=creating_list()
l2=creating_list()

def removing_duplicates(list):
    non_dup_list=[]
    for item in list:
        if item in non_dup_list:
            pass
        else:
            non_dup_list.append(item)
    return non_dup_list

l1.extend(l2)
#OR merged_list= l1 +l2
#   for item in l2:
#        l1.append(item)
L1=removing_duplicates(l1)

print(f"The two list merged into one is {L1}")