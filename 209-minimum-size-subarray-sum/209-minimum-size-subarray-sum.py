class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        l = 0
        leng = float('inf')

        for r in range(len(nums)+1):
            while sum(nums[l:r+1]) >= target:
                leng = min(len(nums[l:r+1]), leng)
                l += 1
                
        return 0 if leng == float('inf') else leng