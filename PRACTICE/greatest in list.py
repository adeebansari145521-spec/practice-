l=[1,-4,23,56,-76,7,8,]
'''largest=l[0]
smallest=l[0]
for item in l:
    if item>largest:
        largest=item
    elif item<smallest:
        smallest=item
print(f"The smallest number in the list is {smallest}")
print(f"The largest number in the list is {largest}")'''

#                       OR
print(max(l))
print(min(l))
