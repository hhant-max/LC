class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针法
        slow = fast = 0
        while fast < len(nums):
            
            if nums[fast] == val:
                fast +=1
            if fast == len(nums): break
            
            nums[slow] = nums[fast]
            
            fast += 1
            slow += 1
            
        return slow
