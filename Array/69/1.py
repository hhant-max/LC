class Solution:
    def mySqrt(self, x: int) -> int:

        
        def binary(nums:list,x) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) //2
                if nums[mid] * nums[mid] == x: 
                    return nums[mid]
                elif nums[mid] * nums[mid] > x:
                    right = mid
                else:
                    left = mid + 1
                
            return mid - 1
        
        searchList = [i+1 for i in range(x)]
        root = binary(searchList,x)
        
        if x == 0 : return 0 
        
