# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        
        max_ = max(nums)
        max_index = nums.index(max_)
        root = TreeNode(max_)
        root.left = self.constructMaximumBinaryTree(nums=nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums=nums[max_index+1 :])
        
        return root
        