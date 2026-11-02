#REMOVING DUPLICATE ELEMENTS FROM THE LIST

def creating_list():

    l=[]
    print("Press Enter when you are done creating the list." )
    
    while True:
        n=input("Enter any number:")
        try:
            n=int(n)
            l.append(n)

        except ValueError:
            break
            
    return l

def removing_duplicates(list):
    non_dup_list=[]
    for item in list:
        if item in non_dup_list:
            pass
        else:
            non_dup_list.append(item)
    print(f"The new list is {non_dup_list}")

l=creating_list()
removing_duplicates(l)
        

