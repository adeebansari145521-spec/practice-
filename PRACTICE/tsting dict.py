marks={"Adeeb":98,"Chandan":90,"Harshit":89}
topper=max(marks,key=marks.get)

#print(topper)
#print(marks[topper])
#print(marks.get("Adeeb"))'''

print(marks.get("Chandan",0))    #Default value
print(f"Siddhant scored", marks.get("Siddhnat",50) ,"marks")   #Default value

'''This is providing a default value if the key is not present in the dictionary '''