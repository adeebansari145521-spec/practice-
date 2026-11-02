#APPERENCE COUNTER

l=[1,1,1,1,2,2,23,3,4]
def counter(list):
    n=int(input("Enter the number you want to know the count of:"))
    count=list.count(n)
    print(f"{n} appears {count} times in the list.")

counter(l)