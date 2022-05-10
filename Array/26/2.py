class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # point is to encunter the first one and put it into 
        # from youtueb solution
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
                

        
