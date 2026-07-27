class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0]==0:
            return 0
        list=[]
        mul=0
        temp=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                mul=(nums[i]-1)*(nums[j]-1)
                if mul>temp:
                    temp=mul
        return temp
        

        