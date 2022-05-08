# because left_b 返回值不会 变 所以修改了


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)
        left_b, right_b = -1,-1
        
        while l<r:
            mid = (l+r) //2 
            if nums[mid] == target:
                left_b = mid
                right_b = mid
                break
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid
        
        while left_b -1 >= 0 and nums[left_b-1] ==target: left_b -=1
        while right_b +1 < len(nums) and nums[right_b+1] ==target: right_b +=1
    
        #还是找不到 and the null list
        return [left_b, right_b]
        
