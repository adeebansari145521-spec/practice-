s=input("Enter any statement:")
i=0
new_s=""

while (i<len(s)):
      
    if i%3!=0:
        new_s+=s[i]
        
    i+=1
        
print(f"The new string is \'{new_s}\'")