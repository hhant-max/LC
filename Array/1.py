class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        l, r, leng = 0, 1, 0

        while l <= r:
            if sum(nums[l:r]) <7:
                r += 1
            else:
                # if minimal update then!
                leng = len(nums[l:r]) if len(nums[l:r]) < leng else -1
                l += 1
        return leng