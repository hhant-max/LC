class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0 
        r = len(nums) -1
        lst = list()
        while l <= r:
            if (nums[l])**2 < (nums[r])**2:
                lst.append((nums[r])**2)
                r -= 1
            else:
                lst.append((nums[l])**2)
                l += 1
            
        # return lst[:-1]
        return lst[::-1]
            
        