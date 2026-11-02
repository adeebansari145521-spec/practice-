n=int(input("Enter any natural number:"))
sum=0
average=0

for i in range(1,n+1):
    sum+=i

average=sum/n

print(f"Sum is {sum}")
print(f"Average is {average}")

