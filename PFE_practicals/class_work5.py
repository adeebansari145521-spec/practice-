n=int(input("Enter the amount of money available : "))

print(f"The max number of books that can be purchased is {n//35}.")
print(f"The remaining money is ₹{n-((n//35)*35)}.")