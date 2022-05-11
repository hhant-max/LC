class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: nums = nums
        l = -1
        for r in range(len(nums)-1):
            l += 1
            if nums[r] == 0 :
                r+=1
                tmp = nums[r]
                #nums[r] = nums[l] 
                nums[r] = 0
                nums[l] = tmp
                break
                
            nums[l] = nums[r]
            
