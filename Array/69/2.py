#still not working: for 8 it returns 1?? why
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0 
        nums = [i+1 for i in range(x)]
        
        left, right = 0, len(nums)    
        while left < right:
            mid = (left + right) //2
            if nums[mid] * nums[mid] == x: 
                return nums[mid]
            elif nums[mid] * nums[mid] > x:
                right = mid
            else:
                left = mid + 1
                
        return nums[mid-1]

        
