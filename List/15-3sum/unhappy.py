class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        for i,n  in enumerate(nums):
            hmap = {}
            target = 0 - n
            
            # target, 2 sum
            for j in range(i+1, len(nums)):
                diff = target - nums[j]
                
                if nums[j] in hmap:
                    res.append([nums[i], hmap[nums[j]], nums[j]])
                
                hmap[diff] = nums[j]
        return res
                                
                
                
                        
                
            
        