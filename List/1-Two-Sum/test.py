from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            # how about the first one??
            # if nums[i] in diff.get(difference,i):
            if difference in diff:
                return [diff[difference], i]
            
            diff[difference] = i 
                
s = Solution()
s.twoSum([1,2,3], target= 3)