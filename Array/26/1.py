class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        for r in range(len(nums)): # attention for r +=1
            if nums[r] > nums[l]: # unique
                l +=1
                nums[l] = nums[r]
                
        return l
                
