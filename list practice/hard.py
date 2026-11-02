i=0
nums=[2,5,5,4,11]
target=10
x=None
while i<len(nums):
    element=nums[i]
    rem=target-element
    
    if rem in nums:
        if rem==element:
            nums.remove(element)
            nums.insert(i,0)
            
            try:
                x=nums.index(rem)
                        
            except ValueError:
                pass
        else:
            try:
                x=nums.index(rem)
            except ValueError:
                pass
    else:
        pass

    if x!=None:
        break
            
    i+=1
            
            
print(i,x) 
