# un consider the border of list when do the operation of --

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)
        left_b, right_b = -1,-1
        
        while l<r:
            mid = l + (r-l) //2 
            if nums[mid] == target:
                left_b = mid
                right_b = mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid
        
        while left_b >= 0 and nums[left-1] ==target: left -=1
        while right_b <= len(nums) and nums[right+1] ==target: right +=1
    
        #还是找不到 and the null list
        return [left_b, right_b]
        
