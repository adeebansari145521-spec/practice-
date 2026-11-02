def sort_dict_value():
    marks={"Adeeb":98,"Harshit":75,"Chandan":87}
    sahi_list=sorted(marks,key=marks.get)
    list2=sahi_list.copy()
    for key in sahi_list :
        print(key,end="")
        if sahi_list:
            
            print(", ",end="")
        else:
            print(".")
        
sort_dict_value()


