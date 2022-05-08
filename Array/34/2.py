class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # solution of lu
        # open interval

        # special situation
        if len(nums) == 0: return [-1,-1]
        
        # noraml -> yizizhao
        def rightborder(nums,target) -> int: #[5,7,7,8,8,10] 8
            left, right = 0, len(nums)
            rightborder = -1
            while left < right:
                mid = (right - left)//2
                if target < nums[mid]:
                    right = mid
                else: # target >= target
                    left = mid + 1
                    rightborder = left
                
            return rightborder -1
        
        def leftborder(nums,target) -> int: #[5,7,7,8,8,10] 8
            left, right = 0, len(nums)
            leftborder = -1
            while left < right:
                mid = (right - left)//2
                if target > nums[mid]:
                    left = mid + 1
                else: # target <= target
                    right = mid
                    leftborder = right
                
            return leftborder +1
        
        return [leftborder(nums,target), rightborder(nums,target)]
