nums=[-1,1,0,2,-1,-4]


for i in range(0,len(nums)):
    solution=[]
    for j in range(i+1,len(nums)):
        for k in range(i+2,len(nums)):
                    
            if nums[i]+nums[j]+nums[k]==0:
                solution.append(nums[i],nums[j],nums[j])

    