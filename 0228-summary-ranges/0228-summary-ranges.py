class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        
        result=[]
        if not nums:
            return result
        
        start = 0
        
        for i in range(1, len(nums) + 1):
            
            # Range ends if numbers are not consecutive
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                
                start = i
        
        return result