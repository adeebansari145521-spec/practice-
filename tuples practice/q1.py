#ADDING ELEMENTS IN A TUPLE

n=int(input("Enter the number of elements :"))
t=()

for i in range(0,n):
    a=int(input("Enter any number :"))
    t+=(a,)
#    t=list(t)
#    t.append(a)
#t=tuple(t)
print(t)



