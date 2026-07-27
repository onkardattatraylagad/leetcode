class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0]==0:
            return 0
        max=smax=0
        for i in range(len(nums)):
            if nums[i]>max:
                smax=max
                max=nums[i]
            elif nums[i]<=max and nums[i]>smax:
                smax=nums[i]
        print(max,smax)
        return((max-1)*(smax-1))
        

        