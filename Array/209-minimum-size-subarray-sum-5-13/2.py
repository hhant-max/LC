# time exeed
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        l, r = 0, 1
        leng = float('inf')

        while l <= r:
            print("-------")
            if sum(nums[l:r+1]) < target:
                r += 1
                print(f'sum is {sum(nums[l:r+1])}')
                print(f"r is {r}")
            else:
                # if minimal update then!
                leng = min(len(nums[l:r+1]), leng)
                l += 1
                print(f"l is {l}")

                
        return 0 if leng == float('inf') else leng

nums = [2,3,1,2,4,3]

test = Solution()
print(test.minSubArrayLen(target=7 , nums=nums))