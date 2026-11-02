#GIVEN A SEQUENCE OF INTEGERS ENDING WITH 0. DETERMINE THE LENGTH OF THE WIDEST FRAGMENT
#    WHERE ALL THE ELEMENTS ARE EQUAL TO EACH OTHER.

largest=0
previous=None
current=0

while True:
    n=int(input("Enter any number (enter 0 to stop):"))
    if n==0:
        break
    if n==previous:
        current+=1
    else:
        current=1
    largest=max(largest,current)
    previous=n

print(f"Widest fragment length is {largest}")


