class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            # how about the first one??
            # if nums[i] in diff.get(difference,i):
            if difference in diff:
                return [diff[difference], nums[i]]
            
            diff[difference] = i 