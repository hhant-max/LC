class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumN = 0
        #怎么初始化 最最开始的这个元素呢
        res = -float('inf')
        
        for num in nums:
            sumN += num
            res = max(sumN,res)
            
            if sumN < 0:
                sumN = 0
        
        # 最后res 为负怎么办
        return res
        