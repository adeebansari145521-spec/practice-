class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i=0
        x=None
        while i<len(nums):

            element=nums[i]
            rem=target-element
            
        
            

            if rem in nums:
                if rem==element:
                    nums.remove(element)
                    nums.insert(i,"a")
                    
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
            
            
        return i,x


