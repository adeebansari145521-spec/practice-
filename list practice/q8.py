#FINDING LARGEST AND SECOND LARGEST NUMBER

#1 Using sort method
def creating_list():

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l

def largest_sec_largest(list):
    list.sort(reverse=True) #Ascending arrangement happens that's why reverse is used
    print(f"Largest number is {list[0]} and the second largest number is {list[1]}")

list_input=creating_list()
largest_sec_largest(list_input)

#2 By using pop
def creating_list():

    l=[]
    N=int(input("Enter the number of elements in the list:"))

    for i in range(N):
        n=int(input("Enter any number:"))
        l.append(n)
    return l

def find_largest(list):
    list.sort(reverse=True)
    largest=list.pop(0)
    sec_largest=list.pop(0)
    print(f"The largest number is {largest} and the second largest number is {sec_largest}")

l=creating_list()
find_largest(l)


