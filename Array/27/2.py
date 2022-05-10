class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针法
        slow = fast = 0
        while fast < len(nums):
            
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
        
            # 当 fast 指针遇到要删除的元素时停止赋值
            # slow 指针停止移动, fast 指针继续前进

            fast += 1
            
        return slow
